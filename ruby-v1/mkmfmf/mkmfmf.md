# mkmfmf

**Tag**: testing, filesystem

## 简介

Fork of bundled mkmf.rb, should work as drop in replacement. Modifications: * GDB and XCode path compatibility: relative path specified by mkmf (../../../../ext/<target>/...) confuses source-to-debug correspondence. The downside to this is that mkmfmf specifies absolute paths, which means that the project will have to be recompiled for debugging from an alternate location. This can be disabled by adding a use_relative_paths block. * CURRENTLY NOT WORKING: Sub-directory support for source code: all .c, .m, .cc, .cxx., .cpp files and if the filesystem is case sensitive, all .C files are automatically included, and any directories with .h files are added to INCFLAGS. * Automatically uses CC from ENV if set

## 官网

- 主页: http://rubygems.org/gems/mkmfmf
- RubyGems: https://rubygems.org/gems/mkmfmf

## 历史版本号

- 0.4 (2010-10-29)
- 0.3 (2010-09-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/mkmfmf
- gem 安装: `gem install mkmfmf`
- Bundler: `gem "mkmfmf"`
- 最新版本: 0.4
- 最新版归档: https://rubygems.org/downloads/mkmfmf-0.4.gem
- 版本锁定: `gem "mkmfmf", "~> 0.4"`
- 中央仓库: https://rubygems.org/
