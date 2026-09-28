# rails-fix-permissions

**Tag**: web, cli, testing, filesystem

## 简介

Sometimes you mess your Rails application Unix permissions and get some annoying errors with git. This gem runs a simple shell script to fix that. Granting 755 permissions to folders and 644 to files, it also ensures that some special files inside the 'bin/' will recive special 755 permissions (bundle, rails, rake and spring) which is pretty much the Rails default. Works with all versions of Ruby on Rails; After install run 'rails-fix-permissions' on terminal inside the application folder to fix. Note that in some cases you may need to run it as superuser with 'sudo'.

## 官网

- 源码仓库: https://github.com/fschuindt/rails-fix-permissions
- 文档: https://www.rubydoc.info/gems/rails-fix-permissions/1.3
- RubyGems: https://rubygems.org/gems/rails-fix-permissions

## 历史版本号

- 1.3 (2014-09-20)
- 1.2 (2014-09-17)
- 1.1 (2014-09-17)
- 1.0 (2014-09-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails-fix-permissions
- gem 安装: `gem install rails-fix-permissions`
- Bundler: `gem "rails-fix-permissions"`
- 最新版本: 1.3
- 最新版归档: https://rubygems.org/downloads/rails-fix-permissions-1.3.gem
- 版本锁定: `gem "rails-fix-permissions", "~> 1.3"`
- 中央仓库: https://rubygems.org/
