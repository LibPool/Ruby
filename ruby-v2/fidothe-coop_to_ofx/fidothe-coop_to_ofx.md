# fidothe-coop_to_ofx

**Tag**: testing, serialization, template, filesystem

## 简介

Convert statement HTML from the Co-operative bank's online banking system to OFX for import into financial apps.  = Usage  For a Current Account:  1. Save the HTML source of the statement page.  coop_to_ofx --current /path/to/statement.html  Will produce /path/to/statement.ofx  For a Credit Card:  1. Save the HTML source of the statement page  coop_to_ofx /path/to/statement.html  Or  coop_to_ofx --credit /path/to/statement.html  Will produce /path/to/statement.ofx   To produce OFX 1 SGML (rather than OFX 2 XML):  coop_to_ofx --ofx1 /path/to/statement.html coop_to_ofx --ofx1 --current /path/to/statement.html  To show all the options:  coop_to_ofx --help    == To do  XML / SGML validation of output against the specs

## 官网

- 主页: http://reprocessed.org/
- 文档: https://www.rubydoc.info/gems/fidothe-coop_to_ofx/1.0.1
- RubyGems: https://rubygems.org/gems/fidothe-coop_to_ofx

## 历史版本号

- 1.0.1 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/fidothe-coop_to_ofx
- gem 安装: `gem install fidothe-coop_to_ofx`
- Bundler: `gem "fidothe-coop_to_ofx"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/fidothe-coop_to_ofx-1.0.1.gem
- 版本锁定: `gem "fidothe-coop_to_ofx", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
