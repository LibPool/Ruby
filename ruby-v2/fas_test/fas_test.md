# fas_test

**Tag**: cli, testing, filesystem

## 简介

Auto-discovers test classes in the working directory and runs the tests with<br/><br/>basically no boot up time and no configuration.  It doesn't matter how you<br/><br/>structure your project, instead, simple naming conventions are used:<br/><br/><br/><br/> - All test files should be named *_tests.rb<br/><br/> - All test methods should be named test__*<br/><br/><br/><br/>Other things you need to know:<br/><br/><br/><br/> - All test classes should inherit FasTest::TestClass<br/><br/> - There are two setup and two teardown methods:<br/><br/>   - class_setup: Called once before any of the tests<br/><br/>   - class_teardown: Called once after any of the tests<br/><br/>   - test_setup: Called before each test<br/><br/>   - test_teardown: Called after each test<br/><br/><br/><br/>Take a look in the test folder to see an example of how the library is used.<br/><br/>(fas_test is used to test itself).<br/><br/><br/><br/>To actually run your tests just invoke fastest.rb from a command line. It will<br/><br/>automatically recursively discover all of your test classes within the working<br/><br/>directory and run there tests.

## 官网

- 主页: https://github.com/graeme-hill/fas_test
- RubyGems: https://rubygems.org/gems/fas_test

## 历史版本号

- 1.0.0 (2011-10-15)
- 0.1.5 (2011-03-01)
- 0.1.4 (2011-02-26)
- 0.0.7 (2011-02-26)
- 0.0.2 (2011-02-25)
- 0.0.1 (2011-02-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/fas_test
- gem 安装: `gem install fas_test`
- Bundler: `gem "fas_test"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/fas_test-1.0.0.gem
- 版本锁定: `gem "fas_test", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
