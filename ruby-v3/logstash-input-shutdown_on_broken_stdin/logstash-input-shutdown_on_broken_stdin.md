# logstash-input-shutdown_on_broken_stdin

**Tag**: library

## 简介

If Logstash is launched as a sub-process, this plugin can be used to exit Logstash when the parent process exits. The parent process should launch the Logstash sub-process using Inherit on Stdin, this way when the parent process exits, the Stdin is broken which is detected by this plugin which exits Logstash

## 官网

- 主页: http://www.elastic.co/guide/en/logstash/current/index.html
- 源码仓库: https://github.com/ksenji/logstash-input-ShutdownOnBrokenStdin
- RubyGems: https://rubygems.org/gems/logstash-input-shutdown_on_broken_stdin

## 历史版本号

- 2.0.4 (2016-02-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/logstash-input-shutdown_on_broken_stdin
- gem 安装: `gem install logstash-input-shutdown_on_broken_stdin`
- Bundler: `gem "logstash-input-shutdown_on_broken_stdin"`
- 最新版本: 2.0.4
- 最新版归档: https://rubygems.org/downloads/logstash-input-shutdown_on_broken_stdin-2.0.4.gem
- 版本锁定: `gem "logstash-input-shutdown_on_broken_stdin", "~> 2.0.4"`
- 中央仓库: https://rubygems.org/
