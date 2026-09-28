# lookout-rack

**Tag**: web, database, testing, security, networking, tooling, filesystem

## 简介

Lookout-Rack

  Lookout-Rack provides easy interaction with Rack┬╣ from Lookout┬▓.  It provides
  you with a session connected to your Rack application through which you can
  make requests, check responses, follow redirects and set, inspect, and clear
  cookies.

┬╣ See http://rack.rubyforge.org/
┬▓ See http://disu.se/software/lookout/

┬º Installation

    Install Lookout-Rack with

    % gem install lookout-rack

┬º Usage

    Include the following code in your ΓÇ╣RakefileΓÇ║ (provided that youΓÇÖre using
    Lookout-Rake┬╣):

      require 'lookout-rack-3.0'

      Lookout::Rake::Tasks::Test.new do |t|
        t.requires << 'lookout-rack-3.0'
      end

  ┬╣ See http://disu.se/software/lookout-rake/

    Then set up a ΓÇ╣fixtures/config.ruΓÇ║ file that Lookout-Rack
    will use for loading your Rack app.

      load 'path/to/app.rb'
      use Rack::Lint
      run Path::To::App

    This file, if it exists, will be loaded during the first call to #session.
    If it doesnΓÇÖt exist, ΓÇ╣config.ruΓÇ║ will be used instead.

    You can now test your app:

      Expectations do
        expect 200 do
          session.get('/').response.status
        end
      end

    The #session method returns an object that lets you #get, #post, #put, and
    #delete resources from the Rack app.  You call these method with a URI┬╣
    that you want to access/modify together with any parameters that you want
    to pass and any Rack environment that you want to use (which isnΓÇÖt very
    common).  For example, letΓÇÖs get ΓÇ╣/pizzas/ΓÇ║ with olives on them:

      expect 200 do
        session.get('/pizzas/', 'olives' => '1').response.status
      end

  ┬╣ Abbreviation for Uniform Resource Identifier

    The #response method on #session returns a mock Rack response object that
    can be queried for results.  Similarly, thereΓÇÖs a #request method that lets
    you inspect the request that was made.

    Lookout-Rack also deals with cookies.  Assuming that ΓÇ╣/cookies/set/ΓÇ║ will
    set any cookies that we pass it and that ΓÇ╣/cookies/show/ΓÇ║ will simply do
    nothing relevant, the following expectation will pass:

      expect 'value' => '1' do
        session.
          get('/cookies/set/', 'value' => '1').
          get('/cookies/show/').request.cookies
      end

    Sometimes you may want to set cookies yourself before making a request.
    You then use the #cookie method, which takes a String of ΓÇ╣KEY=VALUEΓÇ║ pairs
    separated by newlines, commas, and/or semicolons and sets those cookies in
    the session:

      expect 'value' => '1', 'other' => '2' do
        session.
          cookie("value=1\n\nother=2").
          get('/cookies/show/').request.cookies
      end

    You may also want to clear all cookies in your session using #clear:

      expect({}) do
        session.
          get('/cookies/set', 'value' => '1').
          clear.
          get('/cookies/show').request.cookies
      end

    Finally, to test redirects, call the #redirect! method on the session
    object, assuming that ΓÇ╣/redirected/ΓÇ║ redirects to another location:

      expect result.redirect? do
        session.get('/redirected/').response
      end

      expect result.not.redirect? do
        session.get('/redirected/').redirect!.response
      end

    ThatΓÇÖs basically all thereΓÇÖs to it.  You can check the {API documentation}┬╣
    for more information.

┬╣ See http://disu.se/software/lookout-rack/api/Lookout/Rack/

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
  https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=now@disu.se&item_name=Lookout-Rack

┬º Reporting Bugs

    Please report any bugs that you encounter to the {issue tracker}┬╣.

  ┬╣ See https://github.com/now/lookout-rack/issues

┬º Authors

    Nikolai Weibull wrote the code, the tests, the documentation, and this
    README.

┬º Licensing

    Lookout-Rack is free software: you may redistribute it and/or modify it
    under the terms of the {GNU Lesser General Public License, version 3}┬╣ or
    later┬▓, as published by the {Free Software Foundation}┬│.

┬╣ See http://disu.se/licenses/lgpl-3.0/
┬▓ See http://gnu.org/licenses/
┬│ See http://fsf.org/

## 官网

- 主页: http://disu.se/software/lookout-rack/
- 文档: https://www.rubydoc.info/gems/lookout-rack/1.0.1
- RubyGems: https://rubygems.org/gems/lookout-rack

## 历史版本号

- 1.0.1 (2013-09-09)
- 1.0.0 (2013-05-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/lookout-rack
- gem 安装: `gem install lookout-rack`
- Bundler: `gem "lookout-rack"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/lookout-rack-1.0.1.gem
- 版本锁定: `gem "lookout-rack", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
