# protoc

**Tag**: tooling

## 简介

This gem includes protoc, the protobuf compiler, binaries for Linux, Mac, and Windows. It installs a executable shim
called `protoc` that picks the right one to run on your platform. You can use this gem to ensure that you have a protoc
of the version you need. By using this gem, you will not need to manually install the right protoc on your hosts.

The pre-built linux protoc binaries are not compatible with all systems.  For this reason the protobuf source code is
included in this gem, and a new protoc binary is built upon gem installation when the pre-built one does not function.

## 官网

- 主页: https://github.com/Tripwire/protoc-gem
- 文档: https://www.rubydoc.info/gems/protoc/2.6.1.3
- RubyGems: https://rubygems.org/gems/protoc

## 历史版本号

- 2.6.1.3-universal-mswin32 (2018-11-13)
- 2.6.1.3 (2018-11-13)
- 2.6.1.3-universal-mingw32 (2018-11-13)
- 2.6.1.2-universal-mswin32 (2017-02-14)
- 2.6.1.2 (2017-02-14)
- 2.6.1.2-universal-mingw32 (2017-02-14)
- 2.6.1.1-universal-mswin32 (2017-02-13)
- 2.6.1.1-universal-mingw32 (2017-02-13)
- 2.6.1.1 (2017-02-13)
- 2.5.0 (2016-04-15)
- 2.6.1 (2016-04-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/protoc
- gem 安装: `gem install protoc`
- Bundler: `gem "protoc"`
- 最新版本: 2.6.1.3
- 最新版归档: https://rubygems.org/downloads/protoc-2.6.1.3.gem
- 版本锁定: `gem "protoc", "~> 2.6.1.3"`
- 中央仓库: https://rubygems.org/
