# trollop-subcommands

**Tag**: cli, testing

## 简介

Though Trollop has the ability to support subcommands, I find myself
implementing the same logic repeatedly. The abstraction of this logic is
now in trollop-subcommands. This provides a framework for parsing
command line options for ruby scripts that have subcommands. The format
is 'script_name [global_options] subcommand [subcommand_options]'. The
framework supports all the typical scenarios around these type of
command line scripts. All that need to be specified are the trollop
configurations for the global options and each subcommand options. See
the readme for more information.

## 官网

- 主页: https://github.com/jwliechty/trollop-subcommands
- 文档: https://www.rubydoc.info/gems/trollop-subcommands/0.1.0
- RubyGems: https://rubygems.org/gems/trollop-subcommands

## 历史版本号

- 0.1.0 (2015-10-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/trollop-subcommands
- gem 安装: `gem install trollop-subcommands`
- Bundler: `gem "trollop-subcommands"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/trollop-subcommands-0.1.0.gem
- 版本锁定: `gem "trollop-subcommands", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
