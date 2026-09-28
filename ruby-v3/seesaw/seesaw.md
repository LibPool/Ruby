# seesaw

**Tag**: web, devops

## 简介

== DESCRIPTION:  seesaw: [verb] to change rapidly from one state or condition to another and back again.  Seesaw is a replacement/addition to the mongrel_cluster gem and allows you to perform a safe rippling restart of your mongrel cluster without dropping any requests.  Let's say you have a mongrel cluster setup with 7 individual mongrels on your server. Let's also say that you have to deploy a code update and restart all of your mongrels but your site is really busy and you cannot afford any downtime whatsoever.  When you execute:  mongrel_rails seesaw::bounce  This will happen:  1. your webserver configuration is switched to only use the front half of your mongrel pack (mongrels 1-4) 2. the webserver (apache or nginx) is gracefully restarted 3. the back half of your mongrel pack (mongrels 5-7) is restarted 4. your webserver configuration is switched to only use the back half of the pack 5. the webserver is gracefully restarted 6. front half mongrels are restared 7. webserver configuration switched back to full cluster configuration 8. webserver restarted one last time

## 官网

- 文档: https://www.rubydoc.info/gems/seesaw/0.2.5
- RubyGems: https://rubygems.org/gems/seesaw

## 历史版本号

- 0.2.5 (2009-07-25)
- 0.2.4 (2009-07-25)
- 0.2.3 (2009-07-25)
- 0.2.2 (2009-07-25)
- 0.2.1 (2009-07-25)
- 0.2.0 (2009-07-25)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/seesaw
- gem 安装: `gem install seesaw`
- Bundler: `gem "seesaw"`
- 最新版本: 0.2.5
- 最新版归档: https://rubygems.org/downloads/seesaw-0.2.5.gem
- 版本锁定: `gem "seesaw", "~> 0.2.5"`
- 中央仓库: https://rubygems.org/
