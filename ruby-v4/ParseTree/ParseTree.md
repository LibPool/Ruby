# ParseTree

**Tag**: testing

## 简介

ParseTree is a C extension (using RubyInline) that extracts the parse
tree for an entire class or a specific method and returns it as a
s-expression (aka sexp) using ruby's arrays, strings, symbols, and
integers.

As an example:

  def conditional1(arg1)
    if arg1 == 0 then
      return 1
    end
    return 0
  end

becomes:

  [:defn,
    :conditional1,
    [:scope,
     [:block,
      [:args, :arg1],
      [:if,
       [:call, [:lvar, :arg1], :==, [:array, [:lit, 0]]],
       [:return, [:lit, 1]],
       nil],
      [:return, [:lit, 0]]]]]

## 官网

- 主页: https://github.com/seattlerb/parsetree
- RubyGems: https://rubygems.org/gems/ParseTree

## 历史版本号

- 3.0.9 (2012-05-01)
- 3.0.8 (2011-09-27)
- 3.0.7 (2011-02-18)
- 3.0.6 (2010-09-01)
- 3.0.5 (2010-03-28)
- 3.0.4 (2009-08-05)
- 1.3.6 (2009-07-25)
- 1.3.5 (2009-07-25)
- 1.3.4 (2009-07-25)
- 1.3.3 (2009-07-25)
- 1.3.2 (2009-07-25)
- 1.3.0 (2009-07-25)
- 1.2.0 (2009-07-25)
- 1.1.1 (2009-07-25)
- 1.1.0 (2009-07-25)
- 1.7.0 (2009-07-25)
- 1.6.4 (2009-07-25)
- 1.6.3 (2009-07-25)
- 1.6.2 (2009-07-25)
- 1.6.1 (2009-07-25)
- 1.6.0 (2009-07-25)
- 1.5.0 (2009-07-25)
- 1.4.1 (2009-07-25)
- 1.4.0 (2009-07-25)
- 1.3.7 (2009-07-25)
- 2.1.1 (2009-07-25)
- 2.1.0 (2009-07-25)
- 2.0.2 (2009-07-25)
- 2.0.1 (2009-07-25)
- 2.0.0 (2009-07-25)
- 1.7.1 (2009-07-25)
- 3.0.1-x86-mingw32 (2009-07-25)
- 3.0.0 (2009-07-25)
- 2.2.0 (2009-07-25)
- 3.0.3-x86-mswin32-60 (2009-07-25)
- 3.0.3-x86-mingw32 (2009-07-25)
- 3.0.3 (2009-07-25)
- 3.0.2-x86-mswin32-60 (2009-07-25)
- 3.0.2-x86-mingw32 (2009-07-25)
- 3.0.2 (2009-07-25)
- 3.0.1-x86-mswin32-60 (2009-07-25)
- 3.0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/ParseTree
- gem 安装: `gem install ParseTree`
- Bundler: `gem "ParseTree"`
- 最新版本: 3.0.9
- 最新版归档: https://rubygems.org/downloads/ParseTree-3.0.9.gem
- 版本锁定: `gem "ParseTree", "~> 3.0.9"`
- 中央仓库: https://rubygems.org/
