# zu

**Tag**: web, networking, filesystem

## 简介

zu
==

Unzipper (in the tradition of `uz`, but better). Works for .tgz, .xz, .zip,
.deb, .rpm — you name it. (Literally. If you find an archive that it doesn't
open, let me know about it and I'll add that.)

If you have an archive sitting there of format `xyz`, then `zu foo.xyz` should
take care of it.

It will:

- Know how to extract the archive (based on extension ┈ though a version that
  detects based on `file` is something we're considering)
- Guard against impoliteness. That is, if the archive only has one file, it
  will be permitted to extract into the current directory, otherwise it will
  first `mkdir foo; cd foo` then extract there. (The directory name will be
  the archive file minus the extension.)
- Download the file first, using `wget`, if the arg starts with `http:`,
  `https:`, or `ftp:`
- Remove the archive file if you pass `-d`

Dependencies
------------

`zu` doesn't strive to be dependency-free by any means.

For starters, it expects Ruby.

Then it simply delegates to `unzip`, `gunzip`, `tar`, etc.

Not sure if I ever plan on changing this. The main purpose is to optimize the
command-line extraction of archives on a configured box.

Installation
------------

1. Have Ruby 1.8 (with gems) or 1.9
2. `gem install zu`

Feedback
--------

Tell us. (exad-zu@sharpsaw.worg)[mailto:exad-zu@sharpsaw.org]

## 官网

- 主页: https://github.com/exad/zu/
- RubyGems: https://rubygems.org/gems/zu

## 历史版本号

- 0.1 (2012-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/zu
- gem 安装: `gem install zu`
- Bundler: `gem "zu"`
- 最新版本: 0.1
- 最新版归档: https://rubygems.org/downloads/zu-0.1.gem
- 版本锁定: `gem "zu", "~> 0.1"`
- 中央仓库: https://rubygems.org/
