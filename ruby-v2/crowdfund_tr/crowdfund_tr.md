# crowdfund_tr

**Tag**: cli, testing, filesystem, data

## 简介

A simple, text-based crowdfunding simulator.  Run a group of projects through a
series of funding rounds, in which they either receive or lose funds, or are
skipped.  They also receive a random pledge.  Grant projects never lose funds.
Match projects have all future funding matched after they reach half-funding.
Statistics are printed to the console at the end of the simulation.

The normal projects can be specified in a '.csv' file that is given as a command
line argument when loading the program, or the default projects can be used. The
format for 'csv' entries is Project Name,Goal,Initial_funding with a comma and
no spaces between entries and underscores in place of commas within larger
numbers (e.g. Your Project,10_000,0).

The option is given to save a list of underfunded projects upon exiting the
program.  The list is saved in 'underfunded.txt' in the top-level folder of the
application.

Created as a bonus project while completing the Pragmatic Studio Ruby
Programming course.

## 官网

- 文档: https://www.rubydoc.info/gems/crowdfund_tr/1.0.0
- RubyGems: https://rubygems.org/gems/crowdfund_tr

## 历史版本号

- 1.0.0 (2015-07-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/crowdfund_tr
- gem 安装: `gem install crowdfund_tr`
- Bundler: `gem "crowdfund_tr"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/crowdfund_tr-1.0.0.gem
- 版本锁定: `gem "crowdfund_tr", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
