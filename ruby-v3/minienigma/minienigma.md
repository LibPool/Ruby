# minienigma

**Tag**: web, security, networking, data

## 简介

Minienigma it's a simple to use string encrypting/decrypting machine out of the box.
It uses a AES 256 CBC algorithm which makes your data pretty secure this days.
In order to use it, make sure to configure it using MiniEnigma.configure(key, iv)
where key and iv needs to be a combination of characters.  Key must be 32 characters long.  
Iv must be 16 characters long.
Then to encrypt just call MiniEnigma.encrypt('your insecure data here').
To decrypt MiniEnigma.decrypt('your secure data here').
PD: A nice place to get secure key and iv: http://randomkeygen.com

## 官网

- 主页: http://rubygems.org/gems/minienigma
- 源码仓库: https://github.com/esteban8a/minienigma
- RubyGems: https://rubygems.org/gems/minienigma

## 历史版本号

- 0.1.0 (2014-02-13)
- 0.0.8 (2014-02-12)
- 0.0.7 (2014-02-12)
- 0.0.6 (2014-02-12)
- 0.0.5 (2014-02-12)
- 0.0.4 (2014-02-12)
- 0.0.3 (2014-02-12)
- 0.0.2 (2014-02-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/minienigma
- gem 安装: `gem install minienigma`
- Bundler: `gem "minienigma"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/minienigma-0.1.0.gem
- 版本锁定: `gem "minienigma", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
