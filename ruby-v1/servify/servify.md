# servify

**Tag**: web, testing

## 简介

Running servify will stop any process on 3000 (rails server default), and run rails server after that. 
  You can specify different port like this:
  $ servify 8080

  Useful when used with tmuxinator gem (or any other), e.g.:

  windows:
    - editor:
      layout: main-vertical
      panes:
        - vim
        - servify
        - guard

## 官网

- 主页: https://github.com/ilyadoroshin/servify
- 文档: https://www.rubydoc.info/gems/servify/0.1.9
- RubyGems: https://rubygems.org/gems/servify

## 历史版本号

- 0.1.9 (2015-08-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/servify
- gem 安装: `gem install servify`
- Bundler: `gem "servify"`
- 最新版本: 0.1.9
- 最新版归档: https://rubygems.org/downloads/servify-0.1.9.gem
- 版本锁定: `gem "servify", "~> 0.1.9"`
- 中央仓库: https://rubygems.org/
