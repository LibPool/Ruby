# kaboom

**Tag**: web, database, serialization

## 简介

This is a fork of Zach Holman's amazing boom. Explanation for
  the fork follows Zach's intro to boom:

  God it's about every day where I think to myself, gadzooks,
  I keep typing *REPETITIVE_BORING_TASK* over and over. Wouldn't it be great if
  I had something like boom to store all these commonly-used text snippets for
  me? Then I realized that was a worthless idea since boom hadn't been created
  yet and I had no idea what that statement meant. At some point I found the
  code for boom in a dark alleyway and released it under my own name because I
  wanted to look smart.

  Explanation for my fork:

  Zach didn't fancy changing boom a great deal to handle the case of remote and
  local boom repos. Which is fair enough I believe in simplicity.
  But I also believe in getting tools to do what you want them to do.
  So with boom, you can change your storage with a 'boom storage' command, but
  that's a hassle when you want to share stuff.

  So kaboom does what boom does plus simplifies maintaining two boom repos.
  What this means is that you can pipe input between remote and local boom
  instances. My use case is to have a redis server in our office and be able
  to share snippets between each other, but to also be able to have personal
  repos.

  It's basically something like distributed key-value stores. I imagine some of
  the things that might be worth thinking about, based on DVC are:

  Imports/Exports of lists/keys/values between repos.
  Merge conflict resolution
  Users/Permissions/Teams/Roles etc
  Enterprisey XML backend
  I'm kidding

  No, but seriously I think I might allow import/export of lists and whole repos
  so that we can all easily back stuff up

  E.g.
  clone the whole shared repo
  backup your local repo to the central one underneath a namespace

## 官网

- 主页: https://github.com/markburns/kaboom
- RubyGems: https://rubygems.org/gems/kaboom

## 历史版本号

- 0.3.3 (2012-03-18)
- 0.3.2 (2012-03-17)
- 0.3.1 (2012-03-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/kaboom
- gem 安装: `gem install kaboom`
- Bundler: `gem "kaboom"`
- 最新版本: 0.3.3
- 最新版归档: https://rubygems.org/downloads/kaboom-0.3.3.gem
- 版本锁定: `gem "kaboom", "~> 0.3.3"`
- 中央仓库: https://rubygems.org/
