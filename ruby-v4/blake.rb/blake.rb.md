# blake.rb

**Tag**: testing, security

## 简介

BLAKE is a cryptographic hash function based on Dan Bernstein's ChaCha stream cipher, but a permuted copy of the input block, XORed with round constants, is added before each ChaCha round. Like SHA-2, there are two variants differing in the word size. ChaCha operates on a 4×4 array of words. BLAKE repeatedly combines an 8-word hash value with 16 message words, truncating the ChaCha result to obtain the next hash value. BLAKE-256 and BLAKE-224 use 32-bit words and produce digest sizes of 256 bits and 224 bits, respectively, while BLAKE-512 and BLAKE-384 use 64-bit words and produce digest sizes of 512 bits and 384 bits, respectively.

## 官网

- 主页: https://github.com/ydakuka/blake.rb
- 问题追踪: https://github.com/ydakuka/blake.rb/issues
- RubyGems: https://rubygems.org/gems/blake.rb

## 历史版本号

- 0.0.2 (2020-02-22)
- 0.0.1 (2020-02-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/blake.rb
- gem 安装: `gem install blake.rb`
- Bundler: `gem "blake.rb"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/blake.rb-0.0.2.gem
- 版本锁定: `gem "blake.rb", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
