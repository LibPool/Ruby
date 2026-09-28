# ruby_parser

**Tag**: testing, tooling, filesystem

## 简介

ruby_parser (RP) is a ruby parser written in pure ruby (utilizing
racc--which does by default use a C extension). It outputs
s-expressions which can be manipulated and converted back to ruby via
the ruby2ruby gem.

As an example:

    def conditional1 arg1
      return 1 if arg1 == 0
      return 0
    end

becomes:

    s(:defn, :conditional1, s(:args, :arg1),
      s(:if,
        s(:call, s(:lvar, :arg1), :==, s(:lit, 0)),
        s(:return, s(:lit, 1)),
        nil),
      s(:return, s(:lit, 0)))

Tested against 801,039 files from the latest of all rubygems (as of 2013-05):

* 1.8 parser is at 99.9739% accuracy, 3.651 sigma
* 1.9 parser is at 99.9940% accuracy, 4.013 sigma
* 2.0 parser is at 99.9939% accuracy, 4.008 sigma
* 2.6 parser is at 99.9972% accuracy, 4.191 sigma
* 3.0 parser has a 100% parse rate.
  * Tested against 2,672,412 unique ruby files across 167k gems.
  * As do all the others now, basically.

## 官网

- 主页: https://github.com/seattlerb/ruby_parser
- 问题追踪: https://github.com/seattlerb/ruby_parser/issues
- RubyGems: https://rubygems.org/gems/ruby_parser

## 历史版本号

- 3.22.0 (2025-12-21)
- 3.21.1 (2024-07-09)
- 3.21.0 (2024-01-16)
- 3.20.3 (2023-07-12)
- 3.20.2 (2023-06-06)
- 3.20.1 (2023-05-17)
- 3.20.0 (2023-03-04)
- 3.19.2 (2022-12-03)
- 3.19.1 (2022-04-06)
- 3.19.0 (2022-03-30)
- 3.18.1 (2021-11-10)
- 3.18.0 (2021-10-28)
- 3.17.0 (2021-08-04)
- 3.16.0 (2021-05-15)
- 3.15.1 (2021-01-11)
- 3.15.0 (2020-09-01)
- 3.14.2 (2020-02-07)
- 3.14.1 (2019-10-30)
- 3.14.0 (2019-09-25)
- 3.13.1 (2019-03-26)
- 3.13.0 (2019-03-13)
- 3.12.0 (2018-12-04)
- 3.11.0 (2018-02-15)
- 3.10.1 (2017-07-21)
- 3.10.0 (2017-07-17)
- 3.9.0 (2017-04-14)
- 3.8.4 (2017-01-13)
- 3.8.3 (2016-10-09)
- 3.8.2 (2016-05-05)
- 3.8.1 (2016-02-19)
- 3.8.0 (2016-02-19)
- 3.7.3 (2016-01-22)
- 3.7.2 (2015-10-26)
- 3.7.1 (2015-08-06)
- 3.7.0 (2015-05-28)
- 3.6.6 (2015-04-13)
- 3.6.5 (2015-03-12)
- 3.6.4 (2015-01-17)
- 3.6.3 (2014-09-27)
- 3.6.2 (2014-07-18)
- 3.6.1 (2014-05-12)
- 3.6.0 (2014-04-23)
- 3.5.0 (2014-03-25)
- 3.4.1 (2014-02-14)
- 3.4.0 (2014-02-05)
- 3.3.0 (2014-01-15)
- 3.2.2 (2013-07-12)
- 3.2.1 (2013-07-03)
- 3.2.0 (2013-07-03)
- 3.1.3 (2013-04-10)
- 3.1.2 (2013-03-18)
- 3.1.1 (2012-12-19)
- 3.1.0 (2012-12-07)
- 3.0.4 (2012-11-26)
- 3.0.3 (2012-11-23)
- 3.0.2 (2012-11-21)
- 3.0.1 (2012-11-03)
- 3.0.0 (2012-11-02)
- 3.0.0.a10 (2012-10-26)
- 3.0.0.a9 (2012-10-22)
- 3.0.0.a8 (2012-09-26)
- 3.0.0.a7 (2012-09-21)
- 3.0.0.a6 (2012-08-20)
- 3.0.0.a5 (2012-08-01)
- 3.0.0.a4 (2012-07-26)
- 3.0.0.a3 (2012-07-04)
- 3.0.0.a2 (2012-06-19)
- 3.0.0.a1 (2012-05-23)
- 2.3.1 (2011-09-22)
- 2.3.0 (2011-09-06)
- 2.2.0 (2011-08-23)
- 2.1.0 (2011-08-15)
- 2.0.6 (2011-02-19)
- 2.0.5 (2010-09-01)
- 2.0.4 (2009-08-20)
- 2.0.3 (2009-08-05)
- 2.0.2 (2009-07-25)
- 2.0.1 (2009-07-25)
- 2.0.0 (2009-07-25)
- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/ruby_parser
- gem 安装: `gem install ruby_parser`
- Bundler: `gem "ruby_parser"`
- 最新版本: 3.22.0
- 最新版归档: https://rubygems.org/downloads/ruby_parser-3.22.0.gem
- 版本锁定: `gem "ruby_parser", "~> 3.22.0"`
- 中央仓库: https://rubygems.org/
