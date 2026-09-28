# rack_session_mongo

**Tag**: web, cli, database, testing, data

## 简介

require 'mongo'
require 'rake_session_mongo'
$db=Mongo::Client.new   ["localhost:27017"], :database=&gt;'test'
configure do
    use Rack::Session::Mongo,:collection=&gt;$db[:session]
end

## 官网

- 主页: https://github.com/KaltZK/rack_session_mongo
- 文档: https://www.rubydoc.info/gems/rack_session_mongo/0.1.0
- RubyGems: https://rubygems.org/gems/rack_session_mongo

## 历史版本号

- 0.0.1 (2016-05-19)
- 0.1.0 (2016-05-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack_session_mongo
- gem 安装: `gem install rack_session_mongo`
- Bundler: `gem "rack_session_mongo"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/rack_session_mongo-0.1.0.gem
- 版本锁定: `gem "rack_session_mongo", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
