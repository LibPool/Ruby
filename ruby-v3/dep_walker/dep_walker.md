# dep_walker

**Tag**: web, networking, tooling, filesystem

## 简介

The dep_walker is small utility gem that checks dependencies for native extensions
used by installed gems on Windows. If you are {RubyInstaller}[http://www.rubyinstaller.org]
user and have seen message box:

<em>"This application has failed to start because <name_of_dll>.dll was not found.
Re-installing the application may fix this problem"</em>

when you tried to use gem that has pre-built binariy extension, you've faced common
problem on Windows systems - missing dependency dll. Same error might occur even if
extension library was built during gem installation if all header files and libraries
are available to the build tools, but runtime dependencies are not present.

With dep_walker you can simply check all installed gems. Even more, if log is turned on,
gem will print out information where dependency is found on the system, so you can check
whether Ruby extension really uses correct version of required dll.

## 官网

- 主页: http://github.com/bosko/dep_walker
- RubyGems: https://rubygems.org/gems/dep_walker

## 历史版本号

- 1.0.2 (2011-05-22)
- 1.0.1 (2011-05-07)
- 1.0.0 (2011-05-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/dep_walker
- gem 安装: `gem install dep_walker`
- Bundler: `gem "dep_walker"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/dep_walker-1.0.2.gem
- 版本锁定: `gem "dep_walker", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
