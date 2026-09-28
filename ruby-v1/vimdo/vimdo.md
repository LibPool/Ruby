# vimdo

**Tag**: web, cli, filesystem

## 简介

Vimdo is a ruby gem to automate tasks with vim remote servers.
Predefined tasks include diff, merge, etc.  You can define your own recipes
to run tasks with Vim. For example, you can define `DirDiff` recipe:

```ruby
module VimDo
  class CLI < Thor

    desc "dirdiff", "directory diff in vim"
    def dirdiff(from, to)
      [from, to].each do |f|
        unless File.directory?(f)
          raise PathError "#{f} is not directory!"
        end
      end

      from, to = [from, to].map {|f| File.expand_path(f) }
      commands(%Q{exec 'DirDiff ' fnameescape("#{from}") fnameescape("#{to}")})
    end

  end
end

```

Then run `vimdo dirdiff path/to/a path/to/b` from the command line or other tools

## 官网

- 主页: http://zhaocai.github.com/vimdo
- 文档: https://www.rubydoc.info/gems/vimdo/1.2.1
- RubyGems: https://rubygems.org/gems/vimdo

## 历史版本号

- 1.2.1 (2013-10-29)
- 1.2.0 (2013-04-21)
- 1.1.1 (2013-04-19)
- 1.1.0 (2013-04-07)
- 1.0.2 (2013-04-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/vimdo
- gem 安装: `gem install vimdo`
- Bundler: `gem "vimdo"`
- 最新版本: 1.2.1
- 最新版归档: https://rubygems.org/downloads/vimdo-1.2.1.gem
- 版本锁定: `gem "vimdo", "~> 1.2.1"`
- 中央仓库: https://rubygems.org/
