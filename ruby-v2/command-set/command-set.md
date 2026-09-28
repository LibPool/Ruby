# command-set

**Tag**: cli, testing, serialization, template, data

## 简介

CommandSet is a user interface framework.  Its focus is a DSL for defining commands, much like Rake or RSpec.  A default readline based terminal interpreter (complete with context sensitive tab completion, and the amenities of readline: history editing, etc) is included.  It could very well be adapted to interact with CGI or a GUI - both are planned.  CommandSet has a lot of very nice features.  First is the domain-specific language for defining commands and sets of commands.  Those sets can further be neatly composed into larger interfaces, so that useful or standard commands can be resued.  Optional application modes, much like Cisco's IOS, with a little bit more flexibility.  Arguments have their own sub-language, that allows them to provide interface hints (like tab completion) as well as input validation.  On the output side of things, CommandSet has a very flexible output capturing mechanism, which generates a tree of data as it's generated, even capturing writes to multiple places at once (even from multiple threads) and keeping everything straight.  Methods that normally write to stdout are interposed and fed into the tree, so you can hack in existing scripts with minimal adjustment.  The final output can be presented to the user in a number of formats, including contextual coloring and indentation, or even progress hashes.  XML is also provided, although it needs some work.  Templates are on the way.  While you're developing your application, you might find the record and playback utilities useful.  cmdset-record will start up with your defaults for your command set, and spit out an interaction script.  Then you can replay the script against the live set with cmdset-playback.  Great for ad hoc testing, usability surveys and general demos.

## 官网

- 文档: https://www.rubydoc.info/gems/command-set/0.10.4
- RubyGems: https://rubygems.org/gems/command-set

## 历史版本号

- 0.10.4 (2009-07-25)
- 0.10.2 (2009-07-25)
- 0.10.1 (2009-07-25)
- 0.10.0 (2009-07-25)
- 0.9.2 (2009-07-25)
- 0.9.1 (2009-07-25)
- 0.9.0 (2009-07-25)
- 0.8.4 (2009-07-25)
- 0.8.3 (2009-07-25)
- 0.8.2 (2009-07-25)
- 0.8.1 (2009-07-25)
- 0.8.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/command-set
- gem 安装: `gem install command-set`
- Bundler: `gem "command-set"`
- 最新版本: 0.10.4
- 最新版归档: https://rubygems.org/downloads/command-set-0.10.4.gem
- 版本锁定: `gem "command-set", "~> 0.10.4"`
- 中央仓库: https://rubygems.org/
