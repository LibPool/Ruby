# generic_auth

**Tag**: testing, security, filesystem

## 简介

This gem works on the most basic ruby classes. Its only dependency is activesupport for some
                     string and inflector functionality.  GenericAuth is very easy to use, simply create a rules file and your class methods
                     are automatically wrapped to invoke authorization methods before they are run.  You must set the user which must
                     respond to a roles method.  Your authorized classes must also specify which methods should be authorized (generic_auth_on method) 
                     as an array of symbols (see specs).  Other than that, its automatic

## 官网

- 主页: https://github.com/chrismcleod/generic_auth
- RubyGems: https://rubygems.org/gems/generic_auth

## 历史版本号

- 0.1.4 (2012-08-20)
- 0.1.1 (2012-08-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/generic_auth
- gem 安装: `gem install generic_auth`
- Bundler: `gem "generic_auth"`
- 最新版本: 0.1.4
- 最新版归档: https://rubygems.org/downloads/generic_auth-0.1.4.gem
- 版本锁定: `gem "generic_auth", "~> 0.1.4"`
- 中央仓库: https://rubygems.org/
