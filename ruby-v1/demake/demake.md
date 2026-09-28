# demake

**Tag**: web, testing, networking, template, tooling, filesystem

## 简介

== Develop, Decorate and manage Dependencies for C (GNU) Makefiles easily with Ruby.

  Install using the Ruby Gem:

  > gem install demake

  To see command syntax:

  > demake ?

    Command syntax:

    demake               - Create or update Makefile
    demake ?             - View this help information
    demake new <name>    - Create new application
    demake example       - Create an example application
    demake oreo          - Create a different sample application

  To create a new application:

  > demake new <name>

  This will create a new directory and basic files for a new C application.

  To create or update a GNU Makefile on an existing demake application,
  execute without arguments:

  > demake

  To create an example with multiple sample applications:

  > demake example

  This will create a directory named example containing the example.

  To create an example with a single sample application:

  > demake oreo

  This will create a directory named oreo containing the example.

  It requires a demake directory and application file containing the
  application names followed by depencencies separated by spaces and
  with a new line to indicate a different application.
  Something like (from the example):

  > mkdir demake
  > echo "hello string" > demake/applications
  > echo "goodbye string" >> demake/applications
  > demake

  For customization, optionally include (see example):
  demake/settings.rb, demake/test-target.rb, demake/install-target.rb,
  demake/license

  You can also clone from git:

  > git clone https://github.com/MinaswanNakamoto/demake.git
  > chmod +x demake/bin/demake
  > cd demake
  > bin/demake example
  > cd example ; make ; make build ; make test

  If you have an existing C application and you want to generate a Makefile
  for it, you might try the gen_application shell script.

  > ./gen_application myapp

## 官网

- 主页: https://github.com/MinaswanNakamoto/demake
- 文档: https://www.rubydoc.info/gems/demake/0.2.4
- RubyGems: https://rubygems.org/gems/demake

## 历史版本号

- 0.2.4 (2026-07-10)
- 0.2.3 (2026-06-29)
- 0.2.2 (2026-06-21)
- 0.2.1 (2026-05-08)
- 0.2.0 (2026-04-24)
- 0.1.2 (2026-03-12)
- 0.1.1 (2026-01-24)
- 0.1.0 (2026-01-11)
- 0.0.3 (2025-12-28)
- 0.0.2 (2025-11-18)
- 0.0.1 (2025-11-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/demake
- gem 安装: `gem install demake`
- Bundler: `gem "demake"`
- 最新版本: 0.2.4
- 最新版归档: https://rubygems.org/downloads/demake-0.2.4.gem
- 版本锁定: `gem "demake", "~> 0.2.4"`
- 中央仓库: https://rubygems.org/
