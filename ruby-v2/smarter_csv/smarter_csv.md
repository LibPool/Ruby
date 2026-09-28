# smarter_csv

**Tag**: web, testing, filesystem, data

## 简介

SmarterCSV is a high-performance CSV reader and writer for Ruby focused on
fastest end-to-end ingestion — not just parsing. It returns ready-to-use
hashes with configurable header and value transformations, intelligent
defaults, and automatic delimiter discovery.

Built for real-world data pipelines, SmarterCSV supports chunked processing
for large files, streaming via Enumerable APIs, and C acceleration
to optimize the full ingestion path (parsing + hash construction +
conversions).

Designed to handle messy user-uploaded CSV while remaining easy to integrate
with Rails, ActiveRecord imports, Sidekiq jobs, parallel processing, and
S3-based workflows.

## 官网

- 主页: https://github.com/tilo/smarter_csv
- 文档: https://github.com/tilo/smarter_csv/tree/main/docs
- 更新日志: https://github.com/tilo/smarter_csv/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/tilo/smarter_csv/issues
- RubyGems: https://rubygems.org/gems/smarter_csv

## 历史版本号

- 1.19.0 (2026-08-10)
- 1.18.1 (2026-07-01)
- 1.18.0 (2026-06-19)
- 1.17.4 (2026-06-03)
- 1.17.3 (2026-05-27)
- 1.16.6 (2026-05-21)
- 1.17.2 (2026-05-21)
- 1.17.1 (2026-05-17)
- 1.16.5 (2026-05-17)
- 1.15.3 (2026-05-17)
- 1.17.0 (2026-05-14)
- 1.17.0.pre5 (2026-04-28)
- 1.16.4 (2026-04-21)
- 1.16.3 (2026-04-14)
- 1.16.2 (2026-03-30)
- 1.16.1 (2026-03-16)
- 1.16.0 (2026-03-13)
- 1.15.2 (2026-02-20)
- 1.15.1 (2026-02-17)
- 1.15.0 (2026-02-04)
- 1.14.4 (2025-05-29)
- 1.14.3 (2025-05-05)
- 1.14.2 (2025-04-10)
- 1.14.1 (2025-04-09)
- 1.14.0 (2025-04-07)
- 1.13.1 (2024-12-12)
- 1.13.0 (2024-11-05)
- 1.12.1 (2024-07-10)
- 1.12.0 (2024-07-10)
- 1.12.0.pre1 (2024-07-08)
- 1.11.2 (2024-07-06)
- 1.11.0 (2024-07-02)
- 1.10.3 (2024-03-10)
- 1.10.2 (2024-02-11)
- 1.11.0.pre2 (2024-01-14)
- 1.11.0.pre1 (2024-01-13)
- 1.10.1 (2024-01-07)
- 1.10.0 (2023-12-31)
- 1.9.3 (2023-12-16)
- 1.9.2 (2023-11-12)
- 1.9.2.pre01 (2023-11-12)
- 1.9.0 (2023-09-05)
- 1.8.5 (2023-06-26)
- 1.8.4 (2023-04-02)
- 1.8.3 (2023-03-30)
- 1.8.2 (2023-03-22)
- 1.8.1 (2023-03-19)
- 1.8.0 (2023-03-19)
- 1.7.4 (2023-01-14)
- 1.7.3 (2022-12-09)
- 1.7.2 (2022-08-29)
- 1.7.1 (2022-07-31)
- 1.6.1 (2022-05-06)
- 1.6.0 (2022-05-03)
- 1.5.2 (2022-04-29)
- 1.5.1 (2022-04-27)
- 1.5.0 (2022-04-25)
- 1.4.2 (2022-02-15)
- 1.4.0 (2022-02-11)
- 1.3.0 (2022-02-07)
- 1.2.8 (2021-02-04)
- 1.2.7 (2021-02-04)
- 1.2.6 (2018-11-13)
- 1.2.5 (2018-09-16)
- 1.2.4 (2018-08-06)
- 1.2.3 (2018-01-27)
- 1.2.0 (2018-01-20)
- 1.1.5 (2017-11-06)
- 1.1.4 (2017-01-17)
- 1.1.3 (2016-12-30)
- 1.1.2 (2016-12-30)
- 1.1.1 (2016-11-26)
- 1.1.0 (2015-07-27)
- 1.0.19 (2014-10-29)
- 1.0.18 (2014-10-28)
- 1.0.17 (2014-01-13)
- 1.0.16 (2014-01-13)
- 1.0.15 (2013-12-07)
- 1.0.14 (2013-11-02)
- 1.0.12 (2013-10-16)
- 1.0.11 (2013-09-28)
- 1.0.10 (2013-06-26)
- 1.0.9 (2013-06-19)
- 1.0.8 (2013-06-01)
- 1.0.7 (2013-05-20)
- 1.0.6 (2013-05-20)
- 1.0.5 (2013-05-09)
- 1.0.4 (2012-08-17)
- 1.0.3 (2012-08-17)
- 1.0.2 (2012-08-02)
- 1.0.1 (2012-07-30)
- 1.0.0 (2012-07-29)
- 1.0.0.pre1 (2012-07-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/smarter_csv
- gem 安装: `gem install smarter_csv`
- Bundler: `gem "smarter_csv"`
- 最新版本: 1.19.0
- 最新版归档: https://rubygems.org/downloads/smarter_csv-1.19.0.gem
- 版本锁定: `gem "smarter_csv", "~> 1.19.0"`
- 中央仓库: https://rubygems.org/
