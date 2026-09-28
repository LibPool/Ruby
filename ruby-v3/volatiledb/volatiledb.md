# volatiledb

**Tag**: testing, serialization, filesystem, data

## 简介

The VolatileDB gem allows you to specify a key and an action yielding a particular piece of data.
  
  This data will be stored in the /tmp folder of the file system you are currently running on. Data is accessible
  by key. Data will be read and written to storage using File.read() and File.open() -- that's it. It's up to the
  consuming application to serialize and deserialize data correctly. All VolatileDB does is push and pull data to
  the FS. 
  
  If the underlying file supporting the data is found to be missing, it will be re-initialized.
  
  This gets to the main idea behind VolatileDB: use it to persist data that is transient and can be re-seeded 
  periodically as conditions change.

## 官网

- 主页: https://github.com/bitops/volatiledb
- 文档: http://bitops.github.com/volatiledb/Volatile/DB.html
- 问题追踪: https://github.com/bitops/volatiledb/issues
- RubyGems: https://rubygems.org/gems/volatiledb

## 历史版本号

- 1.0.0 (2012-01-11)
- 0.0.4 (2012-01-11)
- 0.0.3 (2012-01-10)
- 0.0.2 (2012-01-04)
- 0.0.1 (2012-01-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/volatiledb
- gem 安装: `gem install volatiledb`
- Bundler: `gem "volatiledb"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/volatiledb-1.0.0.gem
- 版本锁定: `gem "volatiledb", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
