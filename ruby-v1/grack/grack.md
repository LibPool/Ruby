# grack

**Tag**: web, testing, networking

## 简介

This project aims to replace the builtin git-http-backend CGI handler
distributed with C Git with a Rack application. By default, Grack uses calls to
git on the system to implement Smart HTTP. Since the git-http-backend is really
just a simple wrapper for the upload-pack and receive-pack processes with the
'--stateless-rpc' option, this does not actually re-implement very much.
However, it is possible to use a different backend by specifying a different
Adapter.

## 官网

- 主页: https://github.com/grackorg/grack
- 文档: https://www.rubydoc.info/gems/grack/0.1.1
- RubyGems: https://rubygems.org/gems/grack

## 历史版本号

- 0.1.1 (2020-03-14)
- 0.1.0 (2016-04-30)
- 0.1.0.pre2 (2015-09-22)
- 0.1.0.pre1 (2015-09-14)
- 0.0.2 (2012-10-10)
- 0.0.1 (2012-10-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/grack
- gem 安装: `gem install grack`
- Bundler: `gem "grack"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/grack-0.1.1.gem
- 版本锁定: `gem "grack", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
