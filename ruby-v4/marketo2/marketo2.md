# marketo2

**Tag**: web, cli, networking, filesystem

## 简介

Allows easy integration with marketo from ruby (v2 and up). You can synchronize leads and fetch them back by email.
     By default this is configured for the SOAP wsdl file: http://app.marketo.com/soap/mktows/1_4?WSDL but this is
     configurable when you construct the client, e.g.
     client = Rapleaf::Marketo.new_client(<access_key>, <secret_key>, (api_subdomain = 'na-i'), (api_version = '1_5'), (document_version = '1_4'))
     More information at https://www.rapleaf.com/developers/marketo.
     Forked from James O'Brien's marketo gem.

## 官网

- 主页: https://github.com/hanaiapa/marketo2
- RubyGems: https://rubygems.org/gems/marketo2

## 历史版本号

- 1.4.0 (2013-10-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/marketo2
- gem 安装: `gem install marketo2`
- Bundler: `gem "marketo2"`
- 最新版本: 1.4.0
- 最新版归档: https://rubygems.org/downloads/marketo2-1.4.0.gem
- 版本锁定: `gem "marketo2", "~> 1.4.0"`
- 中央仓库: https://rubygems.org/
