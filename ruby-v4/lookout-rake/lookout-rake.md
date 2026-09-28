# lookout-rake

**Tag**: web, testing, security, networking, tooling, filesystem

## 简介

Lookout-Rake

  Lookout-Rake provides Rake┬╣ tasks for testing using Lookout.

┬╣ See http://rake.rubyforge.org/

┬º Installation

    Install Lookout-Rake with

    % gem install lookout-rake

┬º Usage

    Include the following code in your ΓÇ╣RakefileΓÇ║:

      require 'lookout-rake-3.0'

      Lookout::Rake::Tasks::Test.new

    If the ΓÇ╣:defaultΓÇ║ task hasnΓÇÖt been defined itΓÇÖll be set to depend on the
    ΓÇ╣:testΓÇ║ task.  The ΓÇ╣:checkΓÇ║ task will also depend on the ΓÇ╣:testΓÇ║ task.
    ThereΓÇÖs also a ΓÇ╣:test:coverageΓÇ║ task that gets defined that uses the
    coverage library that comes with Ruby 1.9 to check the test coverage when
    the tests are run.

    You can hook up your test task to use your Inventory┬╣:

      load File.expand_path('../lib/library-X.0/version.rb', __FILE__)

      Lookout::Rake::Tasks::Test.new :inventory => Library::Version

    Also, if you use the tasks that come with Inventory-Rake┬▓, the test task
    will hook into the inventory you tell them to use automatically, that is,
    the following will do:

      load File.expand_path('../lib/library-X.0/version.rb', __FILE__)

      Inventory::Rake::Tasks.define Library::Version

      Lookout::Rake::Tasks::Test.new

    For further usage information, see the {API documentation}┬│.

┬╣ Inventory: http://disu.se/software/inventory/
┬▓ Inventory-Rake: http://disu.se/software/inventory-rake/
┬│ API: http://disu.se/software/lookout-rake/api/Lookout/Rake/Tasks/Test/

┬º Integration

    To use Lookout together with Vim┬╣, place ΓÇ╣contrib/rakelookout.vimΓÇ║ in
    ΓÇ╣~/.vim/compilerΓÇ║ and add

      compiler rakelookout

    to ΓÇ╣~/.vim/after/ftplugin/ruby.vimΓÇ║.  Executing ΓÇ╣:makeΓÇ║ from inside Vim
    will now run your tests and an errors and failures can be visited with
    ΓÇ╣:cnextΓÇ║.  Execute ΓÇ╣:help quickfixΓÇ║ for additional information.

    Another useful addition to your ΓÇ╣~/.vim/after/ftplugin/ruby.vimΓÇ║ file may
    be

      nnoremap <buffer> <silent> <Leader>M <Esc>:call <SID>run_test()<CR>
      let b:undo_ftplugin .= ' | nunmap <buffer> <Leader>M'

      function! s:run_test()
        let test = expand('%')
        let line = 'LINE=' . line('.')
        if test =~ '^lib/'
          let test = substitute(test, '^lib/', 'test/', '')
          let line = ""
        endif
        execute 'make' 'TEST=' . shellescape(test) line
      endfunction

    Now, pressing ΓÇ╣<Leader>MΓÇ║ will either run all tests for a given class, if
    the implementation file is active, or run the test at or just before the
    cursor, if the test file is active.  This is useful if youΓÇÖre currently
    receiving a lot of errors and/or failures and want to focus on those
    associated with a specific class or on a specific test.

┬╣ Find out more about Vim at http://www.vim.org/

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
  https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=now%40disu%2ese&item_name=Nikolai%20Weibull%20Software%20Services

┬º Reporting Bugs

    Please report any bugs that you encounter to the {issue tracker}┬╣.

  ┬╣ See https://github.com/now/lookout-rake/issues

┬º Authors

    Nikolai Weibull wrote the code, the tests, the manual pages, and this
    README.

## 官网

- 主页: http://disu.se/software/lookout-rake
- 文档: https://www.rubydoc.info/gems/lookout-rake/3.1.0
- RubyGems: https://rubygems.org/gems/lookout-rake

## 历史版本号

- 3.1.0 (2013-09-04)
- 3.0.2 (2013-04-30)
- 3.0.1 (2012-05-04)
- 3.0.0 (2012-04-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/lookout-rake
- gem 安装: `gem install lookout-rake`
- Bundler: `gem "lookout-rake"`
- 最新版本: 3.1.0
- 最新版归档: https://rubygems.org/downloads/lookout-rake-3.1.0.gem
- 版本锁定: `gem "lookout-rake", "~> 3.1.0"`
- 中央仓库: https://rubygems.org/
