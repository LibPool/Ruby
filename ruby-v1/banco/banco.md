# banco

**Tag**: web, cli, networking, filesystem, data

## 简介

Welcome to Banco !

Banco has been developed to summarize statements downloaded from your bank.
Install as a Rubygem, navigate to the directory your .csv files are in and execute from the command line with 'banco'.

Banco will only accept comma seperated value files (.csv) and will produce a summary for the period uploaded from the file.

Remove the header line from your downloaded bank statement, ensure the columns are ordered date, description, type of charge, money in an money out from left to right, any columns right of the fifth will be ignored. Banco will total the incoming & outgoing transactions for the period. Reporting the bottom line aswell as summing up the values for similar transactions. This is achieved by matching the description name, currently set at the first 9 characters of the string, (:total_outgoing :total_incoming - class Reporter), you can change this to be more or less exact.

Hope your numbers are positive !
https://github.com/s33dco/banco
https://rubygems.org/gems/banco

## 官网

- 主页: https://github.com/s33dco/banco
- 文档: https://www.rubydoc.info/gems/banco/1.0.3
- RubyGems: https://rubygems.org/gems/banco

## 历史版本号

- 1.0.3 (2019-11-14)
- 1.0.2 (2019-06-14)
- 1.0.1 (2019-06-09)
- 1.0.0 (2017-11-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/banco
- gem 安装: `gem install banco`
- Bundler: `gem "banco"`
- 最新版本: 1.0.3
- 最新版归档: https://rubygems.org/downloads/banco-1.0.3.gem
- 版本锁定: `gem "banco", "~> 1.0.3"`
- 中央仓库: https://rubygems.org/
