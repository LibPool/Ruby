# activerecord_idnamecache

**Tag**: web, database, networking, data

## 简介

Use Mysql AUTO_INCREMENT to support key value cache, which should be combined by an integer and string. It means to reduce the database storage size, and improve query performance.  All cache will store in process memory, and will never be expired, until the process dies, so the less kvs you use, the better performance you will get. BTW, 100,000 general strings use 10MB memory.  Some relatived articles: http://en.wikipedia.org/wiki/Correlation_database  Usage ------------------------------------------ ## setup  ```ruby create_table :kv_browser_names, :options => 'ENGINE=MyISAM DEFAULT CHARSET=utf8' do |t| t.string :name t.timestamps end  class KvBrowserName < ActiveRecord::Base include IdNameCache end ```  or  ```ruby create_table :common_tag, :options => 'ENGINE=MyISAM DEFAULT CHARSET=utf8' do |t| t.integer :tagid t.string  :tagname end  class CommonTag < ActiveRecord::Base self.table_name = :common_tag self.primary_key = :tagid  include IdNameCache; set_key_value :tagid, :tagname # include IdNameCache; set_key_value_without_create :tagid, :tagname # if you dont want create it automately end ```  ### use cases  ```text ruby-1.9.3-rc1 :001 > QuizTag[1] QuizTag Load (0.3ms)  SELECT `common_tag`.* FROM `common_tag` WHERE `common_tag`.`tagid` = 1 LIMIT 1 => "Android" ruby-1.9.3-rc1 :002 > QuizTag[1] => "Android" ruby-1.9.3-rc1 :003 > QuizTag['Android'] QuizTag Load (0.5ms)  SELECT `common_tag`.* FROM `common_tag` WHERE `common_tag`.`tagname` = 'Android' LIMIT 1 => 1 ruby-1.9.3-rc1 :004 > QuizTag['Android'] => 1 ```  == Copyright MIT, David Chen at eoe.cn

## 官网

- 主页: http://github.com/mvj3/activerecord_idnamecache
- 文档: https://www.rubydoc.info/gems/activerecord_idnamecache/0.1
- RubyGems: https://rubygems.org/gems/activerecord_idnamecache

## 历史版本号

- 0.1 (2013-06-30)
- 0.0.4 (2013-06-22)
- 0.0.3 (2013-05-31)
- 0.0.2 (2013-03-05)
- 0.0.1 (2013-01-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/activerecord_idnamecache
- gem 安装: `gem install activerecord_idnamecache`
- Bundler: `gem "activerecord_idnamecache"`
- 最新版本: 0.1
- 最新版归档: https://rubygems.org/downloads/activerecord_idnamecache-0.1.gem
- 版本锁定: `gem "activerecord_idnamecache", "~> 0.1"`
- 中央仓库: https://rubygems.org/
