# active_record-postgres-constraints

**Tag**: web, database, testing, networking, template, data

## 简介

From http://edgeguides.rubyonrails.org/active_record_migrations.html#types-of-schema-dumps:

      There is however a trade-off: db/schema.rb cannot express database
      specific items such as triggers, stored procedures or check constraints.
      While in a migration you can execute custom SQL statements, the schema
      dumper cannot reconstitute those statements from the database. If you are
      using features like this, then you should set the schema format to :sql.

    No longer is this the case.  You can now use the default schema format
    (:ruby) and still preserve your check constraints.

## 官网

- 主页: https://github.com/on-site/active_record-postgres-constraints
- 文档: https://www.rubydoc.info/gems/active_record-postgres-constraints/0.2.2
- RubyGems: https://rubygems.org/gems/active_record-postgres-constraints

## 历史版本号

- 0.2.2 (2020-04-21)
- 0.2.1 (2020-03-27)
- 0.2.0 (2020-01-21)
- 0.1.5 (2019-03-13)
- 0.1.4 (2018-12-07)
- 0.1.3 (2018-12-07)
- 0.1.2 (2017-03-23)
- 0.1.1 (2017-03-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/active_record-postgres-constraints
- gem 安装: `gem install active_record-postgres-constraints`
- Bundler: `gem "active_record-postgres-constraints"`
- 最新版本: 0.2.2
- 最新版归档: https://rubygems.org/downloads/active_record-postgres-constraints-0.2.2.gem
- 版本锁定: `gem "active_record-postgres-constraints", "~> 0.2.2"`
- 中央仓库: https://rubygems.org/
