# do_not_want

**Tag**: library

## 简介

Several methods in ActiveRecord skip validations, callbacks, or both. In my extremely humble but also extremely correct opinion, it's too easy to accidentally use these.

Do Not Want kills those methods dead so you won't cut yourself on them:

    >> User.new.update_attribute(:foo, 5)
    DoNotWant::NotSafe: User#update_attribute isn't safe because it skips validation

## 官网

- 主页: http://github.com/garybernhardt/do_not_want
- RubyGems: https://rubygems.org/gems/do_not_want

## 历史版本号

- 0.0.1 (2011-08-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/do_not_want
- gem 安装: `gem install do_not_want`
- Bundler: `gem "do_not_want"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/do_not_want-0.0.1.gem
- 版本锁定: `gem "do_not_want", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
