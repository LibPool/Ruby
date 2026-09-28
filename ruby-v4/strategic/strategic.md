# strategic

**Tag**: library

## 简介

if/case conditionals can get really hairy in highly sophisticated business domains.
Domain model inheritance can help remedy the problem, but you don't want to dump all
logic variations in the same domain models.
Strategy Pattern solves that problem by externalizing logic variations to
separate classes outside the domain models.
One difficulty with implementing Strategy Pattern is making domain models aware
of newly added strategies without touching their code (Open/Closed Principle).
Strategic solves that problem by supporting Strategy Pattern with automatic discovery
of strategies and ability fetch the right strategy without conditionals.
This allows you to make any domain model "strategic" by simply following a convention
in the directory/namespace structure you create your strategies under so that the domain
model automatically discovers all available strategies.

## 官网

- 主页: http://github.com/AndyObtiva/strategic
- 文档: https://www.rubydoc.info/gems/strategic/1.2.0
- RubyGems: https://rubygems.org/gems/strategic

## 历史版本号

- 1.2.0 (2022-01-23)
- 1.1.0 (2021-09-14)
- 1.0.1 (2021-09-14)
- 1.0.0 (2021-03-29)
- 0.9.1 (2021-03-17)
- 0.9.0 (2021-03-15)
- 0.8.0 (2020-01-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/strategic
- gem 安装: `gem install strategic`
- Bundler: `gem "strategic"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/strategic-1.2.0.gem
- 版本锁定: `gem "strategic", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
