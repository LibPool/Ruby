# syspy

**Tag**: database, networking, data

## 简介

Captures TDS (Sybase / MSSQL) packages directly from a network interface.

Currently, only TDS_LANGUAGE (Query Statements) and their TDS_PARAMFMT/2 TDS_PARAMS are parsed.

There are still many data types missing.

Also replaces parameters from prepared statements (e.g. @sql9_object_id is going to be replaced by the corresponding value from TDS_PARAMS).

Usage:
sudo syspy interface destination_ip destination_port

Example:
sudo syspy eth0 192.168.1.6 2048

## 官网

- 主页: https://github.com/balmma/syspy
- RubyGems: https://rubygems.org/gems/syspy

## 历史版本号

- 0.0.32 (2013-02-27)
- 0.0.31 (2013-02-27)
- 0.0.30 (2013-02-27)
- 0.0.28 (2013-02-19)
- 0.0.27 (2013-02-18)
- 0.0.26 (2013-02-15)
- 0.0.24 (2013-02-15)
- 0.0.23 (2013-02-15)
- 0.0.22 (2013-02-15)
- 0.0.21 (2013-02-15)
- 0.0.20 (2013-02-14)
- 0.0.19 (2013-02-14)
- 0.0.18 (2013-02-14)
- 0.0.17 (2013-01-23)
- 0.0.16 (2013-01-23)
- 0.0.15 (2013-01-23)
- 0.0.14 (2013-01-23)
- 0.0.13 (2013-01-23)
- 0.0.12 (2013-01-23)
- 0.0.11 (2013-01-23)
- 0.0.10 (2012-12-06)
- 0.0.9 (2012-11-28)
- 0.0.8 (2012-11-28)
- 0.0.7 (2012-11-28)
- 0.0.6 (2012-11-28)
- 0.0.5 (2012-11-28)
- 0.0.4 (2012-11-28)
- 0.0.3 (2012-11-28)
- 0.0.2 (2012-11-28)
- 0.0.1 (2012-11-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/syspy
- gem 安装: `gem install syspy`
- Bundler: `gem "syspy"`
- 最新版本: 0.0.32
- 最新版归档: https://rubygems.org/downloads/syspy-0.0.32.gem
- 版本锁定: `gem "syspy", "~> 0.0.32"`
- 中央仓库: https://rubygems.org/
