# rspec-advanced_subject

**Tag**: testing, filesystem

## 简介

advanced_subject attempts to cut out having to explicitly write the subject of your example group when trying to call methods or add arguments to methods. It works by reading the conventional description syntax to determine what the method you are calling is and later you state what you are passing to it.

Given you have a file advanced_subject_spec.rb.
```ruby
describe Hash do
  when_initialized_with [:a, :b] do
    it { should eq({a: :b}) }

    describe '#fetch' do
      when_passed :a do
        it { should eq(:b) }
      end
    end
  end
end
```

When you run `rspec -f d advanced_subject_spec.rb` it will output:
```
Hash
  when initialized with [:a, :b]
    should eq {:a =&gt; :b}
  #fetch
    when passed :a
      should eq :b
```

## 官网

- 主页: https://github.com/kwstannard/rspec-advanced_subject
- 文档: https://www.rubydoc.info/gems/rspec-advanced_subject/0.0.4
- RubyGems: https://rubygems.org/gems/rspec-advanced_subject

## 历史版本号

- 0.0.4 (2014-12-12)
- 0.0.2.1 (2014-07-28)
- 0.0.1 (2014-07-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/rspec-advanced_subject
- gem 安装: `gem install rspec-advanced_subject`
- Bundler: `gem "rspec-advanced_subject"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/rspec-advanced_subject-0.0.4.gem
- 版本锁定: `gem "rspec-advanced_subject", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
