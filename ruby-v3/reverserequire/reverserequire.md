# reverserequire

**Tag**: testing, filesystem

## 简介

reverse_require requires specific files from the gems which depend on a certain RubyGem and contain the specified path. Using reverse_require one can allow others to easily extend the functionality of a RubyGem. Simply add reverse_require into the code of your RubyGem:  reverse_require 'my_gem', 'some/path'  Then other gems which depend upon +my_gem+ merely have to provide &lt;tt&gt;some/path&lt;/tt&gt; within their &lt;tt&gt;lib/&lt;/tt&gt; directory, and reverse_require will load them all at run-time. This ability makes designing plug-in systems for a RubyGem trivial.

## 官网

- 主页: http://rubyforge.org/projects/reverserequire/
- RubyGems: https://rubygems.org/gems/reverserequire

## 历史版本号

- 0.0.9 (2009-07-25)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/reverserequire
- gem 安装: `gem install reverserequire`
- Bundler: `gem "reverserequire"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/reverserequire-0.1.0.gem
- 版本锁定: `gem "reverserequire", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
