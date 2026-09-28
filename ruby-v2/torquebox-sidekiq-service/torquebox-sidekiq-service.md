# torquebox-sidekiq-service

**Tag**: cli, testing

## 简介

The TorqueBox Sidekiq service replaces the traditional Sidekiq CLI client for starting a Sidekiq processor.  This
    allows TorqueBox features only available in-container to be usable by all your Sidekiq workers.  It has the added
    benefit of reducing memory overhead by running in a single JVM and allows for better optimization through JIT and
    better debugging & profiling through TorqueBox's runtime inspection facilities.

## 官网

- 主页: http://github.com/mogotest/torquebox-sidekiq-service
- 文档: https://www.rubydoc.info/gems/torquebox-sidekiq-service/0.2.2
- RubyGems: https://rubygems.org/gems/torquebox-sidekiq-service

## 历史版本号

- 0.2.2 (2013-05-28)
- 0.2.1 (2013-05-20)
- 0.2.0 (2013-05-06)
- 0.1.3 (2013-04-30)
- 0.1.2 (2013-04-30)
- 0.1.1 (2013-03-29)
- 0.1.0 (2013-03-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/torquebox-sidekiq-service
- gem 安装: `gem install torquebox-sidekiq-service`
- Bundler: `gem "torquebox-sidekiq-service"`
- 最新版本: 0.2.2
- 最新版归档: https://rubygems.org/downloads/torquebox-sidekiq-service-0.2.2.gem
- 版本锁定: `gem "torquebox-sidekiq-service", "~> 0.2.2"`
- 中央仓库: https://rubygems.org/
