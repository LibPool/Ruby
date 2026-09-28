# switch-cli

**Tag**: cli, testing, serialization, filesystem, data

## 简介

Switch helps you add multiple languages to your site by leveraging the power of google spreadsheets. It is a commandline tool providing you with an easy way to automate the process and avoid common mistakes.

  The most common use case of switch is for switching between a locale representation in JSON/YAML to a CSV (spreadsheet) based one and vice-versa.

  # Install

  ```
  gem install switch-cli
  ```

  # Usage

  ```
  switch json2csv [input-dir] [output-file]
  ```

  Converts multiple json files to be a single csv file with columns for each file, with the file name as the column header.

  If you do not specify an input-dir it will be taken as ./locales and output-file would be the direcotry name + .csv.

  ```
  switch csv2json [input-file] [output-dir]
  ```

  Converts a single csv file into multiple json files, with a file for each column using the key and order columns to construct the files.

## 官网

- 主页: https://github.com/yagudaev/switch
- 问题追踪: https://github.com/yagudaev/switch/issues
- RubyGems: https://rubygems.org/gems/switch-cli

## 历史版本号

- 0.0.8 (2016-08-25)
- 0.0.7 (2016-05-26)
- 0.0.5 (2016-05-21)
- 0.0.3 (2016-04-15)
- 0.0.2 (2016-01-20)
- 0.0.1 (2016-01-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/switch-cli
- gem 安装: `gem install switch-cli`
- Bundler: `gem "switch-cli"`
- 最新版本: 0.0.8
- 最新版归档: https://rubygems.org/downloads/switch-cli-0.0.8.gem
- 版本锁定: `gem "switch-cli", "~> 0.0.8"`
- 中央仓库: https://rubygems.org/
