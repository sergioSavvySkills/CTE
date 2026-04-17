---
atom_id: virtualization-concepts
title: Virtualization Concepts
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core1::4.1
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - operating-systems-overview
  - hardware-components-overview
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to explain virtualization, distinguish between Type 1 and Type 2 hypervisors, and describe common IT uses for virtual machines.

## Content stub

- **What is virtualization:** abstracting hardware to run multiple OS instances on one physical host; key benefits (consolidation, isolation)
- **Type 1 hypervisors:** bare-metal; runs directly on hardware; VMware ESXi, Hyper-V, KVM; used in data centers
- **Type 2 hypervisors:** runs on a host OS; VirtualBox, VMware Workstation, Parallels; used for desktops and testing
- **VM components:** vCPU, vRAM, virtual disk (VMDK/VHD), virtual NIC; how each maps to physical resources
- **Snapshots and clones:** snapshot saves VM state; clone creates a full copy; use in testing and rollback scenarios
- **Resource contention:** overcommitting RAM/CPU; impact on VM performance; why VMs slow each other down

## Assessment stub

- Hypervisor comparison: create a table comparing Type 1 vs. Type 2 on 5 criteria
- Short answer: why would a school IT lab use VMs instead of physical machines for student practice?
- Scenario: a technician wants to safely test malware — what VM configuration minimizes risk to the host?
