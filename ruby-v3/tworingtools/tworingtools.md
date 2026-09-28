# tworingtools

**Tag**: web, testing, networking, tooling

## 简介

- xcsims: Delete all simulators and recreate one for each compatible platform and device type pairing.
  - sync-git-remotes: Make sure all your GitHub repos are cloned into a given directory and keep them synced with upstream. Forks are maintained with a remote for both the fork and upstream, both remotes' default branches are tracked in local counterparts, and the upstream default branch is also pushed to the fork.
  - changetag: Extract changelog entries to write into git tag annotation messages.
  - prerelease-podspec: Branch and create/push a release candidate tag, modify the podspec to use that version tag, and try linting it.
  - release-podspec: Create a tag with the version and push it to repo origin, push podspec to CocoaPods trunk.
  - revert-failed-release-tag: In case `release-podspec` fails, make sure the tag it may have created/pushed is destroyed before trying to run it again after fixing, so it doesn't break due to the tag already existing the second time around.
  - bumpr: Increment the desired part of a version number (major/minor/patch/build) and write the change to a git commit.
  - clean-rc-tags: deletes any release candidate tags leftover after prerelease testing.
  - migrate-changelog: for a changelog adhering to [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), move any contents under Unreleased to a new section for a new version with the current date.

## 官网

- 主页: https://github.com/TwoRingSoft/tools
- 文档: https://www.rubydoc.info/gems/tworingtools/6.2.0
- RubyGems: https://rubygems.org/gems/tworingtools

## 历史版本号

- 6.2.0 (2022-04-28)
- 6.1.0 (2022-04-25)
- 6.0.0 (2021-03-28)
- 5.0.0 (2021-03-27)
- 4.7.0 (2020-10-25)
- 4.6.0 (2020-10-02)
- 4.5.1 (2020-09-24)
- 4.5.0 (2020-09-24)
- 4.4.2 (2020-09-15)
- 4.4.1 (2020-09-15)
- 4.4.0 (2020-09-15)
- 4.3.2 (2020-09-10)
- 4.3.1 (2020-09-10)
- 4.3.0 (2020-09-10)
- 4.2.0 (2020-09-10)
- 4.1.0 (2020-09-09)
- 4.0.1 (2020-08-20)
- 4.0.0 (2020-08-20)
- 3.1.0 (2020-08-09)
- 3.0.2 (2020-08-05)
- 3.0.1 (2020-04-21)
- 3.0.0 (2020-04-18)
- 2.1.1 (2020-04-17)
- 2.1.0 (2020-04-17)
- 2.0.3 (2020-04-16)
- 2.0.2 (2020-04-14)
- 2.0.1 (2020-04-14)
- 2.0.0 (2020-04-14)
- 1.13.0 (2020-03-27)
- 1.12.0 (2020-03-21)
- 1.11.0 (2020-03-16)
- 1.10.0 (2020-03-16)
- 1.9.2 (2020-03-11)
- 1.9.0 (2019-12-12)
- 1.8.0 (2019-12-12)
- 1.7.0 (2019-12-05)
- 1.6.0 (2019-12-02)
- 1.5.3 (2019-10-15)
- 1.5.2 (2019-10-06)
- 1.5.1 (2019-10-05)
- 1.5.0 (2019-10-05)
- 1.4.2 (2019-09-26)
- 1.4.1 (2019-09-23)
- 1.4.0 (2019-09-23)
- 1.3.1 (2018-10-31)
- 1.3.0 (2018-10-31)
- 1.2.0 (2018-10-26)
- 1.1.1 (2018-10-25)
- 1.1.0 (2018-09-30)
- 1.0.1 (2018-09-18)
- 1.0.0 (2018-09-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/tworingtools
- gem 安装: `gem install tworingtools`
- Bundler: `gem "tworingtools"`
- 最新版本: 6.2.0
- 最新版归档: https://rubygems.org/downloads/tworingtools-6.2.0.gem
- 版本锁定: `gem "tworingtools", "~> 6.2.0"`
- 中央仓库: https://rubygems.org/
