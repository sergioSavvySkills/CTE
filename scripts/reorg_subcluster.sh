#!/usr/bin/env bash
# Reorganize repo to subcluster-scoped layout.
#
# Before:
#   library/atoms/<subcluster>/
#   library/credentials/clusters/<cluster>/<subcluster>.{md,csv}
#   library/credentials/clusters/<cluster>/<subcluster>/{objectives,crosswalks}/
#   templates/<state>/<subcluster>/
#   crosswalks/{_schema.md, reports.md}
#   templates/_schema.md
#
# After:
#   library/_schemas/{atom.md, template.md, crosswalk.md}
#   library/<cluster>/<subcluster>/_index.md
#   library/<cluster>/<subcluster>/credentials/{_index.csv, <cred>.csv}
#   library/<cluster>/<subcluster>/atoms/
#   library/<cluster>/<subcluster>/crosswalks/<state>/
#   library/<cluster>/<subcluster>/templates/<state>/
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== Step 1: schemas =="
mkdir -p library/_schemas
git mv templates/_schema.md library/_schemas/template.md
git mv crosswalks/_schema.md library/_schemas/crosswalk.md

echo "== Step 2: promote clusters =="
for cluster_dir in library/credentials/clusters/*/; do
    cluster=$(basename "$cluster_dir")
    echo "  cluster: $cluster"
    mkdir -p "library/$cluster"
    for sub_file in "$cluster_dir"*.md "$cluster_dir"*.csv; do
        [ -f "$sub_file" ] || continue
        base=$(basename "$sub_file")
        sub="${base%.*}"
        ext="${base##*.}"
        mkdir -p "library/$cluster/$sub/credentials"
        if [ "$ext" = "md" ]; then
            git mv "$sub_file" "library/$cluster/$sub/_index.md"
        else
            git mv "$sub_file" "library/$cluster/$sub/credentials/_index.csv"
        fi
    done
    for sub_dir in "$cluster_dir"*/; do
        [ -d "$sub_dir" ] || continue
        sub=$(basename "$sub_dir")
        mkdir -p "library/$cluster/$sub"
        if [ -d "$sub_dir/objectives" ]; then
            mkdir -p "library/$cluster/$sub/credentials"
            for obj in "$sub_dir/objectives"/*; do
                [ -f "$obj" ] || continue
                git mv "$obj" "library/$cluster/$sub/credentials/$(basename "$obj")"
            done
            rmdir "$sub_dir/objectives"
        fi
        if [ -d "$sub_dir/crosswalks" ]; then
            git mv "$sub_dir/crosswalks" "library/$cluster/$sub/crosswalks"
        fi
        rmdir "$sub_dir" 2>/dev/null || true
    done
    rmdir "$cluster_dir" 2>/dev/null || true
done

echo "== Step 3: atoms =="
if [ -d library/atoms/it-support-services ]; then
    mkdir -p library/digital-technology/it-support-services
    git mv library/atoms/it-support-services library/digital-technology/it-support-services/atoms
    rmdir library/atoms 2>/dev/null || true
fi

echo "== Step 4: templates =="
for state_dir in templates/*/; do
    [ -d "$state_dir" ] || continue
    state=$(basename "$state_dir")
    for sub_dir in "$state_dir"*/; do
        [ -d "$sub_dir" ] || continue
        sub=$(basename "$sub_dir")
        # Cluster inference: we only have IT Support so far, hardcode lookup
        cluster=$(find library -maxdepth 2 -type d -name "$sub" | head -1 | awk -F/ '{print $2}')
        if [ -z "$cluster" ]; then
            echo "  WARN: cluster unknown for subcluster $sub"
            continue
        fi
        mkdir -p "library/$cluster/$sub/templates/$state"
        for f in "$sub_dir"*; do
            [ -e "$f" ] || continue
            git mv "$f" "library/$cluster/$sub/templates/$state/$(basename "$f")"
        done
        rmdir "$sub_dir" 2>/dev/null || true
    done
    rmdir "$state_dir" 2>/dev/null || true
done
rmdir templates 2>/dev/null || true

echo "== Step 5: crosswalk reports =="
if [ -f crosswalks/texas-it-support-coverage-report.md ]; then
    git mv crosswalks/texas-it-support-coverage-report.md library/digital-technology/it-support-services/crosswalks/texas/coverage-report.md
fi
if [ -f crosswalks/texas-it-support-sme-review.md ]; then
    git mv crosswalks/texas-it-support-sme-review.md library/digital-technology/it-support-services/crosswalks/texas/sme-review.md
fi
rmdir crosswalks 2>/dev/null || true

echo "== Step 6: cleanup =="
rmdir library/credentials/clusters 2>/dev/null || true
rmdir library/credentials 2>/dev/null || true

echo "Done."
