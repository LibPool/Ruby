# diru

**Tag**: web, cli

## 简介

Diru is a Change Directory (cd) utility for
augmenting Unix Shell functionality. Diru makes it easy and efficient
to jump around in Project's directories. Diru uses client/server
architecture, which enables sharing of directory info and state
between terminal sessions.

Each Server serves one Project, which is a tree of related directories
where user wants to jump around and which has a logical root. There
can be multiple Servers, if user needs to access multiple Projects
concurrently.

Client queries directory info from Server and directory change is
pushed to Shell in order to change the current directory within the
Shell.

## 官网

- 文档: https://www.rubydoc.info/gems/diru/0.1.4
- RubyGems: https://rubygems.org/gems/diru

## 历史版本号

- 0.1.4 (2020-01-26)
- 0.1.3 (2020-01-26)
- 0.1.2 (2019-11-14)
- 0.1.1 (2019-07-24)
- 0.1.0 (2019-07-16)
- 0.0.8 (2017-12-08)
- 0.0.7 (2017-09-14)
- 0.0.6 (2017-08-27)
- 0.0.5 (2017-08-14)
- 0.0.4 (2017-07-26)
- 0.0.3 (2017-07-17)
- 0.0.2 (2017-07-16)
- 0.0.1 (2017-07-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/diru
- gem 安装: `gem install diru`
- Bundler: `gem "diru"`
- 最新版本: 0.1.4
- 最新版归档: https://rubygems.org/downloads/diru-0.1.4.gem
- 版本锁定: `gem "diru", "~> 0.1.4"`
- 中央仓库: https://rubygems.org/
