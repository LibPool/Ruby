# sync_enum

**Tag**: serialization

## 简介

Iterate over multiple enumerators in parallel, using the external
interface based on the #next method. Each call to #next returns an
array, containing the next element for each of the enumerators. A
StopIteration exception is raised as soon as any of the enumerators
runs out of elements.

SyncEnum differs from the standard library's REXML::SyncEnumerator in
its use of the #next external iterator interface, while
REXML::SyncEnumerator uses an #each internal iterator interface. The
external interface is more convenient when you expect to end
iteration before reaching the end of any of the enumerations,
including cases where an enumerator generates an unending sequence.

## 官网

- 主页: https://github.com/brucetesar/sync_enum
- 更新日志: https://github.com/brucetesar/sync_enum/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/sync_enum

## 历史版本号

- 0.1.11 (2026-08-18)
- 0.1.10 (2026-04-10)
- 0.1.9 (2026-04-02)
- 0.1.8 (2026-04-01)
- 0.1.7 (2025-10-14)
- 0.1.1 (2021-05-17)
- 0.1.0 (2021-05-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/sync_enum
- gem 安装: `gem install sync_enum`
- Bundler: `gem "sync_enum"`
- 最新版本: 0.1.11
- 最新版归档: https://rubygems.org/downloads/sync_enum-0.1.11.gem
- 版本锁定: `gem "sync_enum", "~> 0.1.11"`
- 中央仓库: https://rubygems.org/
