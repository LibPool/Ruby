# minitest-distributed

**Tag**: database, testing

## 简介

minitest-distributed is a plugin for minitest for executing tests on a
distributed set of unreliable workers.

When a test suite grows large enough, it inevitable gets too slow to run
on a single machine to give timely feedback to developers. This plugins
combats this issue by distributing the full test suite to a set of workers.
Every worker is a consuming from a single queue, so the tests get evenly
distributed and all workers will finish around the same time. Redis is used
as coordinator, but when using this plugin without having access to Redis,
it will use an in-memory coordinator.

Using multiple (virtual) machines for a test run is an (additional) source
of flakiness. To combat flakiness, minitest-distributed implements resiliency
patterns, like re-running a test on a different worker on failure, and
a circuit breaker for misbehaving workers.

## 官网

- 主页: https://github.com/Shopify/minitest-distributed
- RubyGems: https://rubygems.org/gems/minitest-distributed

## 历史版本号

- 0.3.0 (2026-09-22)
- 0.2.13 (2026-06-02)
- 0.2.12 (2026-01-20)
- 0.2.11 (2024-09-16)
- 0.2.10 (2023-08-18)
- 0.2.9 (2023-01-16)
- 0.2.8 (2023-01-04)
- 0.2.7 (2022-09-12)
- 0.2.6 (2022-08-23)
- 0.2.5 (2022-03-21)
- 0.2.2 (2022-03-21)
- 0.2.4 (2021-04-06)
- 0.2.3 (2020-08-06)
- 0.2.1 (2020-07-26)
- 0.2.0 (2020-07-21)
- 0.1.2 (2020-06-18)
- 0.1.1 (2020-06-17)
- 0.1.0 (2020-06-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/minitest-distributed
- gem 安装: `gem install minitest-distributed`
- Bundler: `gem "minitest-distributed"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/minitest-distributed-0.3.0.gem
- 版本锁定: `gem "minitest-distributed", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
