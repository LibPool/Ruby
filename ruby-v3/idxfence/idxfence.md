# idxfence

**Tag**: web

## 简介

idxfence cross-references every `validates :column, uniqueness: true`
/ `uniqueness: { scope: ... }` / `validates_uniqueness_of` declaration
in app/models/*.rb against db/schema.rb's create_table blocks, and
flags any whose column set (including scope columns) has no matching
`t.index [...], unique: true`. An ActiveRecord uniqueness validation
only performs a SELECT ... WHERE check at the application layer
before an INSERT -- under real concurrency, two requests can both
pass that check before either commits, landing a genuine duplicate
row despite the validation "working." Rails Guides themselves
document this exact race and recommend a matching DB-level unique
index as the only real fix; plenty of real apps ship with only the
AR-level check.

## 官网

- 主页: https://github.com/jay-tank/idxfence
- RubyGems: https://rubygems.org/gems/idxfence

## 历史版本号

- 0.1.0 (2026-09-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/idxfence
- gem 安装: `gem install idxfence`
- Bundler: `gem "idxfence"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/idxfence-0.1.0.gem
- 版本锁定: `gem "idxfence", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
