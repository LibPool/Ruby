# bonsai-elasticsearch-rails

**Tag**: web, cli, security, networking, devops

## 简介

This gem offers a shim to connect Rails apps with a Bonsai
  Elasticsearch cluster. The official Elasticsearch gem package
  requires some minor configuration tweaks in order to work
  correctly with Bonsai (namely the client needs to be instantiated
  with the cluster location and HTTP authentication details), and
  the process can be somewhat complicated for users who are
  unfamiliar with the system.

  The bonsai-elasticsearch-rails gem automatically sets up the
  Elasticsearch client correctly so users don't need to worry about
  configuring it in their code or writing an initializer.

  In order for the gem to work correctly, the application needs an
  environment variable called `BONSAI_URL`, which is populated with
  the complete Bonsai Elaticsearch cluster URL, including the HTTP
  authentication. The cluster URL will follow this pattern:

  https://user1234:pass5678@cluster-slug-123.aws-region-X.bonsai.io/

  On Heroku, this variable is created and populated automatically
  when Bonsai is added to the application. Heroku users therefore do
  not need to perform any additional configuration to connect to
  their cluster after adding the bonsai-elasticsearch-rails gem.

  Users who are self-hosting their Rails app will need to make sure
  this environment variable is present:

  export BONSAI_URL="https://user1234:pass5678@aws-region-X.bonsai.io/"

  The cluster URL is available via the Bonsai dashboard.

## 官网

- 主页: https://github.com/omc/bonsai-elasticsearch-rails
- 文档: https://www.rubydoc.info/gems/bonsai-elasticsearch-rails/7.0.1
- RubyGems: https://rubygems.org/gems/bonsai-elasticsearch-rails

## 历史版本号

- 7.0.1 (2018-08-11)
- 6.0.0 (2018-08-11)
- 5.0.0 (2018-08-11)
- 2.0.0 (2018-08-11)
- 1.0.0 (2018-08-11)
- 0.3.0 (2018-08-11)
- 0.2.0 (2016-10-27)
- 0.1.0 (2016-09-06)
- 0.0.4 (2014-04-02)
- 0.0.2 (2014-04-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/bonsai-elasticsearch-rails
- gem 安装: `gem install bonsai-elasticsearch-rails`
- Bundler: `gem "bonsai-elasticsearch-rails"`
- 最新版本: 7.0.1
- 最新版归档: https://rubygems.org/downloads/bonsai-elasticsearch-rails-7.0.1.gem
- 版本锁定: `gem "bonsai-elasticsearch-rails", "~> 7.0.1"`
- 中央仓库: https://rubygems.org/
