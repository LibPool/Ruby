# arp-revolver

**Tag**: filesystem

## 简介

To switch mac address for static arp endpoint.

    This invokes arping command for health checking.
    If no responding for 3 times, it'll try to switch mac address for the target host,
    according to the config file /etc/arp-revolver/arp-revolver.yml.

    Before execute must to make sure that user is root,
    because changed the mac address is a root command.

## 官网

- 文档: https://www.rubydoc.info/gems/arp-revolver/0.1.7
- RubyGems: https://rubygems.org/gems/arp-revolver

## 历史版本号

- 0.1.7 (2020-11-24)
- 0.1.6 (2020-11-24)
- 0.1.5 (2020-11-24)
- 0.1.4 (2020-11-24)
- 0.1.3 (2020-11-24)
- 0.1.2 (2020-11-24)
- 0.1.1 (2020-11-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/arp-revolver
- gem 安装: `gem install arp-revolver`
- Bundler: `gem "arp-revolver"`
- 最新版本: 0.1.7
- 最新版归档: https://rubygems.org/downloads/arp-revolver-0.1.7.gem
- 版本锁定: `gem "arp-revolver", "~> 0.1.7"`
- 中央仓库: https://rubygems.org/
