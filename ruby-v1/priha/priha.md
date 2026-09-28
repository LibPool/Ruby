# priha

**Tag**: testing, security, filesystem

## 简介

If you are a guy who always find something wrong only after sending a pull requset, Priha will help you because Priha lets you examine files' diff between the parent branch and HEAD of the current branch in a real GitHub pull request. However, DO NOT use Priha for your secret repostitory. Since Priha pushes some commits to another repository on GitHub, it easily cause a security incident, espacially the branch you set for Priha is "public". Also, Priha removes all branches on the repository specified in config, so you MUST create a new repository for this purpose and DO NOT use the existing one.

## 官网

- 主页: https://github.com/5t111111/priha
- 文档: https://www.rubydoc.info/gems/priha/0.1.0
- RubyGems: https://rubygems.org/gems/priha

## 历史版本号

- 0.1.0 (2016-01-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/priha
- gem 安装: `gem install priha`
- Bundler: `gem "priha"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/priha-0.1.0.gem
- 版本锁定: `gem "priha", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
