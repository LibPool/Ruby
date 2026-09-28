# csv-diff-report

**Tag**: testing, template, filesystem, data

## 简介

This library generates diff reports of CSV files, using the diff capabilities
        of the CSV Diff gem.

        Unlike a standard diff that compares line by line, and is sensitive to the
        ordering of records, CSV-Diff identifies common lines by key field(s), and
        then compares the contents of the fields in each line.

        CSV-Diff Report takes the diff information calculated by CSV-Diff, and
        uses it to produce Excel, HTML, or text diff reports. It also provides a
        command-line tool (csvdiff) for generating these diff reports from CSV files.

        The csvdiff command-line tool supports both file and directory diffs. As
        directories may contain files of different formats, .csvdiff files can be
        used to match file names to file types, and specify the appropriate diff
        settings for each file type.

## 官网

- 主页: https://github.com/agardiner/csv-diff-report
- 文档: https://www.rubydoc.info/gems/csv-diff-report/0.4.1
- RubyGems: https://rubygems.org/gems/csv-diff-report

## 历史版本号

- 0.4.1 (2018-07-31)
- 0.3.5 (2018-03-05)
- 0.3.4 (2017-05-17)
- 0.3.2 (2016-01-26)
- 0.3.1 (2015-02-23)
- 0.2 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/csv-diff-report
- gem 安装: `gem install csv-diff-report`
- Bundler: `gem "csv-diff-report"`
- 最新版本: 0.4.1
- 最新版归档: https://rubygems.org/downloads/csv-diff-report-0.4.1.gem
- 版本锁定: `gem "csv-diff-report", "~> 0.4.1"`
- 中央仓库: https://rubygems.org/
