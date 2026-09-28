# reverse-require

**Tag**: testing, filesystem

## 简介

reverse-require allows one to require files that ends with a specified path from other RubyGems.  For instance, if one wanted to require the file 'mylibrary/extensions.rb' from all RubyGems:  require 'reverse_require'  require_all 'mylibrary/extensions' # =&gt; true  One can also require 'mylibrary/extensions.rb' only from RubyGems that depend on the currently loaded version of the mylibrary Gem:  require_for 'mylibrary', 'mylibrary/extensions' # =&gt; true

## 官网

- 主页: http://reverserequire.rubyforge.org/
- RubyGems: https://rubygems.org/gems/reverse-require

## 历史版本号

- 0.3.1 (2009-07-25)
- 0.3.0 (2009-07-25)
- 0.2.0 (2009-07-25)
- 0.1.2 (2009-07-25)
- 0.1.1 (2009-07-25)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/reverse-require
- gem 安装: `gem install reverse-require`
- Bundler: `gem "reverse-require"`
- 最新版本: 0.3.1
- 最新版归档: https://rubygems.org/downloads/reverse-require-0.3.1.gem
- 版本锁定: `gem "reverse-require", "~> 0.3.1"`
- 中央仓库: https://rubygems.org/
