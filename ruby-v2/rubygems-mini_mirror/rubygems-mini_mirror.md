# rubygems-mini_mirror

**Tag**: web, filesystem

## 简介

Mirror some version of gems with Gem::Version DSL
  Create a mini_gem file and add this to it :
  source :gemcutter
  gem 'rails', ['~> 1.2.0', '>= 3.0']

  or
  source :gemcutter
  resource :path => '/your_path/mini_gem.yml'

  # /your_path/mini_gem.yml

  gem:
    - rails:
      -
        - '~> 1.2.0'
        - '>= 3.0'

  It will solve the dependencies for you so you don't have to write an exhaustive list of the gems you want to mirror

## 官网

- RubyGems: https://rubygems.org/gems/rubygems-mini_mirror

## 历史版本号

- 1.0.3 (2011-12-28)
- 1.0.2 (2011-12-13)
- 1.0.1 (2011-09-27)
- 1.0.0 (2011-09-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/rubygems-mini_mirror
- gem 安装: `gem install rubygems-mini_mirror`
- Bundler: `gem "rubygems-mini_mirror"`
- 最新版本: 1.0.3
- 最新版归档: https://rubygems.org/downloads/rubygems-mini_mirror-1.0.3.gem
- 版本锁定: `gem "rubygems-mini_mirror", "~> 1.0.3"`
- 中央仓库: https://rubygems.org/
