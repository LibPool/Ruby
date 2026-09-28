# rack-dedos

**Tag**: web

## 简介

Somewhat more radical filters designed to decimate malicious requests during
a denial-of-service (DoS) attack by chopping their connection well before
your Rack app wastes any significant resources on them – ouch!

The filters have been proven to work against certain DoS attacks, however,
they might also block IPs behind proxies or VPNs. Make sure you have
understood how the filters are triggered and consider this middleware a last
resort only to be enabled during an attack.

## 官网

- 主页: https://github.com/svoop/rack-dedos
- 文档: https://www.rubydoc.info/gems/rack-dedos
- 更新日志: https://github.com/svoop/rack-dedos/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/svoop/rack-dedos/issues
- RubyGems: https://rubygems.org/gems/rack-dedos

## 历史版本号

- 0.7.3 (2026-06-26)
- 0.7.2 (2026-06-26)
- 0.7.1 (2026-04-21)
- 0.7.0 (2026-03-11)
- 0.5.1 (2026-01-08)
- 0.5.0 (2026-01-06)
- 0.4.2 (2025-12-01)
- 0.4.1 (2025-11-04)
- 0.4.0 (2025-07-21)
- 0.3.2 (2025-01-16)
- 0.2.2 (2024-12-25)
- 0.2.1 (2024-11-20)
- 0.2.0 (2023-05-16)
- 0.1.0 (2023-02-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack-dedos
- gem 安装: `gem install rack-dedos`
- Bundler: `gem "rack-dedos"`
- 最新版本: 0.7.3
- 最新版归档: https://rubygems.org/downloads/rack-dedos-0.7.3.gem
- 版本锁定: `gem "rack-dedos", "~> 0.7.3"`
- 中央仓库: https://rubygems.org/
