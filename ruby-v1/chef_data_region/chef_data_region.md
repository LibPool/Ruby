# chef_data_region

**Tag**: web, cli, testing, security, devops, filesystem, data

## 简介

# Chef Data Region

## Description

Chef Data Region extends the `Chef::DSL::DataQuery` module's
`data_bag_item` method with the ability to dynamically expand the data
bag name in a configurable, environment-specific manner.

## Motivation

This gem exists to address the following scenario:

An organization maintains data in Chef data bag items. The data is
deployed to several data center environments and is stored in data
bags whose names reference the environments. The organization wants to
write environment-agnostic recipes that access the data bags without
explicitly referencing the data bags by their environment names.

As a concrete example, imagine the organization maintains encrypted
data for three deployment environments: development, staging, and
production. It maintains this data in three data bags, one for each
environment, with data for services named `gadget` and `widget` in
items:

    | Environment | Bag            | Item   |
    |-------------+----------------+--------|
    | Development | secure-dev     | gadget |
    | Development | secure-dev     | widget |
    | Production  | secure-prod    | gadget |
    | Production  | secure-prod    | widget |
    | Staging     | secure-staging | gadget |
    | Staging     | secure-staging | widget |

The items are encrypted with a key unique to that environment to
maximize security.

Now consider how a recipe would access these bags. When then recipe is
running, it needs to know the data center environment in order to
construct the bag name. The organization would most likely assign the
enviroment name to a node attribute. In a naive implementation, each
recipe would include logic that examined the attribute's value to
determine which bag to load. This would obviously duplicate code.

Imagine instead that the organization wants to reference the bag by
the name `secure` and rely on an _abstraction_ to translate `secure`
into the environment-specific bag name.

This gem provides that abstraction.

## Features

This gem overrides the `data_bag_item` method with configurable logic
that dynamically decides which bag to load. It retains API
compatibility with `Chef::DSL::DataQuery#data_bag_item`, so existing
recipes that call `data_bag_item` work without modification.

The gem imposes no constraints on data bag item structure.

## Configuration

Assign the region name to a node attribute that varies by environment:

    node.default['local'][region'] = 'staging'

Add the following configuration to Chef Client's `client.rb` file.

  * Require the gem:

        require 'chef/data_region'

  * Configure the gem with a hash that maps a bag name to an expansion
    pattern:

        Chef::DataRegion.add(
          'secure',
          { attribute: %w(local region), pattern: 'secure-%&lt;attribute&gt;s' }
        )

## Bag name expansion

The gem expands bag names using Ruby's `format` method.

_More pending..._

## 官网

- 主页: https://so.me.one
- 文档: https://www.rubydoc.info/gems/chef_data_region/1.0.6
- RubyGems: https://rubygems.org/gems/chef_data_region

## 历史版本号

- 1.0.6 (2018-04-24)
- 1.0.5 (2018-04-24)
- 1.0.4 (2018-04-24)
- 1.0.3 (2018-04-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/chef_data_region
- gem 安装: `gem install chef_data_region`
- Bundler: `gem "chef_data_region"`
- 最新版本: 1.0.6
- 最新版归档: https://rubygems.org/downloads/chef_data_region-1.0.6.gem
- 版本锁定: `gem "chef_data_region", "~> 1.0.6"`
- 中央仓库: https://rubygems.org/
