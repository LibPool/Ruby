# rhubarbcipher

**Tag**: testing, security, filesystem, data

## 简介

WARNING: Please be aware that this gem has not undergone any form of independent security evaluation and is provided for academic/educational purposes only. RHUBARBCIPHER should not be used to encrypt any data with high confidentiality, availability or integrity requirements, and should be treated purely as a proof of concept and/or learning exercise. RHUBARBCIPHER is an experimental multi-key file encryption/decryption system for GNU/Linux and BSD that combines one-time pad encryption/decryption with Shamir's Secret Sharing in an attempt to encrypt files in a versatile yet information-theoretically secure manner. RHUBARBCIPHER only works well on smaller files (e.g. less than 15000KiB) due to the time taken to encrypt/decrypt data, which increases as a function of file size. It includes an optional decoy feature which allows users to specify a decoy file and generate a set of decoy keys in addition to the real keys. Size similarity between the decoy file and the real file is strictly enforced.

## 官网

- 主页: https://github.com/octetsplicer/RHUBARBCIPHER
- 文档: https://www.rubydoc.info/gems/rhubarbcipher/0.2.5
- RubyGems: https://rubygems.org/gems/rhubarbcipher

## 历史版本号

- 0.2.5 (2024-08-02)
- 0.2.4 (2020-06-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/rhubarbcipher
- gem 安装: `gem install rhubarbcipher`
- Bundler: `gem "rhubarbcipher"`
- 最新版本: 0.2.5
- 最新版归档: https://rubygems.org/downloads/rhubarbcipher-0.2.5.gem
- 版本锁定: `gem "rhubarbcipher", "~> 0.2.5"`
- 中央仓库: https://rubygems.org/
