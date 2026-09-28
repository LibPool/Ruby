# autotest-run_dependencies

**Tag**: testing

## 简介

This gem provides a mechanism through which it is possible to specify that 
an arbitrary number of external dependencies are satisfied before a test 
run can be executed.

Dependencies are added by specifying a name, command, satisfied_regexp and 
errors_regexp parameter for each. The command refers to a script that is 
run to satisfy or test the dependency. If the output of the command 
(either to standard output or standard error) matches the satisfied_regexp 
then the dependency is considered met otherwise any lines in the output 
matching errors_regexp are output and the dependency test waits for changes 
to the codebase before trying to satisfy the dependency again.

## 官网

- 主页: http://github.com/tobyclemson/autotest-run_dependencies
- RubyGems: https://rubygems.org/gems/autotest-run_dependencies

## 历史版本号

- 0.1.0 (2009-11-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/autotest-run_dependencies
- gem 安装: `gem install autotest-run_dependencies`
- Bundler: `gem "autotest-run_dependencies"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/autotest-run_dependencies-0.1.0.gem
- 版本锁定: `gem "autotest-run_dependencies", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
