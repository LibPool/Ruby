# togglefleet

**Tag**: web, networking, filesystem, data

## 简介

ToggleFleet is a hosted feature-flag service for Ruby. This gem fetches your environment's
flags once, refreshes them in the background with conditional ETag requests, and evaluates
all five gates — boolean, actor, group, percentage-of-actors (sticky), and percentage-of-time
— entirely in-process. Checking a flag is a hash lookup, not a network call, so flags cost
nothing on the hot path and keep working at their last known values if ToggleFleet is
unreachable.

Zero runtime dependencies — only the Ruby standard library. Thread-safe, fork-safe under
Puma/Unicorn/Passenger, and fail-safe by design: any error returns your configured default
rather than raising into a request.

Evaluation is byte-identical to server-side evaluation, including MD5 bucketing, so a sticky
rollout targets exactly the same actors whether it is resolved locally or through the API.
Group membership is decided by predicates in your own code, so no user data leaves your process.

Requires a ToggleFleet account for an SDK key. Full documentation at https://togglefleet.com/docs.

## 官网

- 主页: https://togglefleet.com
- 源码仓库: https://github.com/takeaseatventure/togglefleet-ruby
- 文档: https://togglefleet.com/docs
- 更新日志: https://github.com/takeaseatventure/togglefleet-ruby/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/takeaseatventure/togglefleet-ruby/issues
- RubyGems: https://rubygems.org/gems/togglefleet

## 历史版本号

- 0.2.1 (2026-07-26)
- 0.2.0 (2026-07-26)
- 0.1.0 (2026-06-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/togglefleet
- gem 安装: `gem install togglefleet`
- Bundler: `gem "togglefleet"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/togglefleet-0.2.1.gem
- 版本锁定: `gem "togglefleet", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
