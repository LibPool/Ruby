# es_tractor

**Tag**: web, cli

## 简介

Minimal, simple, DRY DSL for searching Elasticsearch.

Takes one shallow hash argument and translates it to an elaborate one passed
on to elasticsearch-api. The price: narrower options. The gain: succinctness.
For example, a root &lt;tt&gt;:range&lt;/tt&gt; is always a boolean filter and always 
includes the edges:

  tractor = Client.new
  opts = { range: { timestamp: ['now-5m', 'now'] } }

  tractor.search(opts) # =&gt; sends the following to Ealsticsearch:
  {
    "query": {
      "bool": {
        "filter": [
          {
            "range": {
              "timestamp": {
                "gte":"now-5m",
                "lte":"now"
              }
            }
          }
        ],
        "must": [],
      }
    }
  }

## 官网

- 主页: https://rubygems.org/gems/es_tractor
- 文档: https://www.rubydoc.info/gems/es_tractor/0.0.6

## 历史版本号

- 0.0.6 (2017-10-22)
- 0.0.5 (2017-10-12)
- 0.0.4 (2017-09-09)
- 0.0.3 (2017-09-09)
- 0.0.2 (2017-09-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/es_tractor
- gem 安装: `gem install es_tractor`
- Bundler: `gem "es_tractor"`
- 最新版本: 0.0.6
- 最新版归档: https://rubygems.org/downloads/es_tractor-0.0.6.gem
- 版本锁定: `gem "es_tractor", "~> 0.0.6"`
- 中央仓库: https://rubygems.org/
