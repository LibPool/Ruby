# autocronitor

**Tag**: cli, template, filesystem

## 简介

A CLI tool to parse a standard format crontab file, create monitors in cronitor.io for each job, and automatically add the necessary curl commands to the original crontab. It assumes that you are using cronitor's 'template' feature to configure notifications for your monitors, and that you have created templates which will then be passed to autocronitor. Please note, cronitor.io (and therefore autocronitor) do not support 'informal' cron expressions such as @hourly or @daily.

## 官网

- 主页: https://github.com/jonlives/autocronitor
- 文档: https://www.rubydoc.info/gems/autocronitor/0.0.5
- RubyGems: https://rubygems.org/gems/autocronitor

## 历史版本号

- 0.0.5 (2017-06-22)
- 0.0.4 (2016-03-08)
- 0.0.3 (2015-12-22)
- 0.0.2 (2015-12-14)
- 0.0.1 (2015-12-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/autocronitor
- gem 安装: `gem install autocronitor`
- Bundler: `gem "autocronitor"`
- 最新版本: 0.0.5
- 最新版归档: https://rubygems.org/downloads/autocronitor-0.0.5.gem
- 版本锁定: `gem "autocronitor", "~> 0.0.5"`
- 中央仓库: https://rubygems.org/
