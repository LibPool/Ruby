# care_bert

**Tag**: database, testing, data

## 简介

CareBert analyzes the current items of your database and performs differing validation and integrity tests. Currently it supports following checks: \n - Table Integrity =&gt; check each single model-instance of all available tables can be loaded \n - Model Validation =&gt; triggers the validation of each single model-instance (which results might have changed due code-modifications) \n - Missing Assocs =&gt; tries to load each instance of an assoc, if the foreign_key is set (having a present FK doesn't mean it really has the targeted model available)

## 官网

- 主页: https://github.com/loybert/care_bert
- 文档: https://www.rubydoc.info/gems/care_bert/0.0.5
- RubyGems: https://rubygems.org/gems/care_bert

## 历史版本号

- 0.0.5 (2015-03-06)
- 0.0.4 (2015-01-22)
- 0.0.3 (2014-10-02)
- 0.0.2 (2014-10-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/care_bert
- gem 安装: `gem install care_bert`
- Bundler: `gem "care_bert"`
- 最新版本: 0.0.5
- 最新版归档: https://rubygems.org/downloads/care_bert-0.0.5.gem
- 版本锁定: `gem "care_bert", "~> 0.0.5"`
- 中央仓库: https://rubygems.org/
