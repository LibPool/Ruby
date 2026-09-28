# omnifocus-bugzilla

**Tag**: web, testing, serialization, networking, filesystem

## 简介

Plugin for omnifocus gem to provide bugzilla BTS synchronization.

The first time this runs it creates a yaml file in your home directory
for the bugzilla url, username, and queries.

The queries config is optional.  If it is not included bugzilla-omnifocus will
pull all active bugs assigned to the specified user.

To use a custom query or multiple queries you must include a queries parameter
in your config.

The queries config is an array of strings.  Each string is the query string
portion of the bugzilla search results url.  Its easiest to create your search
in bugzilla and then paste the portion of the url after the question mark into
the config file.

Example:

    ---
    bugzilla_url: http://bugs/buglist.cgi
    username: aja
    queries: ["bug_status=NEW", "bug_status=CLOSED"]

## 官网

- 主页: https://github.com/seattlerb/omnifocus-bugzilla
- 文档: https://www.rubydoc.info/gems/omnifocus-bugzilla/1.1.4
- RubyGems: https://rubygems.org/gems/omnifocus-bugzilla

## 历史版本号

- 1.1.4 (2015-05-08)
- 1.1.2 (2011-07-20)
- 1.1.1 (2010-12-15)
- 1.1.0 (2009-09-30)
- 1.0.0 (2009-08-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/omnifocus-bugzilla
- gem 安装: `gem install omnifocus-bugzilla`
- Bundler: `gem "omnifocus-bugzilla"`
- 最新版本: 1.1.4
- 最新版归档: https://rubygems.org/downloads/omnifocus-bugzilla-1.1.4.gem
- 版本锁定: `gem "omnifocus-bugzilla", "~> 1.1.4"`
- 中央仓库: https://rubygems.org/
