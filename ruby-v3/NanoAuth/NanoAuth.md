# NanoAuth

**Tag**: web, security, filesystem

## 简介

NanoAuth is a super stripped down Rails authentication module. It's comprised (so far) of one file that provides some additional methods to be mixed in to your User model. Over the years I kept tweaking code in various projects and continued to see the same boiler plate code for:

  * authentication a user via User.authenticate(email,password)
  * encrypt(password)
  * authenticated?(password)

 \ So I decided on some down time to pull all this stuff out and make a nice little gem of it.

## 官网

- 主页: https://github.com/jasonbits/nano_auth/blob/master
- RubyGems: https://rubygems.org/gems/NanoAuth

## 历史版本号

- 0.1.0 (2011-11-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/NanoAuth
- gem 安装: `gem install NanoAuth`
- Bundler: `gem "NanoAuth"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/NanoAuth-0.1.0.gem
- 版本锁定: `gem "NanoAuth", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
