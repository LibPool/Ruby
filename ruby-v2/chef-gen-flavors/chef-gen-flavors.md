# chef-gen-flavors

**Tag**: web, testing, networking, template

## 简介

chef-gen-flavors is a framework for creating custom templates for the
'chef generate' command provided by ChefDK.

This gem simply provides a framework; templates are provided by separate
gems, which you can host privately for use within your organization or
publicly for the Chef community to use.

[chef-gen-flavor-base](https://github.com/jf647/chef-gen-flavor-base) is
a base class that makes it easy to compose a flavor from reusable
snippets of functionality, and using it is highly recommended.  Using
chef-gen-flavors on its own is only suitable if you already have a
template which is a copy of the skeleton provided by ChefDK.

At present this is focused primarily on providing templates for
generation of cookbooks, as this is where most organization-specific
customization takes place. Support for the other artifacts that ChefDK
can generate may work, but is not the focus of early releases.

## 官网

- 主页: https://github.com/jf647/chef-gen-flavors
- 文档: https://www.rubydoc.info/gems/chef-gen-flavors/0.9.1
- RubyGems: https://rubygems.org/gems/chef-gen-flavors

## 历史版本号

- 0.9.1 (2015-09-11)
- 0.9.0 (2015-09-09)
- 0.8.6 (2015-08-06)
- 0.8.5 (2015-07-16)
- 0.8.4 (2015-07-14)
- 0.8.3 (2015-06-19)
- 0.8.2 (2015-06-18)
- 0.8.1 (2015-06-18)
- 0.8.0 (2015-06-18)
- 0.7.0 (2015-06-09)
- 0.6.2 (2015-06-05)
- 0.6.1 (2015-06-05)
- 0.6.0 (2015-06-05)
- 0.5.0 (2015-05-18)
- 0.4.0 (2015-05-15)
- 0.3.0 (2015-05-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/chef-gen-flavors
- gem 安装: `gem install chef-gen-flavors`
- Bundler: `gem "chef-gen-flavors"`
- 最新版本: 0.9.1
- 最新版归档: https://rubygems.org/downloads/chef-gen-flavors-0.9.1.gem
- 版本锁定: `gem "chef-gen-flavors", "~> 0.9.1"`
- 中央仓库: https://rubygems.org/
