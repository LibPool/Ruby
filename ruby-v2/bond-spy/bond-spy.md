# bond-spy

**Tag**: cli, testing

## 简介

Bond is a small library that can be used to spy values and mock functions
    during tests. Spying is a replacement for writing the assertEquals in your
    test, which are tedious to write and even more tedious to update when your
    test setup or code inevitably changes. With Bond, you separate what is
    being verified, e.g., the variable named output, from what value it should
    have. This way you can quickly spy several variables, even have structured
    values such as lists or dictionaries, and these values are saved into an
    observation log that is saved for future reference. If the test observations
    are different you have the option to interact with a console or visual tool
    to see what has changed, and whether the reference set of observations need
    to be updated.

## 官网

- 主页: http://github.com/necula01/bond
- 文档: https://www.rubydoc.info/gems/bond-spy/0.2.1
- RubyGems: https://rubygems.org/gems/bond-spy

## 历史版本号

- 0.2.1 (2016-02-18)
- 0.2.0 (2016-02-04)
- 0.1.0 (2016-01-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/bond-spy
- gem 安装: `gem install bond-spy`
- Bundler: `gem "bond-spy"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/bond-spy-0.2.1.gem
- 版本锁定: `gem "bond-spy", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
