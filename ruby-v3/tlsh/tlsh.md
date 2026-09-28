# tlsh

**Tag**: filesystem

## 简介

tlsh is a fuzzy matching library, which hashes can be used for similarity comparison.
Given a byte stream with a minimum length of 256 bytes, TLSH generates a hash value
which can be used for similarity comparisons. Similar objects will have similar hash
values which allow for the detection of similar objects by comparing their hash values.

The computed hash is 35 bytes long (output as 70 hexadecimal characters).
The first 3 bytes are used to capture the information about the file as a whole (length, ...),
while the last 32 bytes are used to capture information about incremental parts of the file.

## 官网

- 主页: https://github.com/adamliesko/tlsh
- 文档: https://www.rubydoc.info/gems/tlsh/0.1.3
- RubyGems: https://rubygems.org/gems/tlsh

## 历史版本号

- 0.1.3 (2017-08-18)
- 0.1.1 (2017-08-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/tlsh
- gem 安装: `gem install tlsh`
- Bundler: `gem "tlsh"`
- 最新版本: 0.1.3
- 最新版归档: https://rubygems.org/downloads/tlsh-0.1.3.gem
- 版本锁定: `gem "tlsh", "~> 0.1.3"`
- 中央仓库: https://rubygems.org/
