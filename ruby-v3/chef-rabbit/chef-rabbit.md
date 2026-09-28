# chef-rabbit

**Tag**: web, cli, testing, security, networking, template, filesystem

## 简介

= DESCRIPTION:

Provides a Chef handler which can report run status, including any changes that were made, to a rabbit server. In the case of failed runs a backtrace will be included in the details reported. Based on the Graylog Gelf handler by Jon Wood (&lt;jon@blankpad.net&gt;) https://github.com/jellybob/chef-gelf

= REQUIREMENTS:

* A Rabbit server running somewhere.

= USAGE:

This example makes of the chef_handler cookbook, place some thing like this in cookbooks/chef_handler/recipes/rabbit.rb and add it to your run list. 

  include_recipe "chef_handler::default"

  gem_package "chef-rabbit" do
    action :nothing
  end.run_action(:install)
  
  # Make sure the newly installed Gem is loaded.
  Gem.clear_paths
  require 'chef/rabbit'
  
  chef_handler "Chef::RABBIT::Handler" do
    source "chef/rabbit"
    arguments({
      :connection =&gt; {
        :host =&gt; "your_rabbit_server",
        :user =&gt; "rabbit_user",
        :pass =&gt; "rabbit_pass",
        :vhost =&gt; "/stuff"
      }
      :queue =&gt; {
        :name =&gt; "some_queue",
        :params =&gt; {
          :durable =&gt; true,
          ...
        }
      },
      :exchange =&gt; {
        :name =&gt; "some_exchange",
        :params =&gt; {
          :durable =&gt; true,
          ...
        }
      },
      :timestamp_tag =&gt; "@timestamp"
    })

    supports :exception =&gt; true, :report =&gt; true
  end.run_action(:enable)

Arguments take the form of an options hash, with the following options:

* :connection             - http://rubybunny.info/articles/connecting.html
* :queue                  - rabbit queue info to use. name is set to "chef-client" + durable = true by default
* :exchange               - rabbit exchange to use .default_exchange + durable = true by default 
* :timestamp_tag          - tag for timestamp "timestamp" by default
* :blacklist ({})         - A hash of cookbooks, resources and actions to ignore in the change list.

= BLACKLISTING:

Some resources report themselves as having updated on every run even if nothing changed, or are just things you don't care about. To reduce the amount of noise in your logs these can be ignored by providing a blacklist. In this example we don't want to be told about the GELF handler being activated:

    chef_handler "Chef::RABBIT::Handler" do
      source "chef/rabbit"
      arguments({
        :blacklist =&gt; {
          "chef_handler" =&gt; {
            "chef_handler" =&gt; [ "nothing", "enable" ]
          }
        }
      })

      supports :exception =&gt; true, :report =&gt; true
    end.run_action(:enable)

= LICENSE and AUTHOR:

Copyright 2014 by MTN Satellite Communications

Licensed under the Apache License, Version 2.0 (the “License”); you may not use this file except in compliance with the License. You may obtain a copy of the License at 

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.

## 官网

- 主页: https://github.com/MTNSatelliteComm/chef-rabbit
- 文档: https://www.rubydoc.info/gems/chef-rabbit/1.0.13
- RubyGems: https://rubygems.org/gems/chef-rabbit

## 历史版本号

- 1.0.13 (2015-08-25)
- 1.0.12 (2015-08-14)
- 1.0.11 (2014-12-08)
- 1.0.10 (2014-05-05)
- 1.0.9 (2014-04-24)
- 1.0.8 (2014-04-24)
- 1.0.7 (2014-04-24)
- 1.0.6 (2014-04-24)
- 1.0.5 (2014-04-24)
- 1.0.4 (2014-04-23)
- 1.0.3 (2014-04-23)
- 1.0.1 (2014-04-23)
- 1.0.0 (2014-04-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/chef-rabbit
- gem 安装: `gem install chef-rabbit`
- Bundler: `gem "chef-rabbit"`
- 最新版本: 1.0.13
- 最新版归档: https://rubygems.org/downloads/chef-rabbit-1.0.13.gem
- 版本锁定: `gem "chef-rabbit", "~> 1.0.13"`
- 中央仓库: https://rubygems.org/
