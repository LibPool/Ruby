# sym-crypt

**Tag**: security, serialization, data

## 简介

sym-crypt is a core encryption module for the symmetric encryption app 
(and a corresponding gem) "sym", and contains the main base serialization, 
encryption, encoding, compression routines.

sym-crypt uses a symmetric 256-bit key with the AES-256-CBC cipher, which is the 
same cipher as the one used by the US Government. For encyption with a 
password sym-crypt uses AES-128-CBC cipher. 

The resulting data is zlib-compressed and base64-encoded. The keys are also 
base64 encoded for easy copying/pasting/etc.

## 官网

- 主页: https://github.com/kigster/sym-crypt
- 文档: https://www.rubydoc.info/gems/sym-crypt/1.2.0
- RubyGems: https://rubygems.org/gems/sym-crypt

## 历史版本号

- 1.2.0 (2019-05-10)
- 1.1.1 (2017-10-25)
- 1.0.0 (2017-07-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/sym-crypt
- gem 安装: `gem install sym-crypt`
- Bundler: `gem "sym-crypt"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/sym-crypt-1.2.0.gem
- 版本锁定: `gem "sym-crypt", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
