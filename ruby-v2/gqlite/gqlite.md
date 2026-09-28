# gqlite

**Tag**: web, database, testing, networking, filesystem, data

## 简介

GQLite is a Rust-language library, with a C interface, that implements a small, fast, self-contained, high-reliability, full-featured, Graph Query database engine.
GQLite support multiple database backends, such as SQLite and redb.
This enable to achieve high performance and for application to combine Graph queries with traditional SQL queries.

GQLite source code is license under the [MIT License](LICENSE) and is free to everyone to use for any purpose.

The official repositories contains bindings/APIs for C, C++, Python, Ruby and Crystal.

The library is still in its early stage, but it is now fully functional. Development effort has now slowed down and new features are added on a by-need basis. It supports a subset of OpenCypher, with some ISO GQL extensions.

Example of use
--------------

```ruby
require 'gqlite'

begin
  # Create a database on the file "test.db"
  connection = GQLite::Connection.new filename: "test.db"

  # Execute a simple query to create a node and return all the nodes
  value = connection.execute_oc_query("CREATE () MATCH (n) RETURN n")

  # Print the result
  if value.nil?
    puts "Empty results"
  else
    puts "Results are #{value.to_s}"
  end
rescue GQLite::Error => ex
  # Report any error
  puts "An error has occured: #{ex.message}"
end

```

The documentation for the GQL query language can found in [OpenCypher](https://auksys.org/documentation/5/libraries/gqlite/opencypher/) and for the [API](https://auksys.org/documentation/5/libraries/gqlite/api/).

## 官网

- 主页: https://gitlab.com/auksys/gqlite
- 文档: https://www.rubydoc.info/gems/gqlite/1.8.2
- RubyGems: https://rubygems.org/gems/gqlite

## 历史版本号

- 1.8.2 (2026-09-26)
- 1.8.1 (2026-08-19)
- 1.8.0 (2026-07-29)
- 1.7.0 (2026-07-28)
- 1.5.1 (2026-02-21)
- 1.5.0 (2026-01-18)
- 1.4.0 (2025-11-11)
- 1.3.1 (2025-10-28)
- 1.3.0 (2025-09-01)
- 1.2.3 (2025-08-17)
- 1.2.2 (2025-07-26)
- 1.2.0 (2025-07-17)
- 1.1.0 (2024-05-18)
- 1.0.0 (2023-11-17)
- 0.9 (2023-09-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/gqlite
- gem 安装: `gem install gqlite`
- Bundler: `gem "gqlite"`
- 最新版本: 1.8.2
- 最新版归档: https://rubygems.org/downloads/gqlite-1.8.2.gem
- 版本锁定: `gem "gqlite", "~> 1.8.2"`
- 中央仓库: https://rubygems.org/
