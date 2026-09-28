# rkseal

**Tag**: cli, security, devops

## 简介

rkseal wraps the kubeseal CLI to author and edit Kubernetes SealedSecrets.
The plaintext Secret manifest is edited in $EDITOR on a RAM-backed buffer
that never touches persistent disk, then sealed with the controller's public key.
Deploys to the cluster are explicit opt-in only and guarded by the active kube context.

## 官网

- 主页: https://github.com/pwojcieszonek/rkseal
- RubyGems: https://rubygems.org/gems/rkseal

## 历史版本号

- 0.1.1 (2026-06-27)
- 0.1.0 (2026-06-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/rkseal
- gem 安装: `gem install rkseal`
- Bundler: `gem "rkseal"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/rkseal-0.1.1.gem
- 版本锁定: `gem "rkseal", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
