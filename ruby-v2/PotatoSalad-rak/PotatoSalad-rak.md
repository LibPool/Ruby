# PotatoSalad-rak

**Tag**: filesystem

## 简介

Based on the Perl tool 'ack' by Andy Lester.  Examples with similar grep:  $ rak pattern $ grep pattern $(find . | grep -v .svn)  $ rak --ruby pattern $ grep pattern $(find . -name '*.rb' | grep -v .svn)  == FEATURES/PROBLEMS:  * Ruby regular expression syntax (uses oniguruma gem if installed). * Highlighted output. * Automatically recurses down the current directory or any given directories. * Skips version control directories, backups like '~' and '#' and your * ruby project's pkg directory. * Allows inclusion and exclusion of files based on types. * Many options similar to grep.

## 官网

- 主页: http://rak.rubyforge.org/
- 文档: https://www.rubydoc.info/gems/PotatoSalad-rak/0.9
- RubyGems: https://rubygems.org/gems/PotatoSalad-rak

## 历史版本号

- 0.9 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/PotatoSalad-rak
- gem 安装: `gem install PotatoSalad-rak`
- Bundler: `gem "PotatoSalad-rak"`
- 最新版本: 0.9
- 最新版归档: https://rubygems.org/downloads/PotatoSalad-rak-0.9.gem
- 版本锁定: `gem "PotatoSalad-rak", "~> 0.9"`
- 中央仓库: https://rubygems.org/
