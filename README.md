# Ansible role: IPv6
[![Travis (.org)](https://img.shields.io/travis/mehdicopter/ansible-role-ipv6)](https://travis-ci.org/mehdicopter/ansible-role-ipv6)
[![Ansible Role](https://img.shields.io/ansible/role/42479)](https://galaxy.ansible.com/mehdicopter/ipv6)
[![Ansible Quality Score](https://img.shields.io/ansible/quality/42479)](https://galaxy.ansible.com/mehdicopter/ipv6)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Configure IPv6 for Linux systems.

## Requirements
Any Linux from Debian, Ubuntu or CentOS.

## Role Variables
```yaml
---
# Disable or enable IPv6
ipv6_enabled: false #false/true
```
## Example Playbook
    - hosts: servers
      become: true
      roles:
         - mehdicopter.ipv6

## Author Information
Mehdi MAHFOUDI aka Mehdicopter.
