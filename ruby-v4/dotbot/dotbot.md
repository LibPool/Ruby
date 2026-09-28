# dotbot

**Tag**: web, cli, serialization, networking, filesystem

## 简介

# Dotbot: A Cute Lil' Dotfiles Manager

I made a simple little dotfiles manager because I got tired of creating symlinks all the time.

## Installation

You can install `dotbot` via the `gem` command:

    $ gem install dotbot

Once you have it installed, either create a `~/.dotbot` file (YAML) with the following contents.

```
dir: ~/.dotfiles  # or whatever your preferred location is
```

Optionally, instead of a .dotbot file, you can use environment variables, each of the pattern DOTBOT_&lt;var&gt;.  For instance, you could execute some commands by saying

    $ DOTBOT_DIR=~/shnargleflorp dotbot update

More commands and options to come later.

## Usage

### Track a New File

    $ dotbot track &lt;filename&gt; [--git]

This command adds the file to your dotfiles repo and creates a symlink in the file's old location so it will stay updated.  Use the `--git` flag to also add/commit/push to your remote dotfiles repo.

### Update Your Dotfiles

    $ dotbot update

This command is pretty much just a `git pull` in your dotfiles repo.

## Development

After checking out the repo, run `bin/setup` to install dependencies. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and tags, and push the `.gem` file to [rubygems.org](https://rubygems.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/[USERNAME]/dotbot-mini. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the Dotbot::Mini project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/rpalo/dotbot/blob/master/CODE_OF_CONDUCT.md).

## 官网

- 主页: https://github.com/rpalo/dotbot
- 文档: https://www.rubydoc.info/gems/dotbot/0.1.1
- RubyGems: https://rubygems.org/gems/dotbot

## 历史版本号

- 0.1.1 (2018-03-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/dotbot
- gem 安装: `gem install dotbot`
- Bundler: `gem "dotbot"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/dotbot-0.1.1.gem
- 版本锁定: `gem "dotbot", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
