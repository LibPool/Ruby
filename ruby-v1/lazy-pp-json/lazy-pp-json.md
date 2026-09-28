# lazy-pp-json

**Tag**: serialization

## 简介

Lazy pp json responses.

### JSON#pretty_generate

```ruby
example_json = "[[0,1395671860.99505,2.50339508056641e-05],{"alloc_count":136,"starttime":1395671856,"uptime":4,"version":"4.0.0","n_queries":0,"cache_hit_rate":0.0,"command_version":1,"default_command_version":1,"max_command_version":2}]"
puts JSON.pretty_generate(JSON.parse(example_json))
#=>
# [
#   [
#     0,
#     1395671860.99505,
#     2.50339508056641e-05
#   ],
#   {
#     "alloc_count": 136,
#     "starttime": 1395671856,
#     "uptime": 4,
#     "version": "4.0.0",
#     "n_queries": 0,
#     "cache_hit_rate": 0.0,
#     "command_version": 1,
#     "default_command_version": 1,
#     "max_command_version": 2
#   }
# ]
```

### lazy-pp-json

```ruby
example_json = "[[0,1395671860.99505,2.50339508056641e-05],{"alloc_count":136,"starttime":1395671856,"uptime":4,"version":"4.0.0","n_queries":0,"cache_hit_rate":0.0,"command_version":1,"default_command_version":1,"max_command_version":2}]"
pp Lazy::PP::JSON.new(example_json)
#=>
[
  [0, 1395671860.99505, 2.50339508056641e-05],
  {
    "alloc_count"            :136,
    "starttime"              :1395671856,
    "uptime"                 :4,
    "version"                :"4.0.0",
    "n_queries"              :0,
    "cache_hit_rate"         :0.0,
    "command_version"        :1,
    "default_command_version":1,
    "max_command_version"    :2
  }
]

```

## 官网

- 文档: https://www.rubydoc.info/gems/lazy-pp-json/0.0.5
- RubyGems: https://rubygems.org/gems/lazy-pp-json

## 历史版本号

- 0.0.5 (2014-03-24)
- 0.0.4 (2014-03-15)
- 0.0.3 (2014-03-15)
- 0.0.2 (2014-03-09)
- 0.0.1 (2014-03-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/lazy-pp-json
- gem 安装: `gem install lazy-pp-json`
- Bundler: `gem "lazy-pp-json"`
- 最新版本: 0.0.5
- 最新版归档: https://rubygems.org/downloads/lazy-pp-json-0.0.5.gem
- 版本锁定: `gem "lazy-pp-json", "~> 0.0.5"`
- 中央仓库: https://rubygems.org/
