# choctop

**Tag**: testing, serialization, tooling, devops, filesystem

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
    rake build               # Build Xcode Release
		rake dmg[automount]      # Create the dmg file for appcasting (`rake dmg`, or `rake dmg[automount]` to automatically mount the dmg)
    rake feed                # Create/update the appcast file
    rake upload              # Upload the appcast file to the host
    rake version:bump:major  # Bump the gemspec by a major version.
    rake version:bump:minor  # Bump the gemspec by a minor version.
    rake version:bump:patch  # Bump the gemspec by a patch version.
    rake version:current     # Display the current version

## 官网

- 主页: http://drnic.github.com/choctop
- RubyGems: https://rubygems.org/gems/choctop

## 历史版本号

- 0.14.1 (2010-07-31)
- 0.14.0 (2010-07-30)
- 0.13.1 (2010-07-07)
- 0.13.0 (2010-07-06)
- 0.12.1 (2010-06-07)
- 0.12.0 (2010-05-29)
- 0.11.1 (2009-11-16)
- 0.11.0 (2009-11-16)
- 0.10.0 (2009-07-25)
- 0.9.1 (2009-07-25)
- 0.9.0 (2009-07-25)
- 0.9.3 (2009-07-25)
- 0.9.2 (2009-07-25)
- 0.9.6 (2009-07-25)
- 0.9.5 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/choctop
- gem 安装: `gem install choctop`
- Bundler: `gem "choctop"`
- 最新版本: 0.14.1
- 最新版归档: https://rubygems.org/downloads/choctop-0.14.1.gem
- 版本锁定: `gem "choctop", "~> 0.14.1"`
- 中央仓库: https://rubygems.org/
