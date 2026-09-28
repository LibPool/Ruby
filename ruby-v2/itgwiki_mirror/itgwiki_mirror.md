# itgwiki_mirror

**Tag**: web, database, devops, data

## 简介

Use two scripts, itgwiki_mirror_backup and itgwiki_mirror_deploy, to
    maintain a read-only mirror of ITGwiki. itgwiki_mirror_backup runs
    periodically and automatically on the live instance of ITGwiki to create a
    backup and copy it to the mirror. itgwiki_mirror_deploy runs on the mirror
    and is triggered by itgwiki_mirror_backup, imports and adjusts the backup
    to be read-only, then deploys it on the mirror server. Requires rsync and
    mysqldump.

    IMPORTANT: database user passwords are visible as part of the command used
    to execute the backup and deploy processes. I recommend creating minimally
    empowered user accounts to execute backup and deploy tasks.

## 官网

- 主页: https://github.com/sidewaysmilk/itgwiki_mirror
- RubyGems: https://rubygems.org/gems/itgwiki_mirror

## 历史版本号

- 1.0.4 (2012-01-24)
- 1.0.3 (2012-01-24)
- 1.0.2 (2012-01-24)
- 1.0.1 (2012-01-24)
- 1.0.0 (2012-01-24)
- 1.0.0.pre (2012-01-24)
- 0.1.0.pre (2012-01-24)
- 0.0.26.pre (2012-01-20)
- 0.0.25.pre (2012-01-20)
- 0.0.24.pre (2012-01-20)
- 0.0.23.pre (2012-01-20)
- 0.0.22.pre (2012-01-20)
- 0.0.21.pre (2012-01-20)
- 0.0.20.pre (2012-01-20)
- 0.0.19.pre (2012-01-20)
- 0.0.18.pre (2012-01-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/itgwiki_mirror
- gem 安装: `gem install itgwiki_mirror`
- Bundler: `gem "itgwiki_mirror"`
- 最新版本: 1.0.4
- 最新版归档: https://rubygems.org/downloads/itgwiki_mirror-1.0.4.gem
- 版本锁定: `gem "itgwiki_mirror", "~> 1.0.4"`
- 中央仓库: https://rubygems.org/
