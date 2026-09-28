# gem-exefy

**Tag**: filesystem

## 简介

GemExefy is RubyGems plugin aimed to replace batch files (.bat) with
executables with the same name. This gem will work only on
RubyInstaller Ruby installation and it requires RubyInstaller DevKit.

Reason for such replaceming batch files with executable stubs is
twofold. When execution of batch file is interrupted with Ctrl-C key
combination, user is faced with the confusing question

"Terminate batch job (Y/N)?"

which is avoided after replacement.

Second reason is appearance of processes in Task manager (or Process
Explorer). In the case of batch files all processes are visible as
ruby.exe. In order to distinguish between them, program arguments must
be examined. In addition, having one process name makes it hard to
define firewall rules. Having executable versions instead of batch
files will facilitate process identification in task list as well as
defining firewall rules. Moreover it makes it possible to create
selective firewall rules for different Ruby gems. Installing Ruby
applications as Windows services should be also much easer when
executable stub is used instead of batch file.

## 官网

- 主页: http://github.com/bosko/gem-exefy
- RubyGems: https://rubygems.org/gems/gem-exefy

## 历史版本号

- 1.2.0-universal-mingw32 (2012-09-11)
- 1.1.0-x86-mingw32 (2012-09-07)
- 1.0.0-x86-mingw32 (2012-06-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/gem-exefy
- gem 安装: `gem install gem-exefy`
- Bundler: `gem "gem-exefy"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/gem-exefy-1.2.0.gem
- 版本锁定: `gem "gem-exefy", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
