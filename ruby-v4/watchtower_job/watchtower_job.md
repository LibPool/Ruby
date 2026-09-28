# watchtower_job

**Tag**: web

## 简介

Reads the interface execution kinesis stream for NT2.  Then it uses that execution info combined with information from VINE Services to determine if this is an error state.  If it is, it sends a message to Einstein.  It also clears Einstein alarms related to tracked errors.  State is not tracked between runs, so if the job fails it won't manage previously created errors.

## 官网

- 文档: https://www.rubydoc.info/gems/watchtower_job/1.3.0
- RubyGems: https://rubygems.org/gems/watchtower_job

## 历史版本号

- 1.3.0 (2018-04-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/watchtower_job
- gem 安装: `gem install watchtower_job`
- Bundler: `gem "watchtower_job"`
- 最新版本: 1.3.0
- 最新版归档: https://rubygems.org/downloads/watchtower_job-1.3.0.gem
- 版本锁定: `gem "watchtower_job", "~> 1.3.0"`
- 中央仓库: https://rubygems.org/
