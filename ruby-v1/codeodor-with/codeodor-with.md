# codeodor-with

**Tag**: testing

## 简介

I sometimes get a little descriptive with my variable names, so when you're doing a lot of work  specifically with one object, it gets especially ugly and repetetive, making the code harder to  read than it needs to be:  @contract_participants_on_drugs.contract_id = params[:contract_id] @contract_participants_on_drugs.participant_name = params[:participant_name] @contract_participants_on_drugs.drug_conviction = DrugConvictions.find(:wtf =&gt; 'this is getting ridiculous') ...  And so on. It gets ridiculous.  Utility Belt implements a with(object) method via a change to Object:  class Object #utility belt implementation def with(object, &amp;block) object.instance_eval &amp;block end end  Unfortunately, that just executes the block in the context of the object, so there isn't any  crossover, nor can you perform assignments with attr_accessors (that I was able to do, anyway).  So, here's With.object() to fill the void.   With.object(@foo) do  a = "wtf" b = "this is not as bad" end  In the above example, @foo.a and @foo.b are the variables getting set.  If you prefer, you can require 'with_on_object' instead and use the notation with(object) do ... end.  The tests in the /test directory offer more examples of what's been implemented and tested so far  (except where noted - namely performing assignment to a variable that was declared outside the  block, and is not on @foo).  Not everything is working yet, but it works for the simplest, most common cases I've run up  against. More complex tests are on the way, along with code to make them pass.  Special thanks to Reg Braithwaite, for help and ideas along the way.

## 官网

- 主页: http://github.com/codeodor/with/tree/master
- 文档: https://www.rubydoc.info/gems/codeodor-with/0.0.2
- RubyGems: https://rubygems.org/gems/codeodor-with

## 历史版本号

- 0.0.1 (2014-08-11)
- 0.0.2 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/codeodor-with
- gem 安装: `gem install codeodor-with`
- Bundler: `gem "codeodor-with"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/codeodor-with-0.0.2.gem
- 版本锁定: `gem "codeodor-with", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
