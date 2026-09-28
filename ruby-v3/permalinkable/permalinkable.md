# permalinkable

**Tag**: database, security, data

## 简介

This is a gem originated from another gem called permalink.
    Since I often want a permalink that provides no way to tell the database ids,
    I came up with the idea about encrypting the id and prepending it to the permalink.
    For more information about FPE(Format Preserving Encryption), please consult the wikipedia.

    The encryption method of current release is simply RC4-40 with a configurable key.
    Note, RC4-40 is not a strong encryption algorithm at all, and you shouldn't rely on it to delivery sensitive
    information. Also, to prevent inconsistance of encryption, and duplication(although the chance is very low)
    you should keep your key as a secret and never change it.

    The original implementation of generating permalink involves a infite loop to check uniqueness in database.
    It's slow, inefficient and most importantly, it still can't prevent race condition. And since we are using
    a FPE algorithm on the database id, which is garanteed to be unique from database, we don't need to put ourselves
    in that inefficient loop.

    Finally, what's the purpose of this gem?
    It's only a gem that helps hiding your database ids.

## 官网

- 主页: http://rubygems.org/gems/permalinkable
- 源码仓库: https://github.com/yangou/permalinkable
- 文档: https://www.rubydoc.info/gems/permalinkable/1.0.1
- RubyGems: https://rubygems.org/gems/permalinkable

## 历史版本号

- 1.0.1 (2014-08-30)
- 0.1.0 (2014-08-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/permalinkable
- gem 安装: `gem install permalinkable`
- Bundler: `gem "permalinkable"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/permalinkable-1.0.1.gem
- 版本锁定: `gem "permalinkable", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
