# ovh-provisioner

**Tag**: web, cli, testing, security, serialization, networking, template, filesystem

## 简介

OVH::Provisioner
================

Interact with OVH REST API, mainly targeted to manage dedicated servers and
OVH DNS.

Installation
------------

Add this line to your application's Gemfile:

```ruby
gem 'ovh-provisioner'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install ovh-provisioner

Configuration
-------------

The best way to use ovh-provisioner is to create a configuration file
(recommended path: ~/.config/ovh-provisioner.yml) containing your keys and some
general configuration. Then, just launch it to get all commands with their
description.

Example:

```yaml
# All keys can be overriden with cli options
api_url: https://eu.api.ovh.com/1.0
app_key: XXXXXXXXXXXX
app_secret: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
consumer_key: XXXXXXXXXXXXXXXXXXXXXXXXXXXX

template: template_name # is be defined in OVH manager when you save a template
use_distrib_kernel: true
ssh-key: 'key_name_to install'

# name_scheme support any variable available as attribute in
# lib/ovh/provisioner/api_object/dedicated_server.rb
# Along with name_domain, it is used to rename (reverse dns) servers
name_scheme: '%{location}-%{flavor_tag}-%{server_id}.%{vrack}'
name_domain: example.com

# example of flavors, you can use any hardware parameters from
# GET /dedicated/server/{serviceName}/specifications/hardware
# to differentiate your flavors
flavors:
  EG-16S:
    tag: eg16s
    hardware:
      description: 'Serveur EG-16 - E3-1230v6 - 16GB - SoftRaid 2x450GB NVMe'
  EG-32S:
    tag: eg32s
    hardware:
      description: 'Serveur EG-32 - E3-1270v6 - 32GB - SoftRaid 2x450GB NVMe'
  EG-64S:
    tag: eg64s
    hardware:
      description: 'Serveur EG-64 - E5-1650v3 - 64GB - SoftRaid 2x450GB NVMe'
```

Development
-----------

After checking out the repo, run `bin/setup` to install dependencies. Then, run
`rake spec` to run the tests. You can also run `bin/console` for an interactive
prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`. To
release a new version, update the version number in `version.rb`, and then run
`bundle exec rake release`, which will create a git tag for the version, push
git commits and tags, and push the `.gem` file to
[rubygems.org](https://rubygems.org).

Contributing
------------

Please read carefully [CONTRIBUTING.md](CONTRIBUTING.md) before making a merge
request.

License and Author
------------------

- Author:: Samuel Bernard (<samuel.bernard@gmail.com>)

```text
Copyright (c) 2015-2016 Sam4Mobile, 2017-2018 Make.org

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## 官网

- 主页: https://gitlab.com/sre-gems/ovh-provisioner
- 文档: https://www.rubydoc.info/gems/ovh-provisioner/0.1.0
- RubyGems: https://rubygems.org/gems/ovh-provisioner

## 历史版本号

- 0.1.0 (2018-10-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/ovh-provisioner
- gem 安装: `gem install ovh-provisioner`
- Bundler: `gem "ovh-provisioner"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/ovh-provisioner-0.1.0.gem
- 版本锁定: `gem "ovh-provisioner", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
