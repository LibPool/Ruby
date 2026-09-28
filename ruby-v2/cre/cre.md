# cre

**Tag**: web, testing, security

## 简介

Cre reduces the amount of code you have to write when                      fetching rails credentials.                      If your encrypted credentials look like this:

                      production:
                        password: 'foobar'
                      development:
                        password: 'foobar'
                      test:
                        password: 'foobar'

                      Usually you have to get it like this:
                        `Rails.application.credentials.dig(Rails.env, :password)`
                      with Cre you can just do: `Cre.dig(:password)`.
                      By default it grabs the current Rails environment.
                      To overwrite this behavior add the enviroment as the
                      first argument: `Cre.dig(:production, :password)`

## 官网

- 主页: https://github.com/khalilgharbaoui/cre
- 更新日志: https://github.com/khalilgharbaoui/cre/blob/master/CHANGELOG.md
- 问题追踪: https://github.com/khalilgharbaoui/cre/issues
- RubyGems: https://rubygems.org/gems/cre

## 历史版本号

- 2.2.0 (2026-08-02)
- 2.1.1 (2021-12-17)
- 2.1.0 (2021-07-10)
- 2 (2020-01-05)
- 0.1.5 (2019-01-31)
- 0.1.3 (2018-10-02)
- 0.1.2 (2018-10-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/cre
- gem 安装: `gem install cre`
- Bundler: `gem "cre"`
- 最新版本: 2.2.0
- 最新版归档: https://rubygems.org/downloads/cre-2.2.0.gem
- 版本锁定: `gem "cre", "~> 2.2.0"`
- 中央仓库: https://rubygems.org/
