# ion1-mischacks

**Tag**: filesystem, data

## 简介

Miscellaneous methods that may or may not be useful.  sh:: Safely pass untrusted parameters to sh scripts.  fork_and_check:: Run a block in a forked process and raise an exception if the process returns a non-zero value.  do_and_exit, do_and_exit!:: Run a block. If the block does not run exit!, a successful exec or equivalent, run exit(1) or exit!(1) ourselves. Useful to make sure a forked block either runs a successful exec or dies.  Any exceptions from the block are printed to standard error.  overwrite:: Safely replace a file. Writes to a temporary file and then moves it over the old file.  tempname_for:: Generates an unique temporary path based on a filename. The generated filename resides in the same directory as the original one.  try_n_times:: Retries a block of code until it succeeds or a maximum number of attempts (default 10) is exceeded.  Exception#to_formatted_string:: Returns a string that looks like how Ruby would dump an uncaught exception.  IO#best_datasync:: Tries fdatasync, falling back to fsync, falling back to flush.

## 官网

- 主页: http://johan.kiviniemi.name/software/mischacks/
- 文档: https://www.rubydoc.info/gems/ion1-mischacks/0.0.5
- RubyGems: https://rubygems.org/gems/ion1-mischacks

## 历史版本号

- 0.0.1 (2014-08-11)
- 0.0.2 (2014-08-11)
- 0.0.3 (2014-08-11)
- 0.0.4 (2014-08-11)
- 0.0.5 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/ion1-mischacks
- gem 安装: `gem install ion1-mischacks`
- Bundler: `gem "ion1-mischacks"`
- 最新版本: 0.0.5
- 最新版归档: https://rubygems.org/downloads/ion1-mischacks-0.0.5.gem
- 版本锁定: `gem "ion1-mischacks", "~> 0.0.5"`
- 中央仓库: https://rubygems.org/
