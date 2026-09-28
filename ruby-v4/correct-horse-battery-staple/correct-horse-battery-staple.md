# correct-horse-battery-staple

**Tag**: web, networking, data

## 简介

Generate a 4 word password from words of size 3-8 characters, with
frequencies in the 30th-60th percentile. This range gives a nice set
of uncommon but not completely alien words.

    $ chbs generate --verbose -W 3..8 -P 30..60
    Corpus size: 6396 candidate words of 33075 total
    Entropy: 48 bits (2^48 = 281474976710656)
    Years to guess at 1000 guesses/sec: 8926
    magnate-thermal-sandbank-augur

With the --verbose flag, the utility will calculate a time-to-guess
based on a completely arbitrary 1000 guesses/sec.  If you'd like a
more secure password, either relax the various filtering rules (-W and
-P), add more words to the password, or use a larger corpus.

By default we use the American TV Shows & Scripts corpus taken from
Wiktionary.

Others provided:

* Project Gutenberg 2005 corpus taken from Wiktionary.
* 1 of every 7 of the top 60000 lemmas from wordfrequency.info (6900
  actual lemmas after processing)

See http://xkcd.com/936/ for the genesis of the idea.

Data sources:

     http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists
     http://wordfrequency.info/

## 官网

- 主页: http://github.com/rsanders/correct-horse-battery-staple
- RubyGems: https://rubygems.org/gems/correct-horse-battery-staple

## 历史版本号

- 0.6.6 (2013-02-14)
- 0.6.5 (2013-02-14)
- 0.6.4 (2012-01-13)
- 0.6.3 (2012-01-11)
- 0.6.2 (2012-01-11)
- 0.6.1 (2012-01-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/correct-horse-battery-staple
- gem 安装: `gem install correct-horse-battery-staple`
- Bundler: `gem "correct-horse-battery-staple"`
- 最新版本: 0.6.6
- 最新版归档: https://rubygems.org/downloads/correct-horse-battery-staple-0.6.6.gem
- 版本锁定: `gem "correct-horse-battery-staple", "~> 0.6.6"`
- 中央仓库: https://rubygems.org/
