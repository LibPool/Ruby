# marketo

**Tag**: web, cli, networking, filesystem

## 简介

Allows easy integration with marketo from ruby. You can synchronize leads and fetch them back by email.
     By default this is configured for the SOAP wsdl file: http://app.marketo.com/soap/mktows/1_4?WSDL but this is
     configurable when you construct the client, e.g.
     client = Rapleaf::Marketo.new_client(<access_key>, <secret_key>, (api_subdomain = 'na-i'), (api_version = '1_5'), (document_version = '1_4'))
     More information at https://www.rapleaf.com/developers/marketo.

## 官网

- 主页: https://www.rapleaf.com/developers/marketo
- 源码仓库: https://github.com/Rapleaf/marketo_gem
- 文档: http://rubydoc.info/gems/marketo/1.4.0/frames
- RubyGems: https://rubygems.org/gems/marketo

## 历史版本号

- 1.4.0 (2012-04-03)
- 1.3.1 (2012-04-03)
- 1.2.5 (2011-02-25)
- 1.2.4 (2011-02-25)
- 1.2.3 (2011-02-09)
- 1.2.2 (2011-02-09)
- 1.2.1 (2011-02-08)
- 1.2.0 (2011-02-08)
- 1.1.6 (2011-02-01)
- 1.1.5 (2011-01-31)
- 1.1.4 (2011-01-31)
- 1.1.3 (2011-01-31)
- 1.1.2 (2011-01-31)
- 1.1.1 (2011-01-31)
- 1.1.0 (2011-01-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/marketo
- gem 安装: `gem install marketo`
- Bundler: `gem "marketo"`
- 最新版本: 1.4.0
- 最新版归档: https://rubygems.org/downloads/marketo-1.4.0.gem
- 版本锁定: `gem "marketo", "~> 1.4.0"`
- 中央仓库: https://rubygems.org/
