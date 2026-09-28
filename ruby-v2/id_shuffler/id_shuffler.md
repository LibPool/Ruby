# id_shuffler

**Tag**: database, testing, security, data

## 简介

An efficient solution to use when it is undesirable to expose internal database
ids, IdShuffler converts integers like 123 into strings like 'q34nr1', and
vice-versa, using a very lightweight integer scrambling algorithm plus
'Crockford 32' encoding. It is built as a native C extension and so is very
fast. The algorithm takes a string key as a seed, so you can use different
keys for different id spaces and thus obtain different slugs for the same
initial integer. This is not a security solution and I am not a cryptographer;
it should be assumed a determined individual can unshuffle the ids without
knowing the key used to generate them. Also note these are 30-bit ids, so the
library can only represent values up to approximately 1 billion
(1,073,741,823).

This gem is still under development in so far as I have not written tests or
documentation for it.

## 官网

- 主页: http://rubygems.org/gems/id_shuffler
- 文档: https://www.rubydoc.info/gems/id_shuffler/0.0.8
- RubyGems: https://rubygems.org/gems/id_shuffler

## 历史版本号

- 0.0.8 (2013-06-12)
- 0.0.6 (2013-06-07)
- 0.0.5 (2013-06-07)
- 0.0.4 (2013-06-07)
- 0.0.3 (2013-04-02)
- 0.0.2 (2013-03-27)
- 0.0.1 (2013-03-26)
- 0.0.0 (2013-03-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/id_shuffler
- gem 安装: `gem install id_shuffler`
- Bundler: `gem "id_shuffler"`
- 最新版本: 0.0.8
- 最新版归档: https://rubygems.org/downloads/id_shuffler-0.0.8.gem
- 版本锁定: `gem "id_shuffler", "~> 0.0.8"`
- 中央仓库: https://rubygems.org/
