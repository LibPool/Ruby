# factory_boy

**Tag**: web, database, testing, data

## 简介

Version 2.0.2 is compatible with ActiveRecord < 3.1      
      Version 2.0.3+ is compatible with ActiveRecord >= 3.1     
      ------
      Factory Girl with database accesses stubbed.
      The versions 2+ only work with Rails 3 (AR 3+) for stubbing queries.
      Now handle Rails 3 (only Rails 3) queries stubbing,
      Transform rail3 queries into ruby select on Plants created with factory boy.
      Example
      user = Plant(:user => 'toto', :addresses => [Plant(:address, :street => 'here')])
      User.where(:name => 'toto').where('addresses.street = 'here').joins(:addresses) will be stubbed into
      a select ruby on plants and return here, user.
      See more on github and in unit tests.
      Compatible ruby 1.9.3.

## 官网

- 主页: http://github.com/anoiaque/factory_boy
- 源码仓库: https://github.com/anoiaque/factory_boy
- 问题追踪: https://github.com/anoiaque/factory_boy/issues
- RubyGems: https://rubygems.org/gems/factory_boy

## 历史版本号

- 2.0.3 (2012-10-14)
- 2.0.2 (2011-04-29)
- 2.0.1 (2011-01-23)
- 2.0.0 (2011-01-23)
- 1.0.5 (2010-10-21)
- 1.0.4 (2010-10-06)
- 1.0.3 (2010-10-06)
- 1.0.2 (2010-10-06)
- 1.0.1 (2010-10-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/factory_boy
- gem 安装: `gem install factory_boy`
- Bundler: `gem "factory_boy"`
- 最新版本: 2.0.3
- 最新版归档: https://rubygems.org/downloads/factory_boy-2.0.3.gem
- 版本锁定: `gem "factory_boy", "~> 2.0.3"`
- 中央仓库: https://rubygems.org/
