# ignore_nil

**Tag**: library

## 简介

The plugin is really rather simple; here's the ignore_nil method:

        def ignore_nil(&block)
          begin
            yield
          rescue NoMethodError, RuntimeError => e
            if (e.message =~ /You have a nil object when you didn't expect it/) ||
                (e.message =~ /undefined method `.*?' for nil:NilClass/) || (e.message =~ /^Called id for nil/)
              return nil
            else
              raise e
            end
          end
        end

    What's interesting about this is it catches both NoMethodError and RuntimeError, both of which
    can occur if a method unexpectedly returned nil and you called a method on it, but *ONLY* if
    the error message matches!  This means legitimate NoMethodError and RuntimeError messages will
    not be bothered by ignore_nil, and will still raise in your application as you expect.

    I've used this in a production application since about mid/late 2008, I'd consider it very stable.
    Feedback welcome!

## 官网

- 主页: http://github.com/ssoroka/ignore_nil
- RubyGems: https://rubygems.org/gems/ignore_nil

## 历史版本号

- 1.0.3 (2009-10-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/ignore_nil
- gem 安装: `gem install ignore_nil`
- Bundler: `gem "ignore_nil"`
- 最新版本: 1.0.3
- 最新版归档: https://rubygems.org/downloads/ignore_nil-1.0.3.gem
- 版本锁定: `gem "ignore_nil", "~> 1.0.3"`
- 中央仓库: https://rubygems.org/
