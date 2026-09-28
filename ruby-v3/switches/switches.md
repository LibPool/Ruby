# switches

**Tag**: web, testing

## 简介

Switches lets you turn on and off parts of your code from the commandline. There's a defaults.yml and a current.yml in the background.

For example:
app/models/user.rb
after_create :subscribe_email if Switches.campaign_monitor?

>> Switches.campaign_monitor?
# => false

$ rake switches:on[campaign_monitor]

>> Switches.campaign_monitor?
# => true

$ rake switches:reset # goes back to default.yml
$ rake switches:diff  # shows diff b/w current.yml and default.yml
$ rake s:d            # alias for switches:diff
$ rake s:c            # alias for switches:list_current

etc.

It's inspired by ActiveSupport's StringInquirer (e.g. Rails.development?) and traditional compile-time assertions.

## 官网

- 主页: http://github.com/seamusabshere/switches
- RubyGems: https://rubygems.org/gems/switches

## 历史版本号

- 0.1.7 (2010-03-30)
- 0.1.6 (2009-11-19)
- 0.1.5 (2009-11-19)
- 0.1.4 (2009-11-18)
- 0.1.3 (2009-11-05)
- 0.1.2 (2009-11-02)
- 0.1.1 (2009-11-02)
- 0.1.0 (2009-10-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/switches
- gem 安装: `gem install switches`
- Bundler: `gem "switches"`
- 最新版本: 0.1.7
- 最新版归档: https://rubygems.org/downloads/switches-0.1.7.gem
- 版本锁定: `gem "switches", "~> 0.1.7"`
- 中央仓库: https://rubygems.org/
