# bjornblomqvist-rails_vcstatus_logger

**Tag**: web, testing, networking, filesystem

## 简介

= rails_vcstatus_logger  It adds current state of version control to the log when you start the server.  * Currently only supports git  Adds current version hash and result of `git diff`  The idea is that you can be sure about what source was running when you look in the log. I recently had a situation where i wasn't sure when a change was put up on the live server.  Please add support for your vc system and send me a pull request!  Just add this to enivorment.rb  config.gem 'bjornblomqvist-rails_vcstatus_logger', :lib =&gt; 'rails_vcstatus_logger', :source =&gt; 'http://gems.github.com'  == Note on Patches/Pull Requests  * Fork the project. * Make your feature addition or bug fix. * Add tests for it. This is important so I don't break it in a future version unintentionally. * Commit, do not mess with rakefile, version, or history. (if you want to have your own version, that is fine but bump version in a commit by itself I can ignore when I pull) * Send me a pull request. Bonus points for topic branches.  == Copyright  Copyright (c) 2009 Bjorn Blomqvist. See LICENSE for details.

## 官网

- 主页: http://github.com/bjornblomqvist/rails_vcstatus_logger
- 文档: https://www.rubydoc.info/gems/bjornblomqvist-rails_vcstatus_logger/0.1.7
- RubyGems: https://rubygems.org/gems/bjornblomqvist-rails_vcstatus_logger

## 历史版本号

- 0.1.1 (2014-08-11)
- 0.1.3 (2014-08-11)
- 0.1.4 (2014-08-11)
- 0.1.5 (2014-08-11)
- 0.1.6 (2014-08-11)
- 0.1.7 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/bjornblomqvist-rails_vcstatus_logger
- gem 安装: `gem install bjornblomqvist-rails_vcstatus_logger`
- Bundler: `gem "bjornblomqvist-rails_vcstatus_logger"`
- 最新版本: 0.1.7
- 最新版归档: https://rubygems.org/downloads/bjornblomqvist-rails_vcstatus_logger-0.1.7.gem
- 版本锁定: `gem "bjornblomqvist-rails_vcstatus_logger", "~> 0.1.7"`
- 中央仓库: https://rubygems.org/
