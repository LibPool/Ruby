# baf

**Tag**: cli, testing, filesystem

## 简介

== Baf

baf helps writing an user acceptance test suite with a dedicated library
and cucumber steps. It can run and wait for programs in a modified
environment, verify the exit status, the output streams and other side
effects. It also supports interactive programs and writing to their
standard input.

Then, it provides a DSL to write the CLI:

    require 'baf/cli'

    module MyProgram
      class CLI < Baf::CLI
        def setup
          flag_version '0.1.2'.freeze

          option :c, :config, 'config', 'specify config file' do |path|
            @config_path = path
          end
        end

        def run
          usage! unless arguments.any?

          puts 'arguments: %s' % arguments
          puts 'config: %s' % @config_path if @config_path
        end
      end
    end

    MyProgram::CLI.run ARGV

Which behaves this way:

    % ./my_program
    Usage: my_program [options]

    options:
        -c, --config config              specify config file

        -h, --help                       print this message
        -V, --version                    print version
    zsh: exit 64    ./my_program

    % ./my_program --wrong-arg
    Usage: my_program [options]

    options:
        -c, --config config              specify config file

        -h, --help                       print this message
        -V, --version                    print version
    zsh: exit 64    ./my_program --wrong-arg

    % ./my_program foo
    arguments ["foo"]

    % ./my_program -c some_file foo
    arguments ["foo"]
    config path some_file

## 官网

- 主页: https://rubygems.org/gems/baf
- 文档: https://www.rubydoc.info/gems/baf/0.15.1

## 历史版本号

- 0.15.1 (2022-07-06)
- 0.15.0 (2022-06-12)
- 0.14.1 (2020-11-04)
- 0.14.0 (2017-10-22)
- 0.13.0 (2017-10-22)
- 0.12.0 (2017-05-11)
- 0.11.0 (2017-04-28)
- 0.10.0 (2017-04-23)
- 0.9.1 (2017-02-12)
- 0.9.0 (2017-01-22)
- 0.8.0 (2016-11-13)
- 0.7.0 (2016-11-13)
- 0.6.2 (2016-11-01)
- 0.6.1 (2016-11-01)
- 0.6.0 (2016-09-23)
- 0.5.0 (2016-09-23)
- 0.4.0 (2016-03-28)
- 0.2.1 (2016-03-27)
- 0.2.0 (2016-03-27)
- 0.1.1 (2016-03-10)
- 0.1.0 (2016-03-08)
- 0.0.3 (2016-03-05)
- 0.0.2 (2016-02-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/baf
- gem 安装: `gem install baf`
- Bundler: `gem "baf"`
- 最新版本: 0.15.1
- 最新版归档: https://rubygems.org/downloads/baf-0.15.1.gem
- 版本锁定: `gem "baf", "~> 0.15.1"`
- 中央仓库: https://rubygems.org/
