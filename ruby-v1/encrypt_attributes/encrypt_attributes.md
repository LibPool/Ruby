# encrypt_attributes

**Tag**: database, testing, security, data

## 简介

This gem provides a dead-simple encryption of string / text attributes of ActiveRecord and Mongoid models. Encryptor internally uses ActiveSupport::MessageEncryptor and therefore it uses 'aes-256-cbc' cipher by default. Gem does NOT require column with different name. From user perspective encryption is completely transparent - they use decrypted values all the time, but encrypted values are stored in database.

## 官网

- 主页: https://github.com/aenain/encrypted_attributes
- 文档: https://www.rubydoc.info/gems/encrypt_attributes/0.0.1
- RubyGems: https://rubygems.org/gems/encrypt_attributes

## 历史版本号

- 0.0.1 (2014-06-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/encrypt_attributes
- gem 安装: `gem install encrypt_attributes`
- Bundler: `gem "encrypt_attributes"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/encrypt_attributes-0.0.1.gem
- 版本锁定: `gem "encrypt_attributes", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
