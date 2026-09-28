# knife-proxmox-ve

**Tag**: web, security, networking, template, devops

## 简介

Extends knife with `knife proxmox vm create` to create a new VM on Proxmox VE and
`knife proxmox vm bootstrap` to create it and automatically bootstrap it with
Chef/CINC in a single command — cloning a prepared template, configuring
CPU/RAM/network/cloud-init, starting the VM and waiting for it to boot before
running the node bootstrap. Adds read-only `cluster list`, `template list` and
`vm list` helpers. Supports multiple Proxmox clusters defined in ~/.cinc/config.rb
and authenticates with Proxmox VE API tokens.

## 官网

- 主页: https://github.com/pwojcieszonek/knife-proxmox-ve
- 文档: https://www.rubydoc.info/gems/knife-proxmox-ve/0.1.5
- RubyGems: https://rubygems.org/gems/knife-proxmox-ve

## 历史版本号

- 0.1.5 (2026-07-25)
- 0.1.4 (2026-06-09)
- 0.1.3 (2026-06-06)
- 0.1.2 (2026-06-06)
- 0.1.1 (2026-06-04)
- 0.1.0 (2026-06-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/knife-proxmox-ve
- gem 安装: `gem install knife-proxmox-ve`
- Bundler: `gem "knife-proxmox-ve"`
- 最新版本: 0.1.5
- 最新版归档: https://rubygems.org/downloads/knife-proxmox-ve-0.1.5.gem
- 版本锁定: `gem "knife-proxmox-ve", "~> 0.1.5"`
- 中央仓库: https://rubygems.org/
