# constrain

**Tag**: filesystem

## 简介

Allows you check if an object match a class expression. It is typically
    used to check the type of method paraameters. It is an alternative to using
    Ruby-3 .rbs files but with a different syntax and only dynamic checks
    
    Typically you'll include the Constrain module and use #constrain to check
    the type of method parameters:

      include Constrain

      # f takes a String and an array of Integer objects. Raise a Constrain::Error
      # if parameters doesn't have the expected types
      def f(a, b)
        constrain a, String
        constrain b, [Integer]
      end

    Constrain works with ruby-2 (and maybe ruby-3)

## 官网

- 主页: https://github.com/clrgit/constrain/
- RubyGems: https://rubygems.org/gems/constrain

## 历史版本号

- 0.10.0 (2023-12-18)
- 0.9.0 (2023-01-21)
- 0.8.0 (2022-09-17)
- 0.7.0 (2022-09-03)
- 0.6.0 (2022-07-20)
- 0.5.1 (2022-03-06)
- 0.5.0 (2022-03-06)
- 0.4.0 (2022-03-03)
- 0.3.3 (2022-01-21)
- 0.3.2 (2021-10-24)
- 0.3.1 (2021-10-24)
- 0.3.0 (2021-09-20)
- 0.2.2 (2021-05-24)
- 0.2.1 (2021-05-22)
- 0.2.0 (2021-05-22)
- 0.1.3 (2021-05-17)
- 0.1.2 (2021-05-17)
- 0.1.1 (2021-05-16)
- 0.1.0 (2021-05-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/constrain
- gem 安装: `gem install constrain`
- Bundler: `gem "constrain"`
- 最新版本: 0.10.0
- 最新版归档: https://rubygems.org/downloads/constrain-0.10.0.gem
- 版本锁定: `gem "constrain", "~> 0.10.0"`
- 中央仓库: https://rubygems.org/
