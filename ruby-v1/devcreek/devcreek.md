# devcreek

**Tag**: web, cli, testing, serialization, networking, template, filesystem

## 简介

The DevCreek gem enables programmers to collect and transmit metrics from their Ruby Test::Unit and RSpec test suites to a DevCreek server. Please visit the DevCreek site (http://devcreek.com/index.html) for more info.  == FEATURES/PROBLEMS:  Supported frameworks include Test::Unit and RSpec (&gt; 1.10).  == SYNOPSIS:  The DevCreek Ruby Gem is library that, when loaded, will automatically listen to and collect metrics from your  Test::Unit/RSpec unit tests. All you have to do is load the DevCreek library in your code and give it your  DevCreek account info so that it can transmit the metrics to the server. Here is the simplest example of how to  load DevCreek:  -------- #Load the devcreek gem require 'rubygems' require 'devcreek'  #set your account info  DevCreek::Core.instance().load_from_yaml(&quot;#{ENV['HOME']}/.yoursettingsfile.devcreek.yml&quot;)   --------  There are two ways to provide DevCreek with your account settings. The first (as shown above) is to point DevCreek to a  settings file. The 'enabled' attribute tells devcreek whether or not it should actually transmit the metrics that it  collects. The yaml file would like this:  -------- user: your_devcreek_username password: your_devcreek_password project: your_devcreek_project enabled: true --------  The other way to provide DevCreek with your settings is via a hash. So, instead of loading a yaml file, you could do this:  -------- #Load the devcreek gem require 'rubygems' require 'devcreek'  #set your account info  DevCreek::Core.instance().load( :user =&gt; 'your_devcreek_username', :password =&gt; 'your_devcreek_password', :project =&gt; 'your_devcreek_project', :enabled =&gt; true )   --------  The first method is preferrable because it allows you to keep your account settings outside of your project (and therefore  your source control tool).  If you only have 1 test file, you can place the code to load devcreek in the test file and your done. However, most projects will have many test files. In this case, you need to make sure that the Ruby interpreter loads devcreek before running the test classes. This can be done via the Ruby '-r' option. For example, assuming your code to load devcreek is in a file called foo.rb, you would run your tests from the command line like this:  ruby -r foo.rb test/test_*  If you run your tests from a Rakefile, then you need to tell rake to include the -r option when it runs the tests (rake runs it's tests in a separate Ruby process). You can do this pretty easily in your Rakefile, like so;  -------- require 'rake/testtask' Rake::TestTask.new('all_tests') do |t| t.ruby_opts = ['-r foo.rb'] t.test_files = ['test/test_*.rb'] end --------

## 官网

- 主页: http://rubyforge.org/projects/devcreek/
- RubyGems: https://rubygems.org/gems/devcreek

## 历史版本号

- 0.1 (2009-07-25)
- 0.5 (2009-07-25)
- 0.4 (2009-07-25)
- 0.3 (2009-07-25)
- 0.2 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/devcreek
- gem 安装: `gem install devcreek`
- Bundler: `gem "devcreek"`
- 最新版本: 0.5
- 最新版归档: https://rubygems.org/downloads/devcreek-0.5.gem
- 版本锁定: `gem "devcreek", "~> 0.5"`
- 中央仓库: https://rubygems.org/
