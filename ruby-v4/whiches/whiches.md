# whiches

**Tag**: database, filesystem

## 简介

Cross-platform way of finding executables in all the paths in $PATH.
    
    This is similar to the Unix 'which' command, however, instead of finding the first
    occurence of the executable in $PATH, it finds all occurences in $PATH.
    This could be useful if you installed something that modified your PATH and now you're
    executing a different version but can't figure out what happened.
    Example:
    On OS X, OpenSSL is installed in /usr/bin/openssl
      % which openssl
      ==> /usr/bin/openssl
    After installing PostgreSQL:
      % which openssl
      ==> /Applications/Postgres.app/Contents/MacOS/bin/openssl
    If you're trying to diagnose what happened, you can use:
      % whiches openssl
      ==>
      [
          [0] "/Applications/Postgres.app/Contents/MacOS/bin/openssl",
          [1] "/usr/bin/openssl"
      ]  
    This will show you that the first one that is found in the PATH is the one from Postgres,
    so if you want to get back your original one, you have to modify your PATH accordingly.

## 官网

- 主页: https://github.com/simplytech/whiches
- 文档: https://www.rubydoc.info/gems/whiches/0.0.2
- RubyGems: https://rubygems.org/gems/whiches

## 历史版本号

- 0.0.2 (2013-07-11)
- 0.0.1 (2013-07-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/whiches
- gem 安装: `gem install whiches`
- Bundler: `gem "whiches"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/whiches-0.0.2.gem
- 版本锁定: `gem "whiches", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
