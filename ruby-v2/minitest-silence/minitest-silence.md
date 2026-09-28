# minitest-silence

**Tag**: cli, testing

## 简介

Minitest plugin to suppress output from tests. This plugin will buffer any output coming from
a test going to STDOUT or STDERR, to make sure it doesn't interfere with the output of the test
runner itself. By default, it will discard any output, unless the `--verbose` option is set
It also supports failing a test if it is writing anything to STDOUT or STDERR by setting the
`--fail-on-output` command line option.

## 官网

- 主页: https://github.com/Shopify/minitest-silence
- RubyGems: https://rubygems.org/gems/minitest-silence

## 历史版本号

- 0.2.4 (2021-02-17)
- 0.2.3 (2020-11-18)
- 0.2.2 (2020-11-18)
- 0.2.1 (2020-06-17)
- 0.2.0 (2020-06-11)
- 0.1.0 (2020-06-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/minitest-silence
- gem 安装: `gem install minitest-silence`
- Bundler: `gem "minitest-silence"`
- 最新版本: 0.2.4
- 最新版归档: https://rubygems.org/downloads/minitest-silence-0.2.4.gem
- 版本锁定: `gem "minitest-silence", "~> 0.2.4"`
- 中央仓库: https://rubygems.org/
