# runshare

**Tag**: web, cli, testing, networking, devops, filesystem

## 简介

# ruby unshare (runshare)

This tool allows to unshare Linux namespaces.
The implementation is similar to the unshare(1) tool.

## Installation

Add this line to your application's Gemfile:

```ruby
    gem 'runshare'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install runshare

## Usage

    > require "runshare"
    > RUnshare::unshare

For example:

    cat > test.rb

    require "runshare"

    pid = RUnshare::unshare(
      :clone_newpid    => true,
      :clone_newns     => true,
      :clone_newcgroup => true,
      :clone_newipc    => true,
      :clone_newuts    => true,
      :clone_newnet    => true,
      :clone_newtime   => true,
      :fork            => true,
      :mount_proc      => "/proc",
      # docker export $(docker create hello-world) | tar -xf - -C rootfs
      :root            => "/tmp/rootfs"
    )

    if pid == 0
      # child
      puts "--- #{Process.pid}"
      if system("/hello") != true
        raise "bad"
      end
      puts "--- done"
    else
      # parent
      puts "-- unshare=#{pid}, pid=#{Process.pid}"
      puts "-- exit=#{Process.waitpid(pid)}"
    end

    ^D

    sudo ruby -I ./lib ./test.rb

## Quick start

    $ rake compile && echo 'require "runshare"; RUnshare::unshare(:clone_newuts => true)' | irb
    install -c tmp/x86_64-linux/runshare/2.4.10/runshare.so lib/runshare/runshare.so
    cp tmp/x86_64-linux/runshare/2.4.10/runshare.so tmp/x86_64-linux/stage/lib/runshare/runshare.so
    Switch to inspect mode.
    require "runshare"; RUnshare::unshare

## Ruby <2.5

If your app is single threaded and you are observing:

    eval:1: warning: pthread_create failed for timer: Invalid argument, scheduling broken

Just ignore it with some degree of bravity. You also
can silence it by setting:

    $VERBOSE = nil

## Development

After checking out the repo, run `bin/setup` to install dependencies.
Then, run `rake spec` to run the tests.
You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`.
To release a new version, update the version number in `version.rb`,
and then run `bundle exec rake release`, which will create a git tag
for the version, push git commits and tags, and push the `.gem` file
to [rubygems.org](https://rubygems.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/sitano/runshare.
This project is intended to be a safe, welcoming space for collaboration,
and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## 官网

- 主页: https://github.com/sitano/runshare
- RubyGems: https://rubygems.org/gems/runshare

## 历史版本号

- 0.1.0 (2021-11-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/runshare
- gem 安装: `gem install runshare`
- Bundler: `gem "runshare"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/runshare-0.1.0.gem
- 版本锁定: `gem "runshare", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
