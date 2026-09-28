# mischacks

**Tag**: filesystem, data

## 简介

Miscellaneous methods that may or may not be useful.

sh:: Safely pass untrusted parameters to sh scripts. Raise an exception if the
script returns a non-zero value.

fork_and_check:: Run a block in a forked process and raise an exception if the
process returns a non-zero value.

do_and_exit, do_and_exit!:: Run a block. If the block does not run exit!, a
successful exec or equivalent, run exit(1) or exit!(1) ourselves. Useful to
make sure a forked block either runs a successful exec or dies.

Any exceptions from the block are printed to standard error.

overwrite:: Safely replace a file. Writes to a temporary file and then moves it
over the old file.

tempname_for:: Generates an unique temporary path based on a filename. The
generated filename resides in the same directory as the original one.

try_n_times:: Retries a block of code until it succeeds or a maximum number of
attempts (default 10) is exceeded.

Exception#to_formatted_string:: Return a string that looks like how Ruby would
dump an uncaught exception.

IO#best_datasync:: Try fdatasync, falling back to fsync, falling back to flush.

Random#exp:: Return a random integer 0 ≤ n < 2^argument (using SecureRandom).

Random#float:: Return a random float 0.0 ≤ n < argument (using SecureRandom).

Random#int:: Return a random integer 0 ≤ n < argument (using SecureRandom).

Password:: A small wrapper for String#crypt that does secure salt generation
and easy password verification.

## 官网

- 主页: http://johan.kiviniemi.name/software/mischacks/
- 源码仓库: http://github.com/ion1/mischacks
- RubyGems: https://rubygems.org/gems/mischacks

## 历史版本号

- 0.2.1 (2010-08-29)
- 0.2.0 (2010-08-29)
- 0.1.1 (2010-08-25)
- 0.1.0 (2010-02-14)
- 0.0.6 (2010-02-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/mischacks
- gem 安装: `gem install mischacks`
- Bundler: `gem "mischacks"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/mischacks-0.2.1.gem
- 版本锁定: `gem "mischacks", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
