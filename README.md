# Ruby 库索引

本仓库收录 RubyGems 中央仓库中的 Ruby gem，按 Ruby 大版本与 gem 名称组织。

- 大版本目录：`ruby-v1`、`ruby-v2`、`ruby-v3`、`ruby-v4`
- gem 路径：`<gem>/<gem>.md`
- gem 会根据所有历史版本声明的 `required_ruby_version` 约束，同时出现在兼容的大版本目录中
- 当前共枚举 196990 个 RubyGems gem

## 收录的中央仓库

| 中央仓库 | 地址 | 说明 |
| --- | --- | --- |
| RubyGems.org | https://rubygems.org/ | Ruby 官方社区 gem 仓库 |
| RubyGems compact index | https://index.rubygems.org/ | 全量 gem 名称、版本和依赖索引 |
| RubyGems API | https://rubygems.org/api/v1/ | gem 详情、项目主页和仓库元数据 |
| Ruby 官网 | https://www.ruby-lang.org/ | Ruby 语言与运行时 |

## 大版本统计

- `ruby-v1`：162486 个 gem
- `ruby-v2`：184820 个 gem
- `ruby-v3`：195740 个 gem
- `ruby-v4`：195682 个 gem

## 生成方式

```bash
python tools/generate_index.py
```

生成器使用 SQLite 保存名称、版本元数据和 gem 详情缓存，网络中断后可直接续跑。
