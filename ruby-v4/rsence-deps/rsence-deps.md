# rsence-deps

**Tag**: web, database, testing, networking

## 简介

This is an empty gem specifying a list of dependencies for RSence

Additionally, you may want to install these gems also, even though
they are tested for and auto-installation in tried:
 - sqlite3
 - rmagick

You must install a Javascript runtime engine separately, because
RubyGems isn't smart enough to allow conditional dependencies.

The V8-based NodeJS is recommended: http://nodejs.org/

If you are on OS X, you already have Apple's JavaScriptCore
installed, which is fine.

Previously, RSence depended on therubyracer, but it was found
to be the the culprit for crashing the Ruby VM and the cause
of some other random memory corruption issues, so it's not
recommended until its maintainers have sorted it out.
You may however proceed to use it on your own risk, if the
speed gains are worth the instability.

More info: http://rsence.org/

## 官网

- 主页: http://rsence.org/
- RubyGems: https://rubygems.org/gems/rsence-deps

## 历史版本号

- 971 (2012-04-28)
- 970 (2012-04-28)
- 969 (2012-04-27)
- 968 (2012-04-23)
- 967 (2012-03-29)
- 966 (2011-12-04)
- 965 (2011-11-30)
- 964 (2011-07-26)
- 963 (2011-01-03)
- 958 (2010-05-25)
- 957 (2010-05-10)
- 956 (2010-05-08)
- 934 (2010-02-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/rsence-deps
- gem 安装: `gem install rsence-deps`
- Bundler: `gem "rsence-deps"`
- 最新版本: 971
- 最新版归档: https://rubygems.org/downloads/rsence-deps-971.gem
- 版本锁定: `gem "rsence-deps", "~> 971"`
- 中央仓库: https://rubygems.org/
