# with_reverse_lookup

**Tag**: library

## 简介

Provides a simple modification to existing hashes to provide key lookup
    by value in addition to value lookup by key.
    
    For example:
    
    TABLE = { :key => 1 }.extend(WithReverseLookup)
    
    TABLE[:key] #=> 1
    TABLE[1]    #=> :key
    
    This is mostly useful for lookup tables.

## 官网

- 主页: http://github.com/mtodd/with_reverse_lookup
- RubyGems: https://rubygems.org/gems/with_reverse_lookup

## 历史版本号

- 0.0.1 (2010-09-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/with_reverse_lookup
- gem 安装: `gem install with_reverse_lookup`
- Bundler: `gem "with_reverse_lookup"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/with_reverse_lookup-0.0.1.gem
- 版本锁定: `gem "with_reverse_lookup", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
