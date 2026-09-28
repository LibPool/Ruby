# moj_tribunals_config

**Tag**: web, testing, filesystem

## 简介

Used by tribunals_frontend and tribunals_api to share configuration.
    To use:

    1) add "gem 'moj_tribunals_config'" to your Gemfile
    2) in an initializer, add the following code:

      require 'moj_tribunals_config'

      my_config = Moj::Tribunals::ConfigLoader.new.load

    This will load the default config files from the gem.


    To load different files, you can provide an alternative path
    to the ConfigLoader.new method, e.g.

      my_config = Moj::Tribunals::ConfigLoader.new('/my/alternative/config/path').load

    To just load config for a specific tribunal, you can do:

      config_loader = Moj::Tribunals::ConfigLoader.new
      config_file = config_loader.config_file_for('utiac')
      config_loader.load_file( config_file )

    RailsConfig integration
    =======================

    If you're using the RailsConfig gem, your intializer can just do something like:

    files = Moj::Tribunals::ConfigLoader.new.config_files
    files.each{ |f| Settings.add_source!( f ) }
    Settings.reload!

## 官网

- 主页: http://github.com/aldavidson/moj_tribunals_config
- 文档: https://www.rubydoc.info/gems/moj_tribunals_config/1.6.0
- RubyGems: https://rubygems.org/gems/moj_tribunals_config

## 历史版本号

- 1.6.0 (2015-03-05)
- 1.5.2 (2015-02-25)
- 1.5.1 (2015-02-18)
- 1.5.0 (2015-02-10)
- 1.4.0 (2015-02-06)
- 1.3.0 (2015-02-03)
- 1.2.0 (2015-02-03)
- 1.0.0 (2015-02-03)
- 0.8.0 (2015-02-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/moj_tribunals_config
- gem 安装: `gem install moj_tribunals_config`
- Bundler: `gem "moj_tribunals_config"`
- 最新版本: 1.6.0
- 最新版归档: https://rubygems.org/downloads/moj_tribunals_config-1.6.0.gem
- 版本锁定: `gem "moj_tribunals_config", "~> 1.6.0"`
- 中央仓库: https://rubygems.org/
