# cpp_engine

**Tag**: testing, tooling, filesystem

## 简介

cpp_engine is an build system for C++ projects, It works like Make but much better. Compring to Rake, cpp_engine is more targeted at building C++ project I just started developing this system. Since I am a student in NYU, the effort I can put on this project is limited. if you are interested in it, please send me email:)
    To use this system, you need to create a file named "enginespec" in your working dir. An example of enginespec is as follows:
   compile(["*.cpp"]){|config|
	config.flags=["-O3", "-msse2", "-msse3", "-mfpmath=sse"]
	config.header_dirs=["include1","include2"]
	config.lib_dirs=["libdir1","libdir2"]
	config.libs=["math","openGL"]
        config.product="xxx"
} 
    After this file is created, you can simply run cppengine to build your project

## 官网

- 文档: https://www.rubydoc.info/gems/cpp_engine/0.0.4
- RubyGems: https://rubygems.org/gems/cpp_engine

## 历史版本号

- 0.0.4 (2012-01-25)
- 0.0.3 (2012-01-25)
- 0.0.2 (2012-01-24)
- 0.0.1 (2012-01-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/cpp_engine
- gem 安装: `gem install cpp_engine`
- Bundler: `gem "cpp_engine"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/cpp_engine-0.0.4.gem
- 版本锁定: `gem "cpp_engine", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
