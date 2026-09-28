# cors

**Tag**: web, cli, filesystem

## 简介

Cross-origin resource sharing (CORS) is great; it allows your visitors to
asynchronously upload files to e.g. Filepicker or Amazon S3, without the
files having to round-trip through your web server. Unfortunately, giving
your users complete write access to your online storage also exposes you to
malicious intent.

To combat harmful usage, good upload services that allow client-side
upload, support a mechanism that allows you to validate and sign all upload
requests to your online storage. By validating every request, you can give
your visitors a nice upload experience, while keeping the bad visitors at
bay.

The CORS gem comes with support for the Amazon S3 REST API.

## 官网

- 主页: http://github.com/elabs/cors
- 文档: https://www.rubydoc.info/gems/cors/1.0.1
- RubyGems: https://rubygems.org/gems/cors

## 历史版本号

- 1.0.1 (2019-08-08)
- 1.0.0 (2012-10-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/cors
- gem 安装: `gem install cors`
- Bundler: `gem "cors"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/cors-1.0.1.gem
- 版本锁定: `gem "cors", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
