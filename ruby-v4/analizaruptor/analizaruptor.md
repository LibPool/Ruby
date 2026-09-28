# analizaruptor

**Tag**: filesystem

## 简介

Analizaruptor is a tool that looks for 'break', 'require', and 'provides'
commands (and does a *teensy* bit of code analyzing (+/(class|module) *(w+)/+)
to provide some defaults) to make your RubyMotion +Rakefile+ and +debugger_cmds+
files short and consistent.

To use, include this gem, and add +app.analyze+ to your +Rakefile+, after you
have added your libraries and whatnot.  In your source code you can add
Analizaruptor commands (+#----> break|provides|requires+) and those will be
translated into directives for `app.files_dependencies` and `debugger_cmds`.

Run +rake+ or +rake debug=1+, and off you go!

## 官网

- 主页: https://github.com/colinta/analizaruptor
- RubyGems: https://rubygems.org/gems/analizaruptor

## 历史版本号

- 0.3.1 (2013-03-07)
- 0.3.0 (2012-12-07)
- 0.2.0 (2012-12-03)
- 0.1.0 (2012-10-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/analizaruptor
- gem 安装: `gem install analizaruptor`
- Bundler: `gem "analizaruptor"`
- 最新版本: 0.3.1
- 最新版归档: https://rubygems.org/downloads/analizaruptor-0.3.1.gem
- 版本锁定: `gem "analizaruptor", "~> 0.3.1"`
- 中央仓库: https://rubygems.org/
