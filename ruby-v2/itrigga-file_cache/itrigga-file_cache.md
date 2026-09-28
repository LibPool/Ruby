# itrigga-file_cache

**Tag**: web, serialization, filesystem

## 简介

A simple file-system-based cache wrapper.

The main method is 'with_cache( :cache_key=>'something_unique', :timeout_seconds=>(an integer) ){ (...) }'
If the given cache key exists and has not timed out, it will return the cached value
If not, it will 
* yield to the given block
* store the result of the given block in the cache with the given key
* return the result of the given block

Required params:
* :cache_key=>'some unique string that is valid in a filename'

Optional params:
* :timeout_seconds => (an integer - default 3600)
* :cache_dir => (an absolute path - defaults to RAILS_ROOT/tmp/cache if RAILS_ROOT is defined, otherwise /tmp/cache )


Example usage:


@stats_json = Itrigga::Cache::FileCache.with_cache(:cache_key=>'admin_stats.json', :timeout_seconds=>600){
  /* some expensive remote API / slow IO call here /*
}

## 官网

- 主页: http://github.com/itrigga/itrigga-file_cache
- RubyGems: https://rubygems.org/gems/itrigga-file_cache

## 历史版本号

- 0.2.1 (2011-10-03)
- 0.2.0 (2011-10-03)
- 0.1.0 (2011-10-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/itrigga-file_cache
- gem 安装: `gem install itrigga-file_cache`
- Bundler: `gem "itrigga-file_cache"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/itrigga-file_cache-0.2.1.gem
- 版本锁定: `gem "itrigga-file_cache", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
