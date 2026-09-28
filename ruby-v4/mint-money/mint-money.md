# mint-money

**Tag**: web, cli, testing, networking, filesystem

## 简介

# Mint::Money

Mint::Money perform currency conversion and arithmetics with different currencies.

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'mint-money'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install mint-money

## Usage

```
# Configure the currency rates with respect to a base currency (here EUR):
 
Money.conversion_rates('EUR', {
  'USD'     =&gt; 1.11,
  'Bitcoin' =&gt; 0.0047
})
```
 
```
# Instantiate money objects:
 
fifty_eur = Money.new(50, 'EUR')
 
# Get amount and currency:
 
fifty_eur.amount   # =&gt; 50
fifty_eur.currency # =&gt; "EUR"
fifty_eur.inspect  # =&gt; "50.00 EUR"
```
 
```
# Convert to a different currency (should return a Money
# instance, not a String):
 
fifty_eur.convert_to('USD') # =&gt; 55.50 USD
```
 
```
# Perform operations in different currencies:
 
twenty_dollars = Money.new(20, 'USD')
 
# Arithmetics:
 
fifty_eur + twenty_dollars # =&gt; 68.02 EUR
fifty_eur - twenty_dollars # =&gt; 31.98 EUR
fifty_eur / 2              # =&gt; 25 EUR
twenty_dollars * 3         # =&gt; 60 USD
```
 
```
# Comparisons (also in different currencies):
 
twenty_dollars == Money.new(20, 'USD') # =&gt; true
twenty_dollars == Money.new(30, 'USD') # =&gt; false
 
fifty_eur_in_usd = fifty_eur.convert_to('USD')
fifty_eur_in_usd == fifty_eur          # =&gt; true
 
twenty_dollars &gt; Money.new(5, 'USD')   # =&gt; true
twenty_dollars &lt; fifty_eur             # =&gt; true
```

## Development

After checking out the repo, run `bin/setup` to install dependencies. Then, run `rake spec` to run the tests. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and tags, and push the `.gem` file to [rubygems.org](https://rubygems.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/mpakus/mint-money.

[![CircleCI](https://circleci.com/gh/mpakus/mint-money.svg?style=svg)](https://circleci.com/gh/mpakus/mint-money)

## 官网

- 主页: https://github.com/mpakus/mint-money
- 文档: https://www.rubydoc.info/gems/mint-money/0.1.1
- RubyGems: https://rubygems.org/gems/mint-money

## 历史版本号

- 0.1.1 (2017-06-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/mint-money
- gem 安装: `gem install mint-money`
- Bundler: `gem "mint-money"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/mint-money-0.1.1.gem
- 版本锁定: `gem "mint-money", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
