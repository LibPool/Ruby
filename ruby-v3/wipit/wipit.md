# wipit

**Tag**: filesystem

## 简介

Save your work.

        $ wipit
        > git add . && git rm $(git ls-files --deleted) && git commit -m 'WIP'

    Save your work to a topic branch.

        $ wipit my_wip_branch
        > git checkout -b my_wip_branch && git add . && git rm $(git ls-files --deleted) && git commit -m 'WIP'

    Save your work to a topic branch and push to origin.

        $ wipit my_wip_branch -p
        > git checkout -b my_wip_branch && git add . && git rm $(git ls-files --deleted) && git commit -m 'WIP' && git push origin my_wip_branch

## 官网

- 主页: http://github.com/johnnytommy/wipit
- RubyGems: https://rubygems.org/gems/wipit

## 历史版本号

- 0.1.1 (2011-09-29)
- 0.1.0 (2011-08-16)
- 0.0.2 (2011-04-29)
- 0.0.1 (2011-04-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/wipit
- gem 安装: `gem install wipit`
- Bundler: `gem "wipit"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/wipit-0.1.1.gem
- 版本锁定: `gem "wipit", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
