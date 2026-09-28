# ignorefile

**Tag**: web, networking, filesystem

## 简介

# Ignorefile
Compile a set of ignore statements from files and code.

## Usage

```ruby
reqire 'ignorefile'

cookbook_files = Dir.glob('**/{*,.*}')
ignore = IgnoreFile.new('.gitignore', 'chefignore', ['.git/*'])

ignore.apply!(cookbook_files)
```

## Thanks
This gem is based upon Seth Vargo's [buff-ignore](https://github.com/sethvargo/buff-ignore).

## 官网

- 主页: https://github.com/jmanero/ignorefile
- 文档: https://www.rubydoc.info/gems/ignorefile/1.1.0
- RubyGems: https://rubygems.org/gems/ignorefile

## 历史版本号

- 1.1.0 (2015-09-04)
- 1.0.0 (2015-05-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/ignorefile
- gem 安装: `gem install ignorefile`
- Bundler: `gem "ignorefile"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/ignorefile-1.1.0.gem
- 版本锁定: `gem "ignorefile", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
