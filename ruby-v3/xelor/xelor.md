# xelor

**Tag**: library

## 简介

Xelor was built for systems that require random bytes for processes faster than one second. Because normal random generation is based off of time as a seed, if there exists multiple calls towards SecureRandom or Rand within one second, the same number will be produced. This can be resolved on unix or linux based systems by making a system call to read /dev/urandom.

## 官网

- 主页: http://avecchio.github.io
- 文档: https://www.rubydoc.info/gems/xelor/0.1.5
- RubyGems: https://rubygems.org/gems/xelor

## 历史版本号

- 0.1.5 (2016-06-21)
- 0.1.3 (2016-06-21)
- 0.1.2 (2016-06-21)
- 0.1.1 (2016-06-21)
- 0.1.0 (2016-06-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/xelor
- gem 安装: `gem install xelor`
- Bundler: `gem "xelor"`
- 最新版本: 0.1.5
- 最新版归档: https://rubygems.org/downloads/xelor-0.1.5.gem
- 版本锁定: `gem "xelor", "~> 0.1.5"`
- 中央仓库: https://rubygems.org/
