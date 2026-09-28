# adhearsion-loquacious

**Tag**: filesystem

## 简介

Descriptive configuration files for Ruby written in Ruby.
    Loquacious provides a very open configuration system written in ruby and descriptions for each configuration attribute.
    The attributes and descriptions can be iterated over allowing for helpful information about those attributes to be displayed to the user.
    In the simple case we have a file something like:
      Loquacious.configuration_for('app') {
        name 'value', :desc => "Defines the name"
        foo  'bar',   :desc => "FooBar"
        id   42,      :desc => "Ara T. Howard"
      }
      Which can be loaded via the standard Ruby loading mechanisms
        load 'config/app.rb'
      The attributes and their descriptions can be printed by using a Help object
        help = Loquacious.help_for('app')
        help.show :values => true        # show the values for the attributes, too
      Descriptions are optional, and configurations can be nested arbitrarily deep.
        Loquacious.configuration_for('nested') {
          desc "The outermost level"
          a {
            desc "One more level in"
            b {
              desc "Finally, a real value"
              c 'value'
            }
          }
        }
        config = Loquacious.configuration_for 'nested'
        p config.a.b.c  #=> "value"
        And as you can see, descriptions can either be given inline after the value or they can appear above the attribute and value on their own line.

## 官网

- 主页: http://rubygems.org/gems/loquacious
- RubyGems: https://rubygems.org/gems/adhearsion-loquacious

## 历史版本号

- 1.9.3 (2012-06-04)
- 1.9.2 (2012-01-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/adhearsion-loquacious
- gem 安装: `gem install adhearsion-loquacious`
- Bundler: `gem "adhearsion-loquacious"`
- 最新版本: 1.9.3
- 最新版归档: https://rubygems.org/downloads/adhearsion-loquacious-1.9.3.gem
- 版本锁定: `gem "adhearsion-loquacious", "~> 1.9.3"`
- 中央仓库: https://rubygems.org/
