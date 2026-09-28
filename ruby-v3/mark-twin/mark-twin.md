# mark-twin

**Tag**: serialization, template, filesystem

## 简介

twin helps keep two machines' configuration aligned.

A sync-file is just Markdown: the prose says why a path is synced, and
fenced YAML blocks define what to do. rsync does the copying.

When both sides changed since the last sync, twin shows a diff and asks
before overwriting. A target is a local path, a mounted volume, or
user@host:/path over ssh, and twin treats all three the same.

Interactive selection runs through fzf with a rendered Markdown preview; the
same sync-files drive scriptable status, dry-run and sync commands.

## 官网

- 主页: https://github.com/rhsev/mark-twin
- 文档: https://github.com/rhsev/mark-twin#readme
- 更新日志: https://github.com/rhsev/mark-twin/releases
- 问题追踪: https://github.com/rhsev/mark-twin/issues
- RubyGems: https://rubygems.org/gems/mark-twin

## 历史版本号

- 0.6.1 (2026-09-05)
- 0.6.0 (2026-08-30)
- 0.5.0 (2026-08-29)
- 0.4.3 (2026-08-08)
- 0.4.2 (2026-08-08)
- 0.4.1 (2026-08-02)
- 0.4.0 (2026-08-02)
- 0.3.0 (2026-07-28)
- 0.2.0 (2026-06-21)
- 0.1.3 (2026-06-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/mark-twin
- gem 安装: `gem install mark-twin`
- Bundler: `gem "mark-twin"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/mark-twin-0.6.1.gem
- 版本锁定: `gem "mark-twin", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
