# billymeltdown-choctop

**Tag**: serialization, tooling, devops, filesystem

## 简介

Build and deploy tools for Cocoa apps using Sparkle for distributions and upgrades; 
it’s like Hoe but for Cocoa apps.

Package up your OS X/Cocoa applications into Custom DMGs, generate Sparkle XML, and
upload. Instead of hours, its only 30 seconds to release each new version of an application.

Build and deploy tools for Cocoa apps using Sparkle for distributions and upgrades; it's
like Hoe but for Cocoa apps.

The main feature is a powerful rake task "rake appcast" which builds a release of your
application, creates a DMG package, generates a Sparkle XML file, and posts the package
and XML file to your remote host via rsync.

All rake tasks:

    rake appcast         # Create dmg, update appcast file, and upload to host
    rake build   # Build Xcode Release
    rake dmg     # Create the dmg file for appcasting
    rake feed    # Create/update the appcast file
    rake upload  # Upload the appcast file to the host

## 官网

- 主页: http://drnic.github.com/choctop
- RubyGems: https://rubygems.org/gems/billymeltdown-choctop

## 历史版本号

- 0.11.0.8 (2010-06-24)
- 0.11.0.7 (2010-05-20)
- 0.11.0.6 (2010-05-20)
- 0.11.0.5 (2010-05-05)
- 0.11.0.4 (2010-05-05)
- 0.11.0.3 (2010-04-15)
- 0.11.0.2 (2010-03-30)
- 0.11.0.1 (2010-03-30)
- 0.11.0 (2010-03-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/billymeltdown-choctop
- gem 安装: `gem install billymeltdown-choctop`
- Bundler: `gem "billymeltdown-choctop"`
- 最新版本: 0.11.0.8
- 最新版归档: https://rubygems.org/downloads/billymeltdown-choctop-0.11.0.8.gem
- 版本锁定: `gem "billymeltdown-choctop", "~> 0.11.0.8"`
- 中央仓库: https://rubygems.org/
