# pik

**Tag**: cli, testing, filesystem

## 简介

Pik is a tool to manage multiple versions of ruby on Windows.  It can be used from the Windows command line (cmd.exe), Windows PowerShell, or Git Bash.  I have yet to test on cygwin.  

    >pik help commands

      add             Adds another ruby location to pik.
      benchmark|bench Runs bencmarks with all versions that pik is aware of.
      checkup|cu      Checks your environment for current Ruby best practices.
      config          Adds/modifies configuration options.
      default         Switches back to the default settings.
      gem             Runs the gem command with all versions that pik is aware of.
      gemsync         Synchronizes gems from the version specified to the current version.
      help            Displays help information.
      implode         Removes your pik configuration.
      info            Displays information about the current ruby version.
      install|in      Downloads and installs different ruby versions.
      list|ls         Lists ruby versions that pik is aware of.
      rake            Runs the rake command with all versions that pik is aware of.
      remove|rm       Removes a ruby location from pik.
      ruby|rb         Runs ruby with all versions that pik is aware of.
      run             Runs command with all versions of ruby that pik is aware of.
      switch|sw|use   Switches ruby versions based on patterns.
      tag             Adds the given tag to the current version.
      tags            Runs the pik command against the given tags.
      uninstall|unin  Deletes a ruby version from the filesystem and removes it from Pik.
      update|up       updates pik.

    For help on a particular command, use 'pik help COMMAND'.

## 官网

- 主页: http://github.com/vertiginous/pik
- 源码仓库: http://github.com/vertiginous/pik/tree/
- 问题追踪: http://github.com/vertiginous/pik/issues
- RubyGems: https://rubygems.org/gems/pik

## 历史版本号

- 0.2.8 (2010-06-22)
- 0.2.7 (2010-06-16)
- 0.2.6 (2009-11-08)
- 0.2.5 (2009-11-03)
- 0.2.4 (2009-10-28)
- 0.2.2 (2009-10-26)
- 0.2.3 (2009-10-26)
- 0.2.1 (2009-10-20)
- 0.2.0 (2009-10-19)
- 0.1.1 (2009-09-26)
- 0.1.0 (2009-09-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/pik
- gem 安装: `gem install pik`
- Bundler: `gem "pik"`
- 最新版本: 0.2.8
- 最新版归档: https://rubygems.org/downloads/pik-0.2.8.gem
- 版本锁定: `gem "pik", "~> 0.2.8"`
- 中央仓库: https://rubygems.org/
