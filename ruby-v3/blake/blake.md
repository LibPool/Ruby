# blake

**Tag**: testing, security

## 简介

BLAKE is a cryptographic hash function based on Dan Bernstein's ChaCha stream cipher, but a permuted copy of the input block, XORed with round constants, is added before each ChaCha round. Like SHA-2, there are two variants differing in the word size. ChaCha operates on a 4×4 array of words. BLAKE repeatedly combines an 8-word hash value with 16 message words, truncating the ChaCha result to obtain the next hash value. BLAKE-256 and BLAKE-224 use 32-bit words and produce digest sizes of 256 bits and 224 bits, respectively, while BLAKE-512 and BLAKE-384 use 64-bit words and produce digest sizes of 512 bits and 384 bits, respectively.

## 官网

- 主页: https://github.com/ydakuka/blake
- 问题追踪: https://github.com/ydakuka/blake/issues
- RubyGems: https://rubygems.org/gems/blake

## 历史版本号

- 0.0.4 (2020-03-21)
- 0.0.3 (2020-03-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/blake
- gem 安装: `gem install blake`
- Bundler: `gem "blake"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/blake-0.0.4.gem
- 版本锁定: `gem "blake", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
