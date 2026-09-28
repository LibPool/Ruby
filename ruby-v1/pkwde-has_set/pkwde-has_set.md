# pkwde-has_set

**Tag**: database, testing, data

## 简介

A simple Gem to enable any `ActiveRecord::Base` object to store a set of attributes in a set like structure represented through a bitfield on the database level.  You only have to specify the name of the set to hold the attributes in question an the rest is done for you through some fine selected Ruby magic. Here is a simple example of how you could use the gem:  class Person &lt; ActiveRecord::Base has_set :interests end  To get this to work you need some additional work done first:  1. You need an unsigned 8-Byte integer column in your database to store the bitfield. It is expected that the column is named after the name of the set with the suffix `_bitfield` appended (e.g. `interests_bitfield`). You can change that default behavior by providing the option `:column_name` (e.g. `has_set :interests, :column_name =&gt; :my_custom_column`). 2. You need a class that provides the valid values to be stored within the set and map the single bits back to something meaningful. The class should be named after the name of the set (you can change this through the `:enum_class` option). This class could be seen as an enumeration and must implement the following simple interface: * There must be a class method `values` to return all valid enumerators in the defined enumeration. * Each enumerator must implement a `name` method to return a literal representation for identification. The literal must be of the type `String`. * Each enumerator must implement a `bitfield_index` method to return the exponent of the number 2 for calculation the position of this enumerator in the bitfield. **Attention** Changing this index afterwards will destroy your data integrity.  Here is a simple example of how to implement such a enumeration type while using the the `renum` gem for simplicity. You are free to use anything else that matches the described interface.  enum :Interests do attr_reader :bitfield_index  Art(0) Golf(1) Sleeping(2) Drinking(3) Dating(4) Shopping(5)  def init(bitfield_index) @bitfield_index = bitfield_index end end

## 官网

- 主页: http://github.com/pkwde/has_set
- 文档: https://www.rubydoc.info/gems/pkwde-has_set/0.0.4
- RubyGems: https://rubygems.org/gems/pkwde-has_set

## 历史版本号

- 0.0.1 (2014-08-10)
- 0.0.2 (2014-08-10)
- 0.0.4 (2014-08-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/pkwde-has_set
- gem 安装: `gem install pkwde-has_set`
- Bundler: `gem "pkwde-has_set"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/pkwde-has_set-0.0.4.gem
- 版本锁定: `gem "pkwde-has_set", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
