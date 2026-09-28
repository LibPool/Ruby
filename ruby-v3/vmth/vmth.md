# vmth

**Tag**: web, testing, security, networking, template, filesystem

## 简介

require 'rubygems'
require 'rake'
require 'echoe'

Echoe.new('vmth', '0.0.2') do |p|
  p.description    = File.open(File.dirname(__FILE__+"/DESCRIPTION")).read
  p.summary        = "A VM test harness for testing operational configurations"
  p.url            = "http://github.com/gregretkowski/vmth"
  p.author         = "Greg Retkowski"
  p.email          = "greg@rage.net"
  p.ignore_pattern = ["tmp/*", "script/*", "ol/*"]
  p.rdoc_template  = nil
  p.rdoc_pattern = /^(lib|bin|tasks|ext)|^README|^CHANGELOG|^TODO|^LICENSE|^QUICKSTART|^CONFIG|^COPYING$/
#  p.rdoc_template = ""
  p.development_dependencies = []
  p.runtime_dependencies = [
    'formatr',
    'net-ssh',
    'net-scp',
  ]

end

## 官网

- 主页: http://github.com/gregretkowski/vmth
- RubyGems: https://rubygems.org/gems/vmth

## 历史版本号

- 0.0.2 (2011-04-28)
- 0.0.1 (2011-04-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/vmth
- gem 安装: `gem install vmth`
- Bundler: `gem "vmth"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/vmth-0.0.2.gem
- 版本锁定: `gem "vmth", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
