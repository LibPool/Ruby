# n8-attr_encrypted

**Tag**: security

## 简介

Generates attr_accessors that encrypt and decrypt attributes transparently. A fork with a kludge to handle :if/:unless Procs with attr_encrypted that uses attributes that may have not been set yet before the original attr_encrypted does its thing. This basically just resaves all the encrypted_attributes in a before_save callback.

## 官网

- 主页: http://github.com/shuber/attr_encrypted
- RubyGems: https://rubygems.org/gems/n8-attr_encrypted

## 历史版本号

- 1.1.3 (2010-09-20)
- 1.1.2 (2010-09-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/n8-attr_encrypted
- gem 安装: `gem install n8-attr_encrypted`
- Bundler: `gem "n8-attr_encrypted"`
- 最新版本: 1.1.3
- 最新版归档: https://rubygems.org/downloads/n8-attr_encrypted-1.1.3.gem
- 版本锁定: `gem "n8-attr_encrypted", "~> 1.1.3"`
- 中央仓库: https://rubygems.org/
