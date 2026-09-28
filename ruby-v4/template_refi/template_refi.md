# template_refi

**Tag**: template, tooling

## 简介

it does not allow the execution of arbitrary code
  templates may contain functions calls of the form \\-function_name(coma,seperated,list,of,minival,values)
  "minival" is a variable parser (see gem "minival_refi")
  (last time I checked one argument was mandatory (suggestion: "\\-fun_without_args(nil)" ))
  
  usage:
  include Refi
  template = Template.new(template_string)
  chunks = template.get_chunks()
  
  "chunks" is an array containing the text of the template as strings and the function calls as hashes {fun_name => [list,of,arguments]}

## 官网

- 主页: http://rubygems.org/gems/template_refi
- RubyGems: https://rubygems.org/gems/template_refi

## 历史版本号

- 0.1.0 (2011-07-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/template_refi
- gem 安装: `gem install template_refi`
- Bundler: `gem "template_refi"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/template_refi-0.1.0.gem
- 版本锁定: `gem "template_refi", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
