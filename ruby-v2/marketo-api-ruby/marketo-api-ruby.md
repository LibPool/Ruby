# marketo-api-ruby

**Tag**: web, networking

## 简介

MarketoAPI (marketo-api-ruby) provides a native Ruby interface to the
{Marketo SOAP API}[http://developers.marketo.com/documentation/soap/], using
{savon}[https://github.com/savonrb/savon]. While understanding the Marketo SOAP
API is necessary for using marketo-api-ruby, it is an explicit goal that
working with MarketoAPI not feel like working with a hinky Java port.

This is release 0.9.1, targeting Marketo API version
{2.3}[http://app.marketo.com/soap/mktows/2_3?WSDL], fixing a +syncLead+ problem
where +Id+, +Email+, and +ForeignSysPersonId+ are inconsistent with other
+syncLead+ parameters. This fixes an issue with Marketo campaign methods.

Please note that Ruby 1.9.2 is not officially supported, but MarketoAPI will
install on any version of Ruby 1.9.2 or later.

## 官网

- 主页: https://github.com/ClearFit/marketo-api-ruby
- 文档: https://www.rubydoc.info/gems/marketo-api-ruby/0.9.2
- RubyGems: https://rubygems.org/gems/marketo-api-ruby

## 历史版本号

- 0.9.2 (2014-08-01)
- 0.9.1 (2014-05-15)
- 0.9 (2014-05-12)
- 0.8 (2014-04-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/marketo-api-ruby
- gem 安装: `gem install marketo-api-ruby`
- Bundler: `gem "marketo-api-ruby"`
- 最新版本: 0.9.2
- 最新版归档: https://rubygems.org/downloads/marketo-api-ruby-0.9.2.gem
- 版本锁定: `gem "marketo-api-ruby", "~> 0.9.2"`
- 中央仓库: https://rubygems.org/
