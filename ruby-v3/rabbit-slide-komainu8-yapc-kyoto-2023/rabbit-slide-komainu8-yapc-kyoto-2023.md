# rabbit-slide-komainu8-yapc-kyoto-2023

**Tag**: web, database, networking

## 简介

MySQLのデータを全文検索したいときの良くあるアプローチは以下の3つがありますが、それぞれ課題があります。

1. MySQLのデフォルトのストレージエンジンInnoDBの全文検索機能を使う。
2. 別途Elasticsearchを用意し、アプリケーションでMySQLとElasticsearchのデータを同期し、検索はElasticsearchで行う。
3. 別途Elasticsearchを用意し、Logstashを使ってMySQLのデータをElasticsearchに同期する。

上記のアプローチの課題を解決する方法として、GroongaとGroongaのデータをMySQLに取り込むツール、GroongaのHTTPでクライアントライブラリーを組み合わせた構成を紹介します。

## 官网

- 主页: https://slide.rabbit-shocker.org/authors/komainu8/yapc-kyoto-2023/
- 文档: https://www.rubydoc.info/gems/rabbit-slide-komainu8-yapc-kyoto-2023/2023.3.19.6
- RubyGems: https://rubygems.org/gems/rabbit-slide-komainu8-yapc-kyoto-2023

## 历史版本号

- 2023.3.19.6 (2023-03-17)
- 2023.3.19.5 (2023-03-16)
- 2023.3.19.4 (2023-03-16)
- 2023.3.19.3 (2023-03-16)
- 2023.3.19.2 (2023-03-16)
- 2023.3.19.1 (2023-03-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/rabbit-slide-komainu8-yapc-kyoto-2023
- gem 安装: `gem install rabbit-slide-komainu8-yapc-kyoto-2023`
- Bundler: `gem "rabbit-slide-komainu8-yapc-kyoto-2023"`
- 最新版本: 2023.3.19.6
- 最新版归档: https://rubygems.org/downloads/rabbit-slide-komainu8-yapc-kyoto-2023-2023.3.19.6.gem
- 版本锁定: `gem "rabbit-slide-komainu8-yapc-kyoto-2023", "~> 2023.3.19.6"`
- 中央仓库: https://rubygems.org/
