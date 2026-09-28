# puppet-lint-wmf_styleguide-check

**Tag**: tooling, filesystem

## 简介

A puppet-lint plugin to check that the code adheres to the WMF coding guidelines:

    * Check for hiera in non-profiles, and in the body of those
    * Check for roles with declared resources that are not profiles
    * Check for parametrized roles
    * Check for node declarations not using the role keyword
    * Check for system::role calls outside of roles
    * Check for cross-module class inclusion
    * Check for the use of the include keyword in profiles
    * Check for wmf-deprecated resources usage
    * Check for deprecated validate_* functions

## 官网

- 主页: https://github.com/lavagetto/puppet-lint-wmf_styleguide-check
- 文档: https://www.rubydoc.info/gems/puppet-lint-wmf_styleguide-check/1.1.4
- RubyGems: https://rubygems.org/gems/puppet-lint-wmf_styleguide-check

## 历史版本号

- 1.1.4 (2024-01-05)
- 1.1.2 (2023-08-11)
- 1.1.3 (2023-08-11)
- 1.1.1 (2023-03-13)
- 1.1.0 (2021-02-15)
- 1.0.7 (2020-10-07)
- 1.0.5 (2020-03-16)
- 1.0.4 (2018-10-09)
- 1.0.2 (2018-06-14)
- 1.0.0 (2017-10-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/puppet-lint-wmf_styleguide-check
- gem 安装: `gem install puppet-lint-wmf_styleguide-check`
- Bundler: `gem "puppet-lint-wmf_styleguide-check"`
- 最新版本: 1.1.4
- 最新版归档: https://rubygems.org/downloads/puppet-lint-wmf_styleguide-check-1.1.4.gem
- 版本锁定: `gem "puppet-lint-wmf_styleguide-check", "~> 1.1.4"`
- 中央仓库: https://rubygems.org/
