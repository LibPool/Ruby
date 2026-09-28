# value

**Tag**: web, database, testing, security, networking, filesystem

## 简介

Value

  Value is a library for defining immutable value objects in Ruby.  A value
  object is an object whose equality to other objects is determined by its
  value, not its identity, think dates and amounts of money.  A value object
  should also be immutable, as you donΓÇÖt want the date ΓÇ£2013-04-22ΓÇ¥ itself to
  change but the current date to change from ΓÇ£2013-04-22ΓÇ¥ to ΓÇ£2013-04-23ΓÇ¥.
  That is, you donΓÇÖt want entries in a calendar for 2013-04-22 to move to
  2013-04-23 simply because the current date changes from 2013-04-22 to
  2013-04-23.

  A value object consists of one or more attributes stored in instance
  variables.  Value sets up an #initialize method for you that letΓÇÖs you set
  these attributes, as, value objects being immutable, thisΓÇÖll be your only
  chance to do so.  Value also adds equality checks ΓÇ╣#==ΓÇ║ and ΓÇ╣#eql?ΓÇ║ (which
  are themselves equivalent), a ΓÇ╣#hashΓÇ║ method, a nice ΓÇ╣#inspectΓÇ║ method, and a
  protected attribute reader for each attribute.  You may of course add any
  additional methods that your value object will benefit from.

  ThatΓÇÖs basically all thereΓÇÖs too it.  LetΓÇÖs now look at using the Value
  library.

┬º Usage

    You create value object class by invoking ΓÇ╣#ValueΓÇ║ inside the class
    (module) you wish to make into a value object class.  LetΓÇÖs create a class
    that represent points on a plane:

      class Point
        Value :x, :y
      end

    A ΓÇ╣PointΓÇ║ is thus a value object consisting of two sub-values ΓÇ╣xΓÇ║ and ΓÇ╣yΓÇ║
    (the coordinates).  Just from invoking ΓÇ╣#ValueΓÇ║, a ΓÇ╣PointΓÇ║ object will have
    a constructor that takes two arguments to set instance variables ΓÇ╣@xΓÇ║ and
    ΓÇ╣@yΓÇ║, equality checks ΓÇ╣#==ΓÇ║ and ΓÇ╣#eql?ΓÇ║ (which are the same), a ΓÇ╣#hashΓÇ║
    method, a nice ΓÇ╣#inspectΓÇ║ method, and two protected attribute readers ΓÇ╣#xΓÇ║
    and ΓÇ╣#yΓÇ║.  We can thus already creat ΓÇ╣PointΓÇ║s:

      origo = Point.new(0, 0)

    The default of making the attribute readers protected is often good
    practice, but for a ΓÇ╣PointΓÇ║ it probably makes sense to be able to access
    its coordinates:

      class Point
        public(*attributes)
      end

    ThisΓÇÖll make all attributes of ΓÇ╣PointΓÇ║ public.  You can of course choose to
    only make certain attributes public:

      class Point
        public :x
      end

    Note that this public is standard Ruby functionality.  Adding a method to
    ΓÇ╣PointΓÇ║ is of course also possible and very much Rubyish:

      class Point
        def distance(other)
          Math.sqrt((other.x - x)**2 + (other.y - y)**2)
        end
      end

    For some value object classes you might want to support optional
    attributes.  This is done by providing a default value for the attribute,
    like so:

      class Money
        Value :amount, [:currency, :USD]
      end

    Here, the ΓÇ╣currencyΓÇ║ attribute will default to ΓÇ╣:USDΓÇ║.  You can create
    ΓÇ╣MoneyΓÇ║ via

      dollars = Money.new(2)

    but also

      kronor = Money.new(2, :SEK)

    All required attributes must come before any optional attributes.

    Splat attributes are also supported:

      class List
        Value :'*elements'
      end

      empty = List.new
      suits = List.new(:spades, :hearts, :diamonds, :clubs)

    Splat attributes are optional.

    Finally, block attributes are also available:

      class Block
        Value :'&block'
      end

      block = Block.new{ |e| e * 2 }

    Block attributes are optional.

    Comparison beyond ΓÇ╣#==ΓÇ║ is possible by specifingy the ΓÇ╣:comparableΓÇ║ option
    to ΓÇ╣#ValueΓÇ║, listing one or more attributes that should be included in the
    comparison:

      class Vector
        Value :a, :b, :comparable => :a
      end

    Note that equality (ΓÇ╣#==ΓÇ║ and ΓÇ╣#eql?ΓÇ║) is always defined based on all
    attributes, regardless of arguments to ΓÇ╣:comparableΓÇ║.

    Here we say that comparisons between ΓÇ╣VectorΓÇ║s should be made between the
    values of the ΓÇ╣aΓÇ║ attribute only.  We can also make comparisons between all
    attributes of a value object:

      class Vector
        Value :a, :b, :comparable => true
      end

    To sum things up, letΓÇÖs use all possible arguments to ΓÇ╣#ValueΓÇ║ at once:

      class Method
        Value :file, :line, [:name, 'unnamed'], :'*args', :'&block',
              :comparable => [:file, :line]
      end

    A ΓÇ╣MethodΓÇ║ consists of file and line information, a possible name, some
    arguments, possibly a block, and is comparable on the file and line on
    which they appear.

    Check out the {full API documentation}┬╣ for a more explicit description,
    should you need it or should you want to extend it.

┬╣ See http://disu.se/software/value/api/

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
  https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=now%40disu%2ese&item_name=Value

┬º Reporting Bugs

    Please report any bugs that you encounter to the {issue tracker}┬╣.

  ┬╣ See https://github.com/now/value/issues

┬º Authors

    Nikolai Weibull wrote the code, the tests, the manual pages, and this
    README.

┬º Licensing

    Value is free software: you may redistribute it and/or modify it under the
    terms of the {GNU Lesser General Public License, version 3}┬╣ or later┬▓, as
    published by the {Free Software Foundation}┬│.

┬╣ See http://disu.se/licenses/lgpl-3.0/
┬▓ See http://gnu.org/licenses/
┬│ See http://fsf.org/

## 官网

- 主页: http://disu.se/software/value
- 文档: https://www.rubydoc.info/gems/value/1.1.3
- RubyGems: https://rubygems.org/gems/value

## 历史版本号

- 1.1.3 (2013-09-04)
- 1.1.2 (2013-04-30)
- 1.1.1 (2012-05-04)
- 1.1.0 (2012-04-26)
- 1.0.1 (2012-04-25)
- 1.0.0 (2012-04-25)
- 0.2.0 (2012-04-23)
- 0.1.0 (2011-09-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/value
- gem 安装: `gem install value`
- Bundler: `gem "value"`
- 最新版本: 1.1.3
- 最新版归档: https://rubygems.org/downloads/value-1.1.3.gem
- 版本锁定: `gem "value", "~> 1.1.3"`
- 中央仓库: https://rubygems.org/
