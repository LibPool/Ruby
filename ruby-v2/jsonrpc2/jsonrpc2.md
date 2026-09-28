# jsonrpc2

**Tag**: web, testing, security, serialization

## 简介

== Description

A Rack compatible JSON-RPC2 server domain specific language (DSL) - allows JSONRPC APIs to be
defined as mountable Rack applications with inline documentation, authentication and type checking.

e.g.

  class Calculator < JSONRPC2::Interface
    title "JSON-RPC2 Calculator"
    introduction "This interface allows basic maths calculations via JSON-RPC2"
    auth_with JSONRPC2::BasicAuth.new({'user' => 'secretword'})

    section 'Simple Ops' do
        desc 'Multiply two numbers'
        param 'a', 'Number', 'a'
        param 'b', 'Number', 'b'
        result 'Number', 'a * b'
        def mul args
          args['a'] * args['b']
        end

        desc 'Add numbers'
        example "Calculate 1 + 1 = 2", :params => { 'a' => 1, 'b' => 1}, :result => 2

        param 'a', 'Number', 'First number'
        param 'b', 'Number', 'Second number'
        optional 'c', 'Number', 'Third number'
        result 'Number', 'a + b + c'
        def sum args
          val = args['a'] + args['b']
          val += args['c'] if args['c']
          val
        end
    end
  end

## 官网

- 主页: http://github.com/livelink/jsonrpc2
- 文档: https://github.com/livelink/jsonrpc2#inline-documentation
- 更新日志: https://github.com/livelink/jsonrpc2/blob/master/CHANGELOG.md
- 问题追踪: https://github.com/livelink/jsonrpc2/issues
- RubyGems: https://rubygems.org/gems/jsonrpc2

## 历史版本号

- 0.3.0 (2023-02-10)
- 0.2.0 (2022-04-14)
- 0.1.1 (2014-01-04)
- 0.1.0 (2014-01-04)
- 0.0.9 (2012-09-03)
- 0.0.8 (2012-09-03)
- 0.0.7 (2012-08-27)
- 0.0.6 (2012-08-24)
- 0.0.5 (2012-07-19)
- 0.0.4 (2012-07-17)
- 0.0.3 (2012-07-17)
- 0.0.2 (2012-07-17)
- 0.0.1 (2012-07-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/jsonrpc2
- gem 安装: `gem install jsonrpc2`
- Bundler: `gem "jsonrpc2"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/jsonrpc2-0.3.0.gem
- 版本锁定: `gem "jsonrpc2", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
