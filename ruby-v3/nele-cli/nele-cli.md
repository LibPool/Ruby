# nele-cli

**Tag**: cli, testing, filesystem

## 简介

Command line interface for nele gem

### Instalation:

    $ gem install nele-cli

### Usage:
Generate config file placed in ~/.nele:<br/>

    $ nele --create-config

Microsoft translator has been set as a default translator. Edit ~/.nele config file and add app id.

    $ nele 'nice girl'
    $ miÅa dziewczyna

    $ nele --to es 'nice girl'
    $ linda chica

You can specify all translator's options in params e.g:<br/>

    $ nele -t ms --appId 5CE6C887658AB9698E1FB710C8F064F94646053B hello
    $ Witaj

Switch to Yahoo's Babelfish translator:<br/>

    $ nele -t babelfish hello
    $ Hola

## 官网

- 主页: http://github.com/cfx/nele-cli
- RubyGems: https://rubygems.org/gems/nele-cli

## 历史版本号

- 0.2.1 (2011-12-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/nele-cli
- gem 安装: `gem install nele-cli`
- Bundler: `gem "nele-cli"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/nele-cli-0.2.1.gem
- 版本锁定: `gem "nele-cli", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
