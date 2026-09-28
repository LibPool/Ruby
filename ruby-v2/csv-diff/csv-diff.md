# csv-diff

**Tag**: serialization, template, filesystem, data

## 简介

This library performs diffs of CSV data, or any table-like source.

        Unlike a standard diff that compares line by line, and is sensitive to the
        ordering of records, CSV-Diff identifies common lines by key field(s), and
        then compares the contents of the fields in each line.

        Data may be supplied in the form of CSV files, or as an array of arrays. The
        diff process provides a fine level of control over what to diff, and can
        optionally ignore certain types of changes (e.g. changes in position).

        CSV-Diff is particularly well suited to data in parent-child format. Parent-
        child data does not lend itself well to standard text diffs, as small changes
        in the organisation of the tree at an upper level can lead to big movements
        in the position of descendant records. By instead matching records by key,
        CSV-Diff avoids this issue, while still being able to detect changes in
        sibling order.

        This gem implements the core diff algorithm, and handles the loading and
        diffing of CSV files (or Arrays of Arrays). It also supports converting
        data in XML format into tabular form, so that it can then be processed
        like any other CSV or table-like source.  It returns a CSVDiff object
        containing the details of differences in object form. This is useful for
        projects that need diff capability, but want to handle the reporting or
        actioning of differences themselves.

        For a pre-built diff reporting capability, see the csv-diff-report gem,
        which provides a command-line tool for generating diff reports in HTML,
        Excel, or text formats.

## 官网

- 主页: https://github.com/agardiner/csv-diff
- 文档: https://www.rubydoc.info/gems/csv-diff/0.6.1
- RubyGems: https://rubygems.org/gems/csv-diff

## 历史版本号

- 0.6.1 (2020-10-21)
- 0.6.0 (2020-08-31)
- 0.5.0 (2020-07-15)
- 0.3.5 (2018-03-05)
- 0.3.3 (2017-05-17)
- 0.3.1 (2016-01-26)
- 0.3.0 (2015-02-23)
- 0.2 (2014-08-11)
- 0.1 (2014-06-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/csv-diff
- gem 安装: `gem install csv-diff`
- Bundler: `gem "csv-diff"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/csv-diff-0.6.1.gem
- 版本锁定: `gem "csv-diff", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
