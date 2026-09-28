# ifelse

**Tag**: testing

## 简介

IfElse is an implementation of the pure object-oriented conditional syntax
found in languages of the SmallTalk family, including Self.  Those languages
distinguish themselves by taking the "everything is an object / everything
is a method" approach to a further extreme than Ruby, and getting rid of
almost all cases of special syntax other than object definition and method
call.

Ruby, of course, already works this way for some purposes -- thus most Ruby
developers prefer to write

  [1, 17, 39].each {|x| puts x}

rather than

  for x in [1, 17, 39]
    puts x
  end

and

  3.times {|n| puts n}

instead of

  i = 1
  while i <= 3
    puts i
    i += 1
  end

This module extends that same preference to conditional statements,
providing replacements for the Ruby keywords +if+, and +unless+:

  x = 1
  (x >= 0).if {puts 'positive'}
  (x < 0).unless {puts 'positive'}

Note that as with the built-in special forms these methods replace, these
methods are available on any Ruby Object, and obey the usual rules of which
values are considered "Truthy" and "Falsey".

<b>Note that the primary purpose of this gem is to demonstrate that the
built-in (special form) versions of conditionals provided with Ruby are
mostly syntactic sugar -- as with the +for+ keyword, there is no real need
for these to be built into the language.  With that said, the gem is
fully tested, has no particular performance penalty (beyond the usual cost
of method dispatch), and should be fully useable in general purpose
code.</b>

<b>Note also that while Smalltalk-family languages also provide an
equivalent to the Ruby +else+ keyword, this depends on the more general
block/lambda capability of those languages, which allow a method to take
multiple blocks as arguments.  This could be imitated with a syntax like:</b>

  # NOT A REAL EXAMPLE
  (x > 42).if then: lambda {|x| :big }, else: lambda {|x| :small}

<b>which is true to the SmallTalk original, but feels less Ruby-ish to me, so I
didn't implement this -- perhaps in a later version.</b>

## 官网

- 主页: https://github.com/jimwise/ifelse
- 文档: https://www.rubydoc.info/gems/ifelse/0.6.0
- RubyGems: https://rubygems.org/gems/ifelse

## 历史版本号

- 0.6.0 (2013-12-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/ifelse
- gem 安装: `gem install ifelse`
- Bundler: `gem "ifelse"`
- 最新版本: 0.6.0
- 最新版归档: https://rubygems.org/downloads/ifelse-0.6.0.gem
- 版本锁定: `gem "ifelse", "~> 0.6.0"`
- 中央仓库: https://rubygems.org/
