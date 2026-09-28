# rtrac

**Tag**: data

## 简介

== FEATURES/PROBLEMS:  Ticket access for Trac  == SYNOPSIS:  Rtrac::Base.get_by_milestone(milestone).each do |id| # grab the ticket's data tick = Rtrac::Ticket.new(id) iteration_hash[:total] += tick.severity.to_i iteration_hash[:tickets] &lt;&lt; {:id =&gt; id, :points =&gt; tick.severity.to_i, :status =&gt; tick.status, :updated_at =&gt;Time.parse(tick.updated_at.to_s)} end  == REQUIREMENTS:  active_support hoe

## 官网

- 文档: https://www.rubydoc.info/gems/rtrac/1.0.2
- RubyGems: https://rubygems.org/gems/rtrac

## 历史版本号

- 1.0.2 (2009-07-25)
- 1.0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/rtrac
- gem 安装: `gem install rtrac`
- Bundler: `gem "rtrac"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/rtrac-1.0.2.gem
- 版本锁定: `gem "rtrac", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
