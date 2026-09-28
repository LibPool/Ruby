# strelka-cors

**Tag**: web, networking

## 简介

This is a Strelka application plugin for describing rules for [Cross-Origin Resource Sharing (CORS)](http://www.w3.org/TR/cors/).

NOTE: It's still a work in progress.

By default, the plugin has paranoid defaults, and doesn't do anything. You'll need to grant access to the resources you want to share.

To grant access, you declare one or more `access_control` blocks which can modify responses to matching access-control requests. All the blocks which match the incoming request's URI are called with the request and response objects in the order in which they're declared: 

	# Allow access to all resources from any origin by default
	access_control do |req, res|
		res.allow_origin '*'
		res.allow_methods 'GET', 'POST'
		res.allow_credentials
		res.allow_headers :content_type
	end


These are applied in the order you declare them, with each matching block passed the request if it matches. This happens before the application gets the request, so it can do any further modification it needs to, and so it can block requests from disallowed origins/methods/etc.

There are a number of helper methods added to the request and response objects for applying and declaring access-control rules when this plugin is loaded:

## 官网

- 主页: http://deveiate.org/projects/strelka-cors
- 文档: https://www.rubydoc.info/gems/strelka-cors/0.0.1
- RubyGems: https://rubygems.org/gems/strelka-cors

## 历史版本号

- 0.0.1 (2016-11-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/strelka-cors
- gem 安装: `gem install strelka-cors`
- Bundler: `gem "strelka-cors"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/strelka-cors-0.0.1.gem
- 版本锁定: `gem "strelka-cors", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
