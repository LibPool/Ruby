# l

**Tag**: filesystem

## 简介

l is a frontend for ls and less, invoking either depending on if it is fed directories or files. This makes navigating a shell a bit smoother and easier, as it is common to switch between the two commands while poking around the file system (see Sample session).  The program filters the switches for ls and less, keeping the most useful and common for each.  Sample session:  user@box:~ l Documents Music Projects  user@box:~ l Documents/ Personal some_doc.pdf example.txt Work  user@box:~ l Documents/example.txt This is just an example Documents/example.txt (END)  user@box:~ l Documents/Work/ proposal.odt document.pdf  user@box:~ l -l Documents/Work/ -rw-r--r--  1 user user  32974 2006-03-31 12:29 proposal.odt -rw-r--r--  1 user user 451726 2006-04-13 10:33 document.pdf  Aliases:  Most aliases for ls as used in .bashrc will work as usual if ls is replaced with l, but there's more: you can combine switches for both ls and less in your alias and l will filter out the inappropriate ones. The following will set ll to use long lists for directories and to ignore case for searches when displaying files:  alias ll='l -I -l'  Because ls and less can't safely share the same switches, there are a few cases where a workaround is needed:  For ls: -i doesn't work, use --inode instead -I doesn't work, use --ignore=PATTERN  For less: -r and -R doesn't work, use --raw-control-chars instead

## 官网

- 主页: http://l-ruby.rubyforge.org
- RubyGems: https://rubygems.org/gems/l

## 历史版本号

- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/l
- gem 安装: `gem install l`
- Bundler: `gem "l"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/l-0.1.0.gem
- 版本锁定: `gem "l", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
