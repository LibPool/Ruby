# hanny

**Tag**: cli, tooling, data

## 简介

Hanny is a Hash-based Approximate Nearest Neighbor (ANN) search library in Ruby.
Hash-based ANN converts vector data into binary codes and builds a hash table by using the binary codes as hash keys.
To build the hash table, Hanny uses Locality Sensitive Hashing (LSH) of approximating cosine similarity.
It is known that if the code length is sufficiently long (ex. greater than 128-bit), LSH can obtain high search performance.
In the experiment, Hanny achieved about twenty times faster search speed than the brute-force search by Euclidean distance.

## 官网

- 主页: https://github.com/yoshoku/hanny
- 文档: https://yoshoku.github.io/hanny/doc/
- 更新日志: https://github.com/yoshoku/hanny/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/hanny

## 历史版本号

- 0.2.2 (2022-08-27)
- 0.2.1 (2021-07-10)
- 0.2.0 (2021-06-25)
- 0.1.0 (2018-05-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/hanny
- gem 安装: `gem install hanny`
- Bundler: `gem "hanny"`
- 最新版本: 0.2.2
- 最新版归档: https://rubygems.org/downloads/hanny-0.2.2.gem
- 版本锁定: `gem "hanny", "~> 0.2.2"`
- 中央仓库: https://rubygems.org/
