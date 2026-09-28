# rabbit-slide-komainu8-dbstudychugoku-28th

**Tag**: web, database, testing, networking, template, devops

## 简介

PostgreSQL で使用できる全文検索の拡張に PGroonga という高速で高性能な拡張があります。 PGroonga は、全言語対応の超高速全文検索機能を PostgreSQL で使えるようにする拡張で、 安定して高速で、かつ高機能（同義語、表記ゆれや異字体への対応、類似文書検索などが使えます）です。

Amazon RDS は Amazon がクラウド上で提供する RDBS サービスで、データベースのインストールや パッチ適用、スケールアウト、バックアップなどを Amazon が面倒をみてくれるため、 運用上の手間を大幅に減らすことができます。

Amazon RDS は、とても便利なのですが、拡張機能を自由にインストールすることができません。 以下の URL の一覧にある拡張しか使えません。
https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts.General.FeatureSupport.Extensions.11x

PGroonga も使えないため、日本語を始めとする多言語対応の超高速全文検索機能を Amazon RDS では使うことができません。

そこで、PostgreSQL 10 から使えるようになった、ロジカルレプリケーションと Amazon EC2 上にインストールした PostgreSQL と PGroonga を使って RDS のメリットである、 運用の負担を少なくしつつ、PGroonga を使用して高速で高機能な全文検索ができるような構成を考えました。

本発表では、どのような構成で Amazon RDS のメリットを活かしつつ、Amazon EC2 上で PGroonga を使った全文検索ができるのかを紹介します。

## 官网

- 主页: https://slide.rabbit-shocker.org/authors/komainu8/dbstudychugoku-28th/
- 文档: https://www.rubydoc.info/gems/rabbit-slide-komainu8-dbstudychugoku-28th/2020.01.25.0
- RubyGems: https://rubygems.org/gems/rabbit-slide-komainu8-dbstudychugoku-28th

## 历史版本号

- 2020.01.25.0 (2020-01-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/rabbit-slide-komainu8-dbstudychugoku-28th
- gem 安装: `gem install rabbit-slide-komainu8-dbstudychugoku-28th`
- Bundler: `gem "rabbit-slide-komainu8-dbstudychugoku-28th"`
- 最新版本: 2020.01.25.0
- 最新版归档: https://rubygems.org/downloads/rabbit-slide-komainu8-dbstudychugoku-28th-2020.01.25.0.gem
- 版本锁定: `gem "rabbit-slide-komainu8-dbstudychugoku-28th", "~> 2020.01.25.0"`
- 中央仓库: https://rubygems.org/
