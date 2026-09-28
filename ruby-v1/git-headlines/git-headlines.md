# git-headlines

**Tag**: testing, filesystem

## 简介

Gem exposes `githl` binary that allows to perform line count / contributor at current HEAD. Running on dirty working tree will produce git errors.

Binary has a couple of options:
  `-p` or `--path` specifies relative path, defaults to `.`;
  `-i` or `--include` specify included files/directories or file extensions;
  `-e` or `--exlude` specify exluded files/directories or file extensions;
  `-v` or `--version` prints version.

  Currently does not work with non-UTF-8 encoded files.

## 官网

- 源码仓库: https://github.com/vikdotdev/git-headlines
- RubyGems: https://rubygems.org/gems/git-headlines

## 历史版本号

- 0.0.5 (2019-12-17)
- 0.0.4 (2019-12-16)
- 0.0.3 (2019-12-15)
- 0.0.2 (2019-12-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/git-headlines
- gem 安装: `gem install git-headlines`
- Bundler: `gem "git-headlines"`
- 最新版本: 0.0.5
- 最新版归档: https://rubygems.org/downloads/git-headlines-0.0.5.gem
- 版本锁定: `gem "git-headlines", "~> 0.0.5"`
- 中央仓库: https://rubygems.org/
