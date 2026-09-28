# safe_memoize

**Tag**: testing, tooling

## 简介

SafeMemoize is a production-ready, zero-dependency memoization library for Ruby. It uses Ruby's prepend mechanism to wrap methods with a thread-safe cache (Mutex + double-check locking) that correctly handles nil and false return values — fixing the silent bug in the common ||= pattern. Results are cached per unique argument combination, so parameterized methods only compute each variant once. Additional features include TTL expiration, LRU cache size limiting, conditional caching via if:/unless: predicates, lifecycle hooks for hit/eviction/expiration events, per-instance metrics (hit rate, miss rate, computation time), targeted cache invalidation, custom cache key generators, and introspection helpers. Method visibility (public, protected, private) is fully preserved.

## 官网

- 主页: https://github.com/eclectic-coding/safe_memoize
- 源码仓库: https://github.com/eclectic-coding/safe_memoize/tree/main
- 更新日志: https://github.com/eclectic-coding/safe_memoize/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/safe_memoize

## 历史版本号

- 1.7.0 (2026-06-02)
- 1.6.0 (2026-06-02)
- 1.5.0 (2026-06-02)
- 1.4.0 (2026-06-02)
- 1.3.0 (2026-05-28)
- 1.2.0 (2026-05-27)
- 1.1.0 (2026-05-22)
- 1.0.0 (2026-05-22)
- 0.9.0 (2026-05-22)
- 0.8.0 (2026-05-22)
- 0.7.0 (2026-05-18)
- 0.6.3 (2026-05-18)
- 0.6.2 (2026-05-18)
- 0.6.1 (2026-05-17)
- 0.6.0 (2026-05-17)
- 0.5.0 (2026-05-17)
- 0.4.0 (2026-05-17)
- 0.3.0 (2026-05-15)
- 0.2.0 (2026-05-14)
- 0.1.2 (2026-05-13)
- 0.1.0 (2026-02-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/safe_memoize
- gem 安装: `gem install safe_memoize`
- Bundler: `gem "safe_memoize"`
- 最新版本: 1.7.0
- 最新版归档: https://rubygems.org/downloads/safe_memoize-1.7.0.gem
- 版本锁定: `gem "safe_memoize", "~> 1.7.0"`
- 中央仓库: https://rubygems.org/
