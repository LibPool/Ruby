# fabiokung-ruby_parser

**Tag**: tooling

## 简介

ruby_parser (RP) is a ruby parser written in pure ruby (utilizing racc--which does by default use a C extension). RP's output is the same as ParseTree's output: s-expressions using ruby's arrays and base types.  As an example:  def conditional1(arg1) if arg1 == 0 then return 1 end return 0 end  becomes:  s(:defn, :conditional1, s(:args, :arg1), s(:scope, s(:block, s(:if, s(:call, s(:lvar, :arg1), :==, s(:arglist, s(:lit, 0))), s(:return, s(:lit, 1)), nil), s(:return, s(:lit, 0)))))

## 官网

- 主页: http://github.com/fabiokung/ruby_parser/tree/master
- 文档: https://www.rubydoc.info/gems/fabiokung-ruby_parser/2.0.3
- RubyGems: https://rubygems.org/gems/fabiokung-ruby_parser

## 历史版本号

- 2.0.2 (2014-08-11)
- 2.0.3 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/fabiokung-ruby_parser
- gem 安装: `gem install fabiokung-ruby_parser`
- Bundler: `gem "fabiokung-ruby_parser"`
- 最新版本: 2.0.3
- 最新版归档: https://rubygems.org/downloads/fabiokung-ruby_parser-2.0.3.gem
- 版本锁定: `gem "fabiokung-ruby_parser", "~> 2.0.3"`
- 中央仓库: https://rubygems.org/
