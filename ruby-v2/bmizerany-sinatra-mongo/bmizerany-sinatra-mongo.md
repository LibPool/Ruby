# bmizerany-sinatra-mongo

**Tag**: web, database, testing, security, networking, filesystem, data

## 简介

= sinatra-mongo

Extends Sinatra with an extension method for dealing with monogodb using the ruby driver.


Install it with gem:

    $ gem install sinatra-mongo

Now we can use it an example application.

    require 'sinatra'
    require 'sinatra/mongo'

    # Specify the database to use. Defaults to mongo://localhost:27017/default,
    # so you will almost definitely want to change this.
    #
    # Alternatively, you can specify the MONGO_URL as an environment variable
    set :mongo, 'mongo://localhost:27017/sinatra-mongo-example'

    # At this point, you can access the Mongo::Database object using the 'mongo' helper:

    puts mongo["testCollection"].insert {"name" => "MongoDB", "type" => "database", "count" => 1, "info" => {"x" => 203, "y" => '102'}}

    get '/' do
      mongo["testCollection"].find_one
    end

If you need to use authentication, you can specify this in the mongo uri:

    set :mongo, 'mongo://myuser:mypass@localhost:27017/sinatra-mongo-example'

== Mongo Reference

 * http://www.mongodb.org/display/DOCS/Ruby+Tutorial

== Note on Patches/Pull Requests

* Fork the project.
* Make your feature addition or bug fix.
* Add tests for it. This is important so I don't break it in a
  future version unintentionally.
* Commit, do not mess with rakefile, version, or history.
  (if you want to have your own version, that is fine but bump version in a commit by itself I can ignore when I pull)
* Send me a pull request. Bonus points for topic branches.

== Copyright

Copyright (c) 2009 Joshua Nichols. See LICENSE for details.

## 官网

- 主页: http://github.com/technicalpickles/sinatra-mongo
- RubyGems: https://rubygems.org/gems/bmizerany-sinatra-mongo

## 历史版本号

- 0.0.3 (2010-05-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/bmizerany-sinatra-mongo
- gem 安装: `gem install bmizerany-sinatra-mongo`
- Bundler: `gem "bmizerany-sinatra-mongo"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/bmizerany-sinatra-mongo-0.0.3.gem
- 版本锁定: `gem "bmizerany-sinatra-mongo", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
