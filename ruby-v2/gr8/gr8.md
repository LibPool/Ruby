# gr8

**Tag**: web, networking, data

## 简介

gr8 is a great command-line utility powered by Ruby.

Example:

    $ cat data
    Haruhi   100
    Mikuru    80
    Yuki     120
    $ cat data | gr8s 'map{|s|s.split()[1]}'
    100
    80
    120
    $ cat data | gr8s 'map{|s|s.split()[1]}.map(&amp;:to_i).sum'
    300
    $ cat data | gr8s 'map{split[1]}.sum_i'
    300
    $ cat data | gr8s -F 'map{self[1]}.sum_i'
    300
    $ cat data | gr8s -C2 'sum_i'
    300

See http://kwatch.github.io/gr8/ for detail.

## 官网

- 主页: http://kwatch.github.io/gr8/
- 文档: https://www.rubydoc.info/gems/gr8/0.1.1
- RubyGems: https://rubygems.org/gems/gr8

## 历史版本号

- 0.1.1 (2015-08-18)
- 0.1.0 (2015-08-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/gr8
- gem 安装: `gem install gr8`
- Bundler: `gem "gr8"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/gr8-0.1.1.gem
- 版本锁定: `gem "gr8", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
