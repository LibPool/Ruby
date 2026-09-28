# pg_search_multiple_highlight

**Tag**: testing, template, filesystem

## 简介

The 'pg_search_multiple_highlight' gem extends the functionality of
   the popular 'pg_search' gem to overcome its limitation when performing searches against
   multiple columns and attempting to highlight results. The core issue arises when using
   the ':highlight' option within the ':tsearch' scope on multiple columns. This gem
   addresses this limitation by introducing the ':multiple_highlight' option, offering a
   comprehensive solution for highlighting results across multiple columns.

   Key Features:
   New Scope Option: The gem introduces the ':multiple_highlight' scope option, allowing
    users to perform searches on multiple columns and highlight matching terms.
   Enhanced Search Results: The gem enables the extraction of highlighted results from
    multiple columns, providing a unified view of highlighted content.
   Usage Convenience: Users can easily integrate the ':multiple_highlight' option into
    their existing 'pg_search' queries by calling the '.with_pg_search_multiple_highlight'
    method on the search object.
   Flexible Customization: The gem's options can be tailored to match specific
    highlighting requirements, such as custom start and stop markers for highlighting.
   Comprehensive Documentation: The README file explains the limitations of 'pg_search'
    regarding highlighting, demonstrates how the ':multiple_highlight' option resolves
    this issue, and offers clear usage examples for quick integration.

## 官网

- 主页: https://github.com/msuliq/pg_search_multiple_highlight
- 更新日志: https://github.com/msuliq/pg_search_multiple_highlight/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/pg_search_multiple_highlight

## 历史版本号

- 0.3.0 (2024-01-28)
- 0.2.0 (2023-08-17)
- 0.1.0 (2023-08-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/pg_search_multiple_highlight
- gem 安装: `gem install pg_search_multiple_highlight`
- Bundler: `gem "pg_search_multiple_highlight"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/pg_search_multiple_highlight-0.3.0.gem
- 版本锁定: `gem "pg_search_multiple_highlight", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
