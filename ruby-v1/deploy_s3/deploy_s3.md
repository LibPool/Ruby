# deploy_s3

**Tag**: testing, devops

## 简介

Separate out the deployment concerns from your application by using deploy_s3 to write your latest deployed git hash to s3. Then let your provisioning system (for instance, chef + deploy_revision provider) take care of actually deploying new code. deploy_s3 shows diffs between your current branch and the deployed revision.

## 官网

- 主页: https://github.com/movableink/deploy_s3
- 文档: https://www.rubydoc.info/gems/deploy_s3/0.0.3
- RubyGems: https://rubygems.org/gems/deploy_s3

## 历史版本号

- 0.0.3 (2015-01-13)
- 0.0.2 (2015-01-13)
- 0.0.1 (2015-01-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/deploy_s3
- gem 安装: `gem install deploy_s3`
- Bundler: `gem "deploy_s3"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/deploy_s3-0.0.3.gem
- 版本锁定: `gem "deploy_s3", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
