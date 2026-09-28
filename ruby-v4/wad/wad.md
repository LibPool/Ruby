# wad

**Tag**: filesystem

## 简介

Since we're all following very strict standards with regards to how our gems 
    are constructed, we might as well pack all those gems back into a directory 
    and use that directory in our load path. 

    Once you do that, you'll discover that loading from all these paths and doing 
    dependency resolution cost on every ruby invocation. On our machines, using 
    wad saves us &gt;500ms every time, on every call. 

    Wad helps you with getting there: It vendors your Gemfile below `vendor/bundle`, 
    then copies relevant source code to `vendor/lib`. All in one simple call.

## 官网

- 主页: https://bitbucket.org/technologyastronauts/wad
- 文档: https://www.rubydoc.info/gems/wad/0.2.1
- RubyGems: https://rubygems.org/gems/wad

## 历史版本号

- 0.2.1 (2015-05-19)
- 0.2.0 (2015-05-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/wad
- gem 安装: `gem install wad`
- Bundler: `gem "wad"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/wad-0.2.1.gem
- 版本锁定: `gem "wad", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
