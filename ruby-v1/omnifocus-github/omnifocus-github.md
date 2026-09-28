# omnifocus-github

**Tag**: web, testing, security, networking

## 简介

Plugin for omnifocus gem to provide github BTS synchronization.

Support for Github Enterprise:

In your git config, set the key github.accounts to a space
separated list of github accounts.

    git config --global github.accounts "github myghe"

For each account API and web end points and authentication information
should be stored in the git config under a key matching the
account. For example:

    git config --global github.user me
    git config --global github.password mypassword
    git config --global myghe.api https://ghe.mydomain.com/api/v3
    git config --global myghe.api https://ghe.mydomain.com/

For each account can you specify the following parameters:

* api - specify an API endpoint other than
  https://api.github.com. This is so you can point this at your Github
  Enterprise endpoint.

* web - specify an API endpoint other than https://www.github.com. This
  is so you can point this at your Github Enterprise endpoint

* user, password - A username and password pair for Basic http authentication.

## 官网

- 主页: https://github.com/seattlerb/omnifocus-github
- RubyGems: https://rubygems.org/gems/omnifocus-github

## 历史版本号

- 2.0.0 (2022-09-28)
- 1.9.0 (2020-02-13)
- 1.8.3 (2019-12-16)
- 1.8.2 (2015-08-10)
- 1.8.1 (2015-04-13)
- 1.8.0 (2014-11-11)
- 1.7.1 (2014-01-22)
- 1.7.0 (2013-12-05)
- 1.6.0 (2013-07-24)
- 1.5.0 (2013-05-10)
- 1.4.1 (2013-04-09)
- 1.4.0 (2012-11-23)
- 1.3.0 (2011-11-19)
- 1.2.0 (2011-08-27)
- 1.1.0 (2011-08-12)
- 1.0.1 (2011-07-17)
- 1.0.0 (2009-08-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/omnifocus-github
- gem 安装: `gem install omnifocus-github`
- Bundler: `gem "omnifocus-github"`
- 最新版本: 2.0.0
- 最新版归档: https://rubygems.org/downloads/omnifocus-github-2.0.0.gem
- 版本锁定: `gem "omnifocus-github", "~> 2.0.0"`
- 中央仓库: https://rubygems.org/
