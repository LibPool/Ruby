# rack-sprocketize

**Tag**: web, filesystem

## 简介

Rack::Sprocketize is a piece of Rack Middleware which uses Sprockets to concatenate javascript files and then optionally compresses them. In a development environment, the files will be sprocketized on each request if there have been changes to the source files. In a production environment, the files will only be sprocketized one time, and only if there have been changes. Also, in a production environment, the files will be compressed by whichever javascript compressor is available.

## 官网

- 主页: http://github.com/petebrowne/rack-sprocketize
- 问题追踪: http://github.com/petebrowne/rack-sprocketize/issues
- RubyGems: https://rubygems.org/gems/rack-sprocketize

## 历史版本号

- 0.4.1 (2011-08-30)
- 0.4.0 (2011-03-17)
- 0.3.0 (2011-03-16)
- 0.2.0 (2011-03-15)
- 0.1.0 (2011-03-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack-sprocketize
- gem 安装: `gem install rack-sprocketize`
- Bundler: `gem "rack-sprocketize"`
- 最新版本: 0.4.1
- 最新版归档: https://rubygems.org/downloads/rack-sprocketize-0.4.1.gem
- 版本锁定: `gem "rack-sprocketize", "~> 0.4.1"`
- 中央仓库: https://rubygems.org/
