# rgfa

**Tag**: web, testing, networking, filesystem

## 简介

The Graphical Fragment Assembly (GFA) is a proposed format which allow
    to describe the product of sequence assembly.
    This gem implements the proposed specifications for the GFA format
    described under https://github.com/pmelsted/GFA-spec/blob/master/GFA-spec.md
    as close as possible.
    The library allows to create an RGFA object from a file in the GFA format
    or from scratch, to enumerate the graph elements (segments, links,
    containments, paths and header lines), to traverse the graph (by
    traversing all links outgoing from or incoming to a segment), to search for
    elements (e.g. which links connect two segments) and to manipulate the
    graph (e.g. to eliminate a link or a segment or to duplicate a segment
    distributing the read counts evenly on the copies).

## 官网

- 主页: http://github.com/ggonnella/rgfa
- 文档: https://www.rubydoc.info/gems/rgfa/1.3.1
- RubyGems: https://rubygems.org/gems/rgfa

## 历史版本号

- 1.3.1 (2016-10-10)
- 1.2.1 (2016-09-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/rgfa
- gem 安装: `gem install rgfa`
- Bundler: `gem "rgfa"`
- 最新版本: 1.3.1
- 最新版归档: https://rubygems.org/downloads/rgfa-1.3.1.gem
- 版本锁定: `gem "rgfa", "~> 1.3.1"`
- 中央仓库: https://rubygems.org/
