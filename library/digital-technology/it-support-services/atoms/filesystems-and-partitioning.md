---
atom_id: filesystems-and-partitioning
title: Filesystems and Disk Partitioning
subcluster: it-support-services
credential_objectives:
  - google-it-support::c3m4
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - storage-technologies
  - file-management
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to create and manage disk partitions, format volumes with the appropriate file system, and use Disk Management and CLI tools to perform disk operations.

## Content stub

- **MBR vs. GPT:** MBR limits (2 TB, 4 primary partitions); GPT advantages (128 partitions, UEFI); when each is used
- **Partition types:** primary, extended, logical on MBR; EFI System Partition; recovery partitions
- **Windows Disk Management:** initialize a disk, create/delete/format/extend volumes; assign drive letters; convert MBR↔GPT
- **diskpart CLI:** list disk/partition/volume, select, clean, create partition primary, format, assign; scripting disk setup
- **Linux partitioning:** fdisk, gdisk, parted; /dev/sda naming; mounting partitions; /etc/fstab for persistence
- **Volume types:** simple, spanned, striped (RAID-0), mirrored (RAID-1) in Windows; LVM basics on Linux

## Assessment stub

- Lab: attach a virtual disk to a VM, initialize as GPT, create two partitions, format each, and assign drive letters
- diskpart script: write a diskpart script that would prepare a blank USB drive as a bootable FAT32 volume
- Short answer: why can't a 3 TB drive be fully used with an MBR partition scheme?
