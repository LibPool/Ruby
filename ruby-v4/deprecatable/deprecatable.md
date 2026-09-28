# deprecatable

**Tag**: web

## 简介

Deprecatable is a library to help you, as a developer, deprecate your API and be
proactive about helping people who use your library find where they need to
update.

When using Deprecatable, you mark methods as 'deperecated' and then the users of
your API will receive a helpful alert showing the exact line of code where they
called the deprecated API, and what they need to do to fix it (although you need
to supply this piece of information).

Users will receive, by default, a single alert for each unique location a
deprecated API method is invoked. They will also receive a final report
detailing all the locations where deprecated APIs were invoked.

The "noisiness" of the alerting and the final report is all configurable, via
both code, and environment variables. See Deprecatable::Options.

## 官网

- 主页: http://github.com/copiousfreetime/deprecatable
- 源码仓库: https://github.com/copiousfreetime/deprecatable
- 文档: http://www.copiousfreetime.org/projects/deprecatable/
- 问题追踪: https://github.com/copiousfreetime/deprecatable/issues
- RubyGems: https://rubygems.org/gems/deprecatable

## 历史版本号

- 1.0.0 (2011-08-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/deprecatable
- gem 安装: `gem install deprecatable`
- Bundler: `gem "deprecatable"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/deprecatable-1.0.0.gem
- 版本锁定: `gem "deprecatable", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
