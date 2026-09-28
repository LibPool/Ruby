# base

**Tag**: web, filesystem

## 简介

People love Base classes! They have tons of methods waiting to be used. Just check out `ActiveRecord::Base`'s method list:

    >> ActiveRecord::Base.methods.length
    => 530

But why stop there? Why not have even more methods? In fact, let's put *every method* on one Base class!

So I did. It's called Base. Just subclass it and feel free to directly reference any class method, instance method, or constant defined on any module or class in the system. Like this:

    class Cantaloupe < Base
      def embiggen
        encode64(deflate(SEPARATOR))
      end
    end

    >> Cantaloupe.new.embiggen
    => "eJzTBwAAMAAw\n"

See that `embiggen` method calling `encode64` and `deflate` methods? Those come from the `Base64` and `Zlib` modules. And the `SEPARATOR` constant is defined in `File`. Base don't care where it's defined! Base calls what it wants!

By the way, remember those 530 ActiveRecord methods? That's amateur stuff. Check out Base loaded inside a Rails app:

    >> Base.new.methods.count
    => 6947

It's so badass that it takes *five seconds* just to answer that question! 

Base is just craaazzy! It's the most fearless class in all of Ruby. Base doesn't afraid of anything!

## 官网

- 主页: http://github.com/garybernhardt/raptor
- RubyGems: https://rubygems.org/gems/base

## 历史版本号

- 0.0.2 (2011-09-03)
- 0.0.1 (2011-09-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/base
- gem 安装: `gem install base`
- Bundler: `gem "base"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/base-0.0.2.gem
- 版本锁定: `gem "base", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
