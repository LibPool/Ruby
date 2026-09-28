# chef-gen-flavor-base

**Tag**: web, testing, networking, template

## 简介

chef-gen-flavor-base is a base class to make it easy to create 'flavors'
for use with
[chef-gen-flavors](https://github.com/jf647/chef-gen-flavors).

chef-gen-flavors plugs into the 'chef generate' command provided by
ChefDK to let you provide an alternate template for cookbooks and other
chef components.

This gem simply provides a class your flavor can derive from; templates
are provided by separate gems, which you can host privately for use
within your organization or publicly for the Chef community to use.

An example flavor that demonstrates how to use this gem is distributed
separately:
[chef-gen-flavor-example](https://github.com/jf647/chef-gen-flavor-example)

At present this is focused primarily on providing templates for
generation of cookbooks, as this is where most organization-specific
customization takes place. Support for the other artifacts that ChefDK
can generate may work, but is not the focus of early releases.

## 官网

- 主页: https://github.com/jf647/chef-gen-flavor-base
- 文档: https://www.rubydoc.info/gems/chef-gen-flavor-base/0.9.2
- RubyGems: https://rubygems.org/gems/chef-gen-flavor-base

## 历史版本号

- 0.9.2 (2015-09-11)
- 0.9.1 (2015-09-10)
- 0.9.0 (2015-09-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/chef-gen-flavor-base
- gem 安装: `gem install chef-gen-flavor-base`
- Bundler: `gem "chef-gen-flavor-base"`
- 最新版本: 0.9.2
- 最新版归档: https://rubygems.org/downloads/chef-gen-flavor-base-0.9.2.gem
- 版本锁定: `gem "chef-gen-flavor-base", "~> 0.9.2"`
- 中央仓库: https://rubygems.org/
