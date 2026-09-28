# git-topic

**Tag**: template

## 简介

gem command around reviewed topic branches.  Supports workflow of the form:

      # alexander:
      git work-on <topic>
      git done

      # bismarck:
      git status    # notice a review branch
      git review <topic>
      # happy, merge into master, push and cleanup
      git accept

      git review <topic2>
      # unhappy
      git reject

      # alexander:
      git status    # notice rejected topic
      git work-on <topic>

      see README.rdoc for more (any) details.


      To make use of bash autocompletion, you must do the following:

        1.  Make sure you source share/completion.bash before you source git's completion.
        2.  Optionally, copy git-topic-completion to your gem's bin directory.
            This is to sidestep ruby issue 3465 which makes loading gems far too
            slow for autocompletion.

## 官网

- 主页: http://github.com/hjdivad/git-topic
- RubyGems: https://rubygems.org/gems/git-topic

## 历史版本号

- 0.2.7.3 (2010-10-22)
- 0.2.7.2 (2010-10-22)
- 0.2.7.1 (2010-10-21)
- 0.2.7 (2010-10-21)
- 0.2.6.1 (2010-10-20)
- 0.2.6 (2010-10-20)
- 0.2.5 (2010-08-27)
- 0.2.4.1 (2010-08-15)
- 0.2.4 (2010-08-15)
- 0.2.3.3 (2010-07-31)
- 0.2.3.2 (2010-07-30)
- 0.2.3.1 (2010-07-28)
- 0.2.3 (2010-07-26)
- 0.2.2 (2010-07-24)
- 0.2.1 (2010-07-24)
- 0.1.6.4 (2010-07-21)
- 0.1.6.3 (2010-07-14)
- 0.1.6.2 (2010-07-14)
- 0.1.5 (2010-07-14)
- 0.1.4 (2010-07-14)
- 0.1.3 (2010-07-08)
- 0.1.2 (2010-07-08)
- 0.1.1 (2010-07-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/git-topic
- gem 安装: `gem install git-topic`
- Bundler: `gem "git-topic"`
- 最新版本: 0.2.7.3
- 最新版归档: https://rubygems.org/downloads/git-topic-0.2.7.3.gem
- 版本锁定: `gem "git-topic", "~> 0.2.7.3"`
- 中央仓库: https://rubygems.org/
