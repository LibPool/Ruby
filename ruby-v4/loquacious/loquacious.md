# loquacious

**Tag**: filesystem

## 简介

Descriptive configuration files for Ruby written in Ruby.

Loquacious provides a very open configuration system written in ruby and
descriptions for each configuration attribute. The attributes and descriptions
can be iterated over allowing for helpful information about those attributes to
be displayed to the user.

In the simple case we have a file something like

  Loquacious.configuration_for('app') {
    name 'value', :desc => "Defines the name"
    foo  'bar',   :desc => "FooBar"
    id   42,      :desc => "Ara T. Howard"
  }

Which can be loaded via the standard Ruby loading mechanisms

  Kernel.load 'config/app.rb'

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

  config = Loquacious.configuration_for('nested')

  p config.a.b.c  #=> "value"

And as you can see, descriptions can either be given inline after the value or
they can appear above the attribute and value on their own line.

## 官网

- 主页: http://rubygems.org/gems/loquacious
- 源码仓库: http://github.com/TwP/loquacious
- 问题追踪: http://github.com/TwP/loquacious/issues
- RubyGems: https://rubygems.org/gems/loquacious

## 历史版本号

- 1.9.1 (2011-12-16)
- 1.9.0 (2011-09-13)
- 1.8.1 (2011-06-09)
- 1.8.0 (2011-06-03)
- 1.7.1 (2011-02-12)
- 1.7.0 (2010-08-16)
- 1.6.4 (2010-06-08)
- 1.6.3 (2010-06-08)
- 1.6.2 (2010-06-01)
- 1.6.1 (2010-05-19)
- 1.6.0 (2010-05-18)
- 1.5.2 (2010-04-06)
- 1.5.1 (2010-04-06)
- 1.5.0 (2010-03-11)
- 1.4.2 (2010-02-02)
- 1.4.1 (2009-11-29)
- 1.4.0 (2009-11-08)
- 1.3.1 (2009-10-30)
- 1.2.0 (2009-07-25)
- 1.1.1 (2009-07-25)
- 1.1.0 (2009-07-25)
- 1.0.0 (2009-07-25)
- 1.3.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/loquacious
- gem 安装: `gem install loquacious`
- Bundler: `gem "loquacious"`
- 最新版本: 1.9.1
- 最新版归档: https://rubygems.org/downloads/loquacious-1.9.1.gem
- 版本锁定: `gem "loquacious", "~> 1.9.1"`
- 中央仓库: https://rubygems.org/
