# string-encrypt

**Tag**: web, testing, security, networking, filesystem

## 简介

String open classed with AES-256 and RSA encryption and zipping methods for easy, secure, encryption of strings.

The string_encryption gem was started with the intention of being
compatible with the RSA and AES algorithms used in a javascript
library on http://www.pidder.com/pidcrypt .  Usage and testing
against the pidcrypt library hasn't been done yet, but is scheduled
for the future.
The intent of this library is to make encryption and decryption of a 
string as straight forward as capitalizing or reversing is.

To encrypt a string:  
    encrypted_secret = &quot;Super Secret Text&quot;.encrypt(&quot;Super Secret Password&quot;)
To decrypt a string:
    decrypted_secret = encrypted_secret.encrypt(&quot;Super Secret Password&quot;)



Branden Giacoletto

## 官网

- 主页: http://string-encrypt.rubyforge.com
- RubyGems: https://rubygems.org/gems/string-encrypt

## 历史版本号

- 0.0.5 (2009-07-25)
- 0.0.4 (2009-07-25)
- 0.0.3 (2009-07-25)
- 0.0.2 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/string-encrypt
- gem 安装: `gem install string-encrypt`
- Bundler: `gem "string-encrypt"`
- 最新版本: 0.0.5
- 最新版归档: https://rubygems.org/downloads/string-encrypt-0.0.5.gem
- 版本锁定: `gem "string-encrypt", "~> 0.0.5"`
- 中央仓库: https://rubygems.org/
