# fat_table

**Tag**: cli, database, testing, template, tooling, filesystem, data

## 简介

FatTable is a gem that treats tables as a data type. It provides methods for
    constructing tables from a variety of sources, building them row-by-row,
    extracting rows, columns, and cells, and performing aggregate operations on
    columns. It also provides as set of SQL-esque methods for manipulating table
    objects: select for filtering by columns or for creating new columns, where
    for filtering by rows, order_by for sorting rows, distinct for eliminating
    duplicate rows, group_by for aggregating multiple rows into single rows and
    applying column aggregate methods to ungrouped columns, a collection of join
    methods for combining tables, and more.

    Furthermore, FatTable provides methods for formatting tables and producing
    output that targets various output media: text, ANSI terminals, ruby data
    structures, LaTeX tables, Emacs org-mode tables, and more. The formatting
    methods can specify cell formatting in a way that is uniform across all the
    output methods and can also decorate the output with any number of footers,
    including group footers. FatTable applies formatting directives to the extent
    they makes sense for the output medium and treats other formatting directives as
    no-ops.

    FatTable can be used to perform operations on data that are naturally best
    conceived of as tables, which in my experience is quite often. It can also serve
    as a foundation for providing reporting functions where flexibility about the
    output medium can be quite useful. Finally FatTable can be used within Emacs
    org-mode files in code blocks targeting the Ruby language. Org mode tables are
    presented to a ruby code block as an array of arrays, so FatTable can read
    them in with its .from_aoa constructor. A FatTable table can output as an
    array of arrays with its .to_aoa output function and will be rendered in an
    org-mode buffer as an org-table, ready for processing by other code blocks.

## 官网

- 主页: https://github.com/ddoherty03/fat_table
- 文档: https://www.rubydoc.info/gems/fat_table/1.0.0
- RubyGems: https://rubygems.org/gems/fat_table

## 历史版本号

- 1.0.0 (2025-12-28)
- 0.9.9 (2025-03-19)
- 0.9.8 (2024-12-31)
- 0.9.7 (2024-12-26)
- 0.9.5 (2023-10-07)
- 0.9.3 (2023-05-24)
- 0.9.2 (2023-05-22)
- 0.9.1 (2023-05-22)
- 0.9.0 (2023-05-22)
- 0.8.0 (2023-04-20)
- 0.7.0 (2023-04-02)
- 0.6.6 (2023-01-09)
- 0.6.4 (2022-06-07)
- 0.6.3 (2022-06-04)
- 0.6.2 (2022-05-24)
- 0.6.1 (2022-04-12)
- 0.6.0 (2022-03-26)
- 0.5.5 (2022-03-25)
- 0.5.4 (2022-01-27)
- 0.5.3 (2022-01-24)
- 0.5.2 (2022-01-22)
- 0.5.1 (2022-01-21)
- 0.4.2 (2022-01-06)
- 0.4.0 (2022-01-02)
- 0.3.4 (2022-01-01)
- 0.3.3 (2022-01-01)
- 0.3.1 (2020-12-13)
- 0.3.0 (2020-06-10)
- 0.2.11 (2019-12-29)
- 0.2.9 (2019-04-04)
- 0.2.8 (2018-08-28)
- 0.2.7 (2017-12-29)
- 0.2.6 (2017-10-27)
- 0.2.4 (2017-05-23)
- 0.2.3 (2017-05-08)
- 0.2.2 (2017-05-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/fat_table
- gem 安装: `gem install fat_table`
- Bundler: `gem "fat_table"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/fat_table-1.0.0.gem
- 版本锁定: `gem "fat_table", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
