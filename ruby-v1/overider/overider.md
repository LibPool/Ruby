# overider

**Tag**: library

## 简介

class A
      def hello
        "hello"
      end
    end

    # Later, I want to overide class A methods

    class A
      extend Overider

      overide (:hello) do |*a|
        overiden(*a) + " overide"
      end
    end

    A.new.hello # ==> "hello overide"

## 官网

- 主页: https://github.com/lsiden/overider
- RubyGems: https://rubygems.org/gems/overider

## 历史版本号

- 0.1 (2011-12-23)
- 0.0.1 (2011-12-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/overider
- gem 安装: `gem install overider`
- Bundler: `gem "overider"`
- 最新版本: 0.1
- 最新版归档: https://rubygems.org/downloads/overider-0.1.gem
- 版本锁定: `gem "overider", "~> 0.1"`
- 中央仓库: https://rubygems.org/
