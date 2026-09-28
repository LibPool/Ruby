# container-backup

**Tag**: database, template, filesystem, data

## 简介

labels:
      - "backup={volumes: [mongo_data],databases: [mongo: {user: ${MONGO_INITDB_ROOT_USERNAME}, password: ${MONGO_INITDB_ROOT_PASSWORD}}]}"
      - "backup={volumes: [influxdb_data],databases: [influxdb: {user: ${INFLUXDB_ADMIN_USER},password: ${INFLUXDB_ADMIN_PASSWORD}}]}"
      - "backup={volumes: [chronograf_data],databases: [chronograf]}"
      - "backup={directories: [/var/www/html/libraries, /var/www/html/modules, /var/www/html/profiles, /var/www/html/themes, /var/www/html/sites]}"
      - "backup={volumes: [drupal_mysql_data],databases: [mysql: {db: ${MYSQL_DATABASE},password: ${MYSQL_ROOT_PASSWORD},user: root}]}"

## 官网

- 主页: https://github.com/mpantel/container-backup
- RubyGems: https://rubygems.org/gems/container-backup

## 历史版本号

- 0.1.0 (2020-10-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/container-backup
- gem 安装: `gem install container-backup`
- Bundler: `gem "container-backup"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/container-backup-0.1.0.gem
- 版本锁定: `gem "container-backup", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
