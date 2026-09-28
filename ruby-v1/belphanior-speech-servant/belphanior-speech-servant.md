# belphanior-speech-servant

**Tag**: web, testing, serialization, networking, filesystem

## 简介

Belphanior speech servant outputs speech to attached audio hardware using the 'espeak' command-line tool. To use,

    * Create a "servant_config" file specifying the host IP and port using the following JSON:
    {"ip":"127.0.0.1","port":3000}
    * run bin/belphanior_speech_servant.
    * Connect to the servant at http://127.0.0.1:3000 to learn more. Your Belphanior butler can connect
      to the servant at http://127.0.0.1:3000/protocol

## 官网

- 主页: http://belphanior.net
- RubyGems: https://rubygems.org/gems/belphanior-speech-servant

## 历史版本号

- 0.0.2 (2012-11-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/belphanior-speech-servant
- gem 安装: `gem install belphanior-speech-servant`
- Bundler: `gem "belphanior-speech-servant"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/belphanior-speech-servant-0.0.2.gem
- 版本锁定: `gem "belphanior-speech-servant", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
