# rails-backup-migrate

**Tag**: web, filesystem

## 简介

Creates a directory db/backup in the rails app and creates / loads YML files from there. 
    After a backup, the db/backups directory is archived into a .tgz file and then deleted.
    When restoring, the db/backup directory is extracted from the .tgz file.
    All of the files in the 'files' directory are also backed up / restored.
    
    The default archive file is "site-backup.tgz" but any other one can be passed as an argument to both db:backup:write
    and db:backup:read, for example:
    
    app1$ rake db:backup:write
    app1$ cd ../app2
    app2$ rake db:backup:read[../app1/site-backup.tgz]
    
    The environment variable 'verbose' or 'VERBOSE' if defined will result in some verbose output.
    
    To add the rake tasks to your Rails app, simply install the gem, and then add the following line to your 'Rakefile':
    
        require 'rails-backup-migrate'

## 官网

- 主页: http://github.com/mattconnolly/rails-backup-migrate
- RubyGems: https://rubygems.org/gems/rails-backup-migrate

## 历史版本号

- 0.0.12 (2012-05-07)
- 0.0.11 (2012-03-22)
- 0.0.10 (2011-12-13)
- 0.0.9 (2011-08-18)
- 0.0.8 (2011-07-25)
- 0.0.7 (2011-07-17)
- 0.0.6 (2011-06-30)
- 0.0.5 (2011-06-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails-backup-migrate
- gem 安装: `gem install rails-backup-migrate`
- Bundler: `gem "rails-backup-migrate"`
- 最新版本: 0.0.12
- 最新版归档: https://rubygems.org/downloads/rails-backup-migrate-0.0.12.gem
- 版本锁定: `gem "rails-backup-migrate", "~> 0.0.12"`
- 中央仓库: https://rubygems.org/
