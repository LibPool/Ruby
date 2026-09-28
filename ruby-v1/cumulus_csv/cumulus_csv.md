# cumulus_csv

**Tag**: web, devops, filesystem, data

## 简介

CSV Files: I hate them, you probably do too, but sometimes you need to get data into your system and this is the only way it's happening.  

    If you're deploying a rails app in a cloud setup, you may have troubles if you're trying to store an uploaded file locally and process it later in a background thread (I know I have).  

    cumulus_csv is one way to solve that problem.  You can save your file to your S3 account, and loop over the data inside it at your convenience later.  So it doesn't matter where you're doing the processing, you just need to have the key you used to store the file, and you can process away.

## 官网

- 主页: http://github.com/evizitei/cumulus_csv
- RubyGems: https://rubygems.org/gems/cumulus_csv

## 历史版本号

- 0.1.0 (2010-04-28)
- 0.0.3 (2010-04-28)
- 0.0.2 (2010-03-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/cumulus_csv
- gem 安装: `gem install cumulus_csv`
- Bundler: `gem "cumulus_csv"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/cumulus_csv-0.1.0.gem
- 版本锁定: `gem "cumulus_csv", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
