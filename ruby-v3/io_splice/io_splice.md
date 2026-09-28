# io_splice

**Tag**: web, networking, filesystem, data

## 简介

The splice family of Linux system calls can transfer data between file
descriptors without the need to copy data into userspace.  Instead of a
userspace buffer, they rely on an ordinary Unix pipe as a kernel-level
buffer.  The `splice' and `tee' syscalls are also provided by the
{sleepy_penguin}[https://yhbt.net/sleepy_penguin/] library.
"io_splice" remains maintained for old applications or users
experimenting with the vmsplice syscalls

## 官网

- 主页: https://yhbt.net/ruby_io_splice/
- 文档: https://www.rubydoc.info/gems/io_splice/4.4.2
- RubyGems: https://rubygems.org/gems/io_splice

## 历史版本号

- 4.4.2 (2020-02-22)
- 4.4.1 (2019-01-02)
- 4.4.0 (2015-01-11)
- 4.3.0 (2014-02-15)
- 4.2.0 (2013-01-19)
- 4.1.1 (2011-05-18)
- 4.1.0 (2011-05-16)
- 4.0.0 (2011-05-13)
- 3.1.0 (2011-05-01)
- 3.0.0 (2011-03-01)
- 2.2.0.18.g3025 (2011-02-28)
- 2.2.0 (2010-08-02)
- 2.1.0 (2010-06-06)
- 2.0.0 (2010-06-05)
- 1.0.0 (2010-05-27)
- 0.1.0 (2010-02-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/io_splice
- gem 安装: `gem install io_splice`
- Bundler: `gem "io_splice"`
- 最新版本: 4.4.2
- 最新版归档: https://rubygems.org/downloads/io_splice-4.4.2.gem
- 版本锁定: `gem "io_splice", "~> 4.4.2"`
- 中央仓库: https://rubygems.org/
