# inventory-rake-tasks-yard

**Tag**: web, database, testing, security, networking, template, filesystem

## 简介

Inventory-Rake-Tasks-YARD

  Inventory-Rake-Tasks-YARD provides Rake┬╣ tasks for YARD┬▓ using your
  Inventory┬│.

┬╣ See http://rake.rubyforge.org/
┬▓ See http://yardoc.org/
┬│ See http://disu.se/software/inventory/

┬º Installation

    Install Inventory-Rake-Tasks-YARD with

    % gem install inventory-rake-tasks-yard

┬º Usage

    Include the following code in your ΓÇ╣RakefileΓÇ║ (assuming that youΓÇÖve already
    set up Inventory-Rake┬╣:

      Inventory::Rake::Tasks.unless_installing_dependencies do
        require 'inventory-rake-tasks-yard-1.0'
        Inventory::Rake::Tasks::YARD.new
      end

    ThisΓÇÖll define the following tasks:

  = .yardopts (file). = Create .yardopts file; depends on the file defining
      this task and Rakefile.
  = html. = Generate documentation in HTML format for all lib files in the
      inventory; depends on .yardopts file.

    ΓÇ╣Inventory::Rake::Tasks::YARDΓÇ║ takes a couple of options, but the ones you
    might want to adjust are

  = :options. = The options to pass to YARD; will be passed to
      `Shellwords.shelljoin`.
  = :globals. = The globals to pass to YARD.
  = :files. = The files to process; mainly used if you want to add additional
      files to process beyond the lib files in the inventory.

    The options passed to YARD will be augmented with any options you list in a
    file named ΓÇ╣.yardopts.taskΓÇ║, where ΓÇ╣taskΓÇ║ is the name of the Rake task
    invoking YARD, for example, ΓÇ╣.yardopts.htmlΓÇ║ for the default
    HTML-generating task.  You can use this to add options that are local to
    your installation and should thus not be listed in the Rakefile itself.

    See the {API documentation}┬▓ for more information.

┬╣ See http://disu.se/software/inventory-rake/
┬▓ See http://disu.se/software/inventory-rake-tasks-yard/api/Inventory/Rake/Tasks/YARD/

┬º Financing

    Currently, most of my time is spent at my day job and in my rather busy
    private life.  Please motivate me to spend time on this piece of software
    by donating some of your money to this project.  Yeah, I realize that
    requesting money to develop software is a bit, well, capitalistic of me.
    But please realize that I live in a capitalistic society and I need money
    to have other people give me the things that I need to continue living
    under the rules of said society.  So, if you feel that this piece of
    software has helped you out enough to warrant a reward, please PayPal a
    donation to now@disu.se┬╣.  Thanks!  Your support wonΓÇÖt go unnoticed!

┬╣ Send a donation:
  https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=now%40disu%2ese&item_name=Inventory-Rake-Tasks-YARD

┬º Reporting Bugs

    Please report any bugs that you encounter to the {issue tracker}┬╣.

  ┬╣ See https://github.com/now/inventory-rake-tasks-yard/issues

┬º Authors

    Nikolai Weibull wrote the code, the tests, the manual pages, and this
    README.

┬º Licensing

    Inventory-Rake-Tasks-YARD is free software: you may redistribute it and/or
    modify it under the terms of the {GNU Lesser General Public License,
    version 3}┬╣ or later┬▓, as published by the {Free Software Foundation}┬│.

┬╣ See http://disu.se/licenses/lgpl-3.0/
┬▓ See http://gnu.org/licenses/
┬│ See http://fsf.org/

## 官网

- 主页: http://disu.se/software/inventory-rake-tasks-yard
- 文档: https://www.rubydoc.info/gems/inventory-rake-tasks-yard/1.4.1
- RubyGems: https://rubygems.org/gems/inventory-rake-tasks-yard

## 历史版本号

- 1.4.1 (2013-09-04)
- 1.4.0 (2013-09-04)
- 1.3.4 (2013-06-04)
- 1.3.3 (2013-04-30)
- 1.3.2 (2013-04-10)
- 1.3.1 (2012-05-04)
- 1.3.0 (2012-05-01)
- 1.2.0 (2012-04-30)
- 1.1.0 (2012-04-29)
- 1.0.0 (2012-04-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/inventory-rake-tasks-yard
- gem 安装: `gem install inventory-rake-tasks-yard`
- Bundler: `gem "inventory-rake-tasks-yard"`
- 最新版本: 1.4.1
- 最新版归档: https://rubygems.org/downloads/inventory-rake-tasks-yard-1.4.1.gem
- 版本锁定: `gem "inventory-rake-tasks-yard", "~> 1.4.1"`
- 中央仓库: https://rubygems.org/
