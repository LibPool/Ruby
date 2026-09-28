# yard-heuristics

**Tag**: web, cli, database, testing, security, networking, template, filesystem

## 简介

YARD-Heuristics

  YARD-Heuristics heuristically determines types of parameters and return
  values for YARD documentation that doesnΓÇÖt explicitly document it.  This
  allows you to write documentation that isnΓÇÖt adorned with ΓÇ£obviousΓÇ¥ types,
  but still get that information into the output.  It also lets you
  nice-looking references to parameters and have them be marked up
  appropriately in HTML output.

┬º Heuristics

    The following sections list the various heuristics that YARD-Heuristics
    apply for determining types of parameters and return values.

    Note that for all heuristics, a type will only be added if none already
    exists.

  ┬º Parameter Named ΓÇ£otherΓÇ¥

      A parameter named ΓÇ£otherΓÇ¥ has the same type as the receiver.  This turns

        class Point
          def ==(other)

      into

        class Point
          # @param [Point] other
          def ==(other)

  ┬º Parameter Types Derived by Parameter Name

      Parameters to a method with names in the following table has the type
      listed on the same row.

    | Name   | Type      |
    |--------+-----------|
    | index  | [Integer] |
    | object | [Object]  |
    | range  | [Range]   |
    | string | [String]  |

      Thus

        class Point
          def x_inside?(range)

      becomes

        class Point
          # @param [Range] range
          def x_inside?(range)

  ┬º Block Parameters

      If the last parameter to a methodΓÇÖs name begins with ΓÇÿ&ΓÇÖ it has the type
      [Proc].

        class Method
          def initialize(&block)

      becomes

        class Method
          # @param [Block] block
          def initialize(&block)

  ┬º Return Types by Method Name

      For the return type of a method with less than two ΓÇ╣@returnΓÇ║ tags, the
      method name is lookup up in the following table and has the type listed on
      the same row. For the ΓÇ£typeΓÇ¥ ΓÇ£self or typeΓÇ¥, if a ΓÇ╣@paramΓÇ║ tag exists with
      the name ΓÇ£otherΓÇ¥, the type of the receiver is used, otherwise ΓÇ£selfΓÇ¥ is
      used.  For the ΓÇ£typeΓÇ¥ ΓÇ£typeΓÇ¥, the type of the receiver is used.

    | Name            | Type           |
    |-----------------+----------------|
    | ΓÇ╣<<ΓÇ║            | self or type   |
    | ΓÇ╣>>ΓÇ║            | self or type   |
    | ΓÇ╣==ΓÇ║            | [Boolean]      |
    | ΓÇ╣===ΓÇ║           | [Boolean]      |
    | ΓÇ╣=~ΓÇ║            | [Boolean]      |
    | ΓÇ╣<=>ΓÇ║           | [Integer, nil] |
    | ΓÇ╣+ΓÇ║             | type           |
    | ΓÇ╣-ΓÇ║             | type           |
    | ΓÇ╣*ΓÇ║             | type           |
    | ΓÇ╣/ΓÇ║             | type           |
    | each            | [self]         |
    | each_with_index | [self]         |
    | hash            | [Integer]      |
    | inspect         | [String]       |
    | length          | [Integer]      |
    | size            | [Integer]      |
    | to_s            | [String]       |
    | to_str          | [String]       |


      Thus

        class Point
          def <<(other)

      becomes

        class Point
          # @return [Point]
          def <<(other)

      but

        class List
          def <<(item)

      becomes

        class List
          # @return [self]
          def <<(item)

┬º Emphasizing Parameter Names

    When producing HTML output, any words in all uppercase, with a possible
    ΓÇ£thΓÇ¥ suffix, that is also the name of a parameter, an ΓÇ╣@optionΓÇ║, or a
    ΓÇ╣@yieldparamΓÇ║, will be downcased and emphasized with a class of
    ΓÇ£parameterΓÇ¥.

    In the following example, ΓÇ£OTHERΓÇ¥ will be turned into
    ΓÇ╣<em class="parameter">other</em>ΓÇ║:

      class Point
        # @return True if the receiverΓÇÖs class and {#x} and {#y} `#==` those of
        #   OTHER
        def ==(other)

┬º Usage

    Add ΓÇ╣--plugin yard-heuristics-1.0ΓÇ║ to your YARD command line.  If youΓÇÖre
    using Inventory-Rake-Tasks-YARD┬╣, add the following to your Rakefile:

      Inventory::Rake::Tasks::YARD.new do |t|
        t.options += %w'--plugin yard-heuristics-1.0'
      end

┬╣ See http://disu.se/software/inventory-rake-tasks-yard/

┬º API

    ThereΓÇÖs really not very much to the YARD-Heuristics API.  What you can do
    is add (or modify) the types of parameters and return types of methods by
    adding (or modifying) entries in the Hash tables
    ΓÇ╣YARDHeuristics::ParamTypesΓÇ║ and ΓÇ╣YARDHeuristics::ReturnTypesΓÇ║
    respectively.  ThatΓÇÖs about it.

┬º Financing

    Currently, most of my time is spent at my day job and in my rather busy
    private life.  Please motivate me to spend time on this piece of software
    by donating some of your money to this project.  Yeah, I realize that
    requesting money to develop software is a bit, well, capitalistic of me.
    But please realize that I live in a capitalistic society and I need money
    to have other people give me the things that I need to continue living
    under the rules of said society.  So, if you feel that this piece of
    software has helped you out enough to warrant a reward, please PayPal a
    donation to now@disu.se┬╣.  Thanks!  Your support wonΓÇÖt go unnoticed!

┬╣ Send a donation:
  https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=now@disu.se&item_name=YARD-Heuristics

┬º Reporting Bugs

    Please report any bugs that you encounter to the {issue tracker}┬╣.

  ┬╣ See https://github.com/now/yard-heuristics/issues

┬º Authors

    Nikolai Weibull wrote the code, the tests, and this README.

┬º Licensing

    YARD-Heuristics is free software: you may redistribute it and/or modify it
    under the terms of the {GNU Lesser General Public License, version 3}┬╣ or
    later┬▓, as published by the {Free Software Foundation}┬│.

┬╣ See http://disu.se/licenses/lgpl-3.0/
┬▓ See http://gnu.org/licenses/
┬│ See http://fsf.org/

## 官网

- 主页: http://disu.se/software/yard-heuristics/
- 文档: https://www.rubydoc.info/gems/yard-heuristics/1.2.2
- RubyGems: https://rubygems.org/gems/yard-heuristics

## 历史版本号

- 1.2.2 (2013-09-05)
- 1.2.1 (2013-05-14)
- 1.2.0 (2013-04-30)
- 1.1.0 (2012-08-03)
- 1.0.1 (2012-05-03)
- 1.0.0 (2012-05-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/yard-heuristics
- gem 安装: `gem install yard-heuristics`
- Bundler: `gem "yard-heuristics"`
- 最新版本: 1.2.2
- 最新版归档: https://rubygems.org/downloads/yard-heuristics-1.2.2.gem
- 版本锁定: `gem "yard-heuristics", "~> 1.2.2"`
- 中央仓库: https://rubygems.org/
