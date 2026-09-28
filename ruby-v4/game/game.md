# game

**Tag**: web, database, testing, networking, template, filesystem, data

## 简介

# Game

A Ruby-powered MVC game framework.

## Install

```sh
$ gem install game
```

## Usage

### Setup

```sh
$ game new my_cool_game
```

This will create a new directory named `my_cool_game` in the current working directory.  
The directory is laid out very much like a Rails application:

    my_cool_game
    ├── Gemfile
    ├── Guardfile
    ├── README
    ├── app
    |   ├── assets
    │   │   ├── fonts
    │   │   ├── images
    │   │   ├── music
    │   │   └── sounds
    |   ├── controllers
    │   │   └── game_controller.rb
    |   ├── helpers
    │   │   └── game_helpers.rb
    |   ├── models
    |   ├── views
    |   └── windows
    │   │   └── game_window.rb
    ├── config
    │   ├── environments
    │   │   ├── development.rb
    │   │   ├── production.rb
    │   │   └── test.rb
    │   ├── initializers
    │   ├── locales
    │   │   └── en.yml
    │   ├── application.rb
    │   ├── boot.rb
    │   └── database.yml
    │   ├── environment.rb
    │   └── routes.rb
    ├── log
    ├── spec
    |   └── spec_helper.rb
    └── tmp

## Acknowledgements

* [Rails][rails] for making MVC very popular in the [Ruby][ruby] universe
* [Gamebox][gamebox] for inspiration.

## Contributing

* Check out the latest master to make sure the feature hasn't been implemented or the bug hasn't been fixed yet
* Check out the issue tracker to make sure someone already hasn't requested it and/or contributed it
* Fork the project
* Start or switch to a testing/unstable/feature/bugfix branch
* Commit and push until you are happy with your contribution
* Make sure to add tests for it. This is important so I don't break it in a future version unintentionally.
* Please try not to mess with the Rakefile, VERSION or gemspec.

## Copyright

Copyright © 2012 Ryan Scott Lewis <ryan@rynet.us>.

The MIT License (MIT) - See LICENSE for further details.

[rails]: https://github.com/rails/rails
[ruby]: https://github.com/ruby/ruby
[gamebox]: https://github.com/shawn42/gamebox

## 官网

- 主页: http://github.com/RyanScottLewis/game
- RubyGems: https://rubygems.org/gems/game

## 历史版本号

- 0.0.1 (2012-11-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/game
- gem 安装: `gem install game`
- Bundler: `gem "game"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/game-0.0.1.gem
- 版本锁定: `gem "game", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
