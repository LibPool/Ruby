# protojson

**Tag**: serialization

## 简介

A Ruby gem for Google's Protocol Buffers messages using three different encodings JSON
                    based syntax instead of the original binary protocol. Supported formats

                    - Hashmap: A tipical JSON message, with key:value pairs where the key is a string representing
                        the field name.

                    - Tagmap: Very similar to Hashmap, but instead of having the field name as key it has the
                        field tag number as defined in the proto definition.

                    - Indexed: Takes the Tagmap format a further step and optimizes the size needed for
                        tag numbers by packing all of them as a string, where each character represents a tag,
                        and placing it as the first element of an array.

## 官网

- RubyGems: https://rubygems.org/gems/protojson

## 历史版本号

- 0.2.0 (2011-08-20)
- 0.1.0 (2011-03-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/protojson
- gem 安装: `gem install protojson`
- Bundler: `gem "protojson"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/protojson-0.2.0.gem
- 版本锁定: `gem "protojson", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
