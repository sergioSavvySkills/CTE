---
atom_id: remote-access-and-virtual-machines
title: Remote Access and Virtual Machines
subcluster: it-support-services
credential_objectives:
  - google-it-support::c3m6
skill_type: knowledge
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - virtualization-concepts
  - windows-client-networking
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to configure and use remote desktop tools, and create and manage a basic virtual machine using a hosted hypervisor.

## Content stub

- **Remote Desktop Protocol:** enabling RDP on Windows; client connection; firewall rules; port 3389; NLA requirement
- **SSH remote access:** key-based vs. password auth; PuTTY and Windows Terminal; basic SSH commands for remote admin
- **VNC and third-party tools:** TeamViewer, AnyDesk, Chrome Remote Desktop; use cases vs. RDP/SSH; attended vs. unattended
- **Hosted hypervisors:** VMware Workstation, VirtualBox, Hyper-V (Windows Pro); guest additions/tools; snapshot workflow
- **VM configuration:** vCPU count, RAM allocation, disk type (dynamic vs. fixed), network modes (NAT/bridged/host-only)
- **Use cases for VMs:** safe testing environment, running legacy software, dev/test isolation, sandboxing

## Assessment stub

- RDP lab: enable RDP on a Windows VM and connect to it from the host machine
- VM creation: create a new VM in VirtualBox, install an OS, and take a snapshot before making changes
- Short answer: what is the difference between NAT and bridged networking mode in a VM?
