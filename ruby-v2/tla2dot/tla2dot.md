# tla2dot

**Tag**: template, data

## 简介

Parse a reachability graph and process it using Mustache templates. 

Example 
State 2/2398339604900326310:
    / steps = &lt;&lt;"TenantManager", "Loader"&gt;&gt;
    / db_data = {}
    / now = 1
    / pc = [ Tail |-&gt; "tail_wait",
      TenantManager |-&gt; "tenant_manager" ]
    / db_tenants = {"t1"}
    / input_data = { [tenant |-&gt; "t1", data |-&gt; "d1"],
      [tenant |-&gt; "t2", data |-&gt; "d2"] }
    
    Transition -8297134421408988195 --&gt; 2398339604900326310

## 官网

- 文档: https://www.rubydoc.info/gems/tla2dot/0.0.6
- RubyGems: https://rubygems.org/gems/tla2dot

## 历史版本号

- 0.0.6 (2016-01-26)
- 0.0.5 (2015-12-25)
- 0.0.3 (2015-12-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/tla2dot
- gem 安装: `gem install tla2dot`
- Bundler: `gem "tla2dot"`
- 最新版本: 0.0.6
- 最新版归档: https://rubygems.org/downloads/tla2dot-0.0.6.gem
- 版本锁定: `gem "tla2dot", "~> 0.0.6"`
- 中央仓库: https://rubygems.org/
