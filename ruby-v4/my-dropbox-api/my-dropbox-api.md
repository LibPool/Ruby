# my-dropbox-api

**Tag**: web, database, networking, tooling, filesystem, data

## 简介

The **dropbox-api** is a Ruby gem for managing DropBox uploading, downloading and sharing DropBox files and folders.

The main goals of building this gem are:
  
1. Simulate a **permanent access token**, since [Dropbox is moving to "short-term live access codes"](https://www.dropboxforum.com/t5/Discuss-Dropbox-Developer-API/Permanent-access-token/td-p/592644);
  
2. Manage DropBox as an elastic-storage providers for [our SaaS projects](https://github.com/leandrosardi/mysaas), allowing us to upload, download and share download links to files;
  
3. Backup and restore secret files of our projects that cannot be commited into the source code repository (E.g.: database passwords, SSL certificates, private keys).

## 官网

- 主页: https://github.com/leandrosardi/my-dropbox-api
- 文档: https://www.rubydoc.info/gems/my-dropbox-api/1.0.3
- RubyGems: https://rubygems.org/gems/my-dropbox-api

## 历史版本号

- 1.0.3 (2025-03-18)
- 1.0.2 (2024-03-30)
- 1.0.1 (2023-04-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/my-dropbox-api
- gem 安装: `gem install my-dropbox-api`
- Bundler: `gem "my-dropbox-api"`
- 最新版本: 1.0.3
- 最新版归档: https://rubygems.org/downloads/my-dropbox-api-1.0.3.gem
- 版本锁定: `gem "my-dropbox-api", "~> 1.0.3"`
- 中央仓库: https://rubygems.org/
