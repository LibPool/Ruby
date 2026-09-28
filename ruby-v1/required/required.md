# required

**Tag**: testing, filesystem

## 简介

Required is a utility to require all files in a directory.

Why would one want to require a whole bunch of files at once? I have used this
gem on 2 projects to:
  - require dozens of jar files when working on a JRuby project
  - pull in all files before running code coverage (rcov), to find code that
      is otherwise dead/untouched

Options for required include the ability to recursively descend through
subdirectories, include/exclude files based on pattern matching, and to specify
the order of requires based on filename.  An array of all the files that were
loaded is returned.

Quick example:
  require 'required'
  required "some/path/to/dir"

See the README for more examples, and description of options.

## 官网

- 主页: http://github.com/ashirazi/required
- RubyGems: https://rubygems.org/gems/required

## 历史版本号

- 0.1.3 (2010-04-02)
- 0.1.2 (2010-04-01)
- 0.1.1 (2010-04-01)
- 0.1.0 (2010-04-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/required
- gem 安装: `gem install required`
- Bundler: `gem "required"`
- 最新版本: 0.1.3
- 最新版归档: https://rubygems.org/downloads/required-0.1.3.gem
- 版本锁定: `gem "required", "~> 0.1.3"`
- 中央仓库: https://rubygems.org/
