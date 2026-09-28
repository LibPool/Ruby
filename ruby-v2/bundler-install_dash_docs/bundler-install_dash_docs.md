# bundler-install_dash_docs

**Tag**: testing, filesystem

## 简介

Bundler plugin that can be installed system-wide (`gem install bundler-install_dash_docs`) or on a per-project basis
    (`bundle plugin install bundler-install_dash_docs`).

    Once installed, primary command is `bundle install_dash_docs install`

    This will read your Gemfile.lock, and use the Dash.app (v3.1.0 and later) custom url scheme `dash-install:` to
    request that Dash.app install the matching documentation for each gem at the specific version. It currently takes ~2 seconds
    per gem, so its a long process for large projects.

    I'd love to do more, but Dash.app does not yet support anything more interesting (removing older versions? updating a search profile?).

## 官网

- 主页: https://github.com/e28eta/bundler-install_dash_docs
- 更新日志: https://github.com/e28eta/bundler-install_dash_docs/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/bundler-install_dash_docs

## 历史版本号

- 0.1.2-universal-darwin (2022-03-05)
- 0.1.1-universal-darwin (2022-03-05)
- 0.1.0-universal-darwin (2022-03-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/bundler-install_dash_docs
- gem 安装: `gem install bundler-install_dash_docs`
- Bundler: `gem "bundler-install_dash_docs"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/bundler-install_dash_docs-0.1.2.gem
- 版本锁定: `gem "bundler-install_dash_docs", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
