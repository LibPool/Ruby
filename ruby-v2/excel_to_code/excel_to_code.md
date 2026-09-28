# excel_to_code

**Tag**: web, testing, networking, filesystem, data

## 简介

# Excel to Code

[![Tests Passing](https://travis-ci.org/tamc/excel_to_code.svg?branch=master)](https://travis-ci.org/tamc/excel_to_code)

excel_to_c - roughly translate some Excel files into C.

excel_to_ruby - roughly translate some Excel files into Ruby.

This allows spreadsheets to be:

1. Embedded in other programs, such as web servers, or optimisers
2. Without depending on any Microsoft code

For example, running [these commands](examples/simple/compile.sh) turns [this spreadsheet](examples/simple/simple.xlsx) into [this Ruby code](examples/simple/ruby/simple.rb) or [this C code](examples/simple/c/simple.c).

# Install

Requires Ruby. Install by:

    gem install excel_to_code

# Run

To just have a go:

	excel_to_c <excel_file_name>

This will produce a file called excelspreadsheet.c

For a more complex spreadsheet:
	
	excel_to_c --compile --run-tests --settable <name of input worksheet> --prune-except <name of output worksheet> <excel file name> 
	
See the full list of options:

	excel_to_c --help

# Gotchas, limitations and bugs

0. No custom functions, no macros for generating results
1. Results are cached. So you must call reset(), then set values, then read values.
2. It must be possible to replace INDIRECT and OFFSET formula with standard references at compile time (e.g., INDIRECT("A"&"1") is fine, INDIRECT(userInput&"3") is not.
3. Doesn't implement all functions. [See which functions are implemented](docs/Which_functions_are_implemented.md).
4. Doesn't implement references that involve range unions and lists (but does implement standard ranges)
5. Sometimes gives cells as being empty, when excel would give the cell as having a numeric value of zero
6. The generated C version does not multithread and will give bad results if you try.
7. The generated code uses floating point, rather than fully precise arithmetic, so results can differ slightly.
8. The generated code uses the sprintf approach to rounding (even-odd) rather than excel's 0.5 rounds away from zero.
9. Ranges like this: Sheet1!A10:Sheet1!B20 and 3D ranges don't work.

Report bugs: <https://github.com/tamc/excel_to_code/issues>

# Changelog

See [Changes](CHANGES.md).

# License

See [License](LICENSE.md)

# Hacking

Source code: <https://github.com/tamc/excel_to_code>

Documentation:

* [Installing from source](docs/installing_from_source.md)
* [Structure of this project](docs/structure_of_this_project.md)
* [How does the calculation work](docs/how_does_the_calculation_work.md)
* [How to fix parsing errors](docs/How_to_fix_parsing_errors.md)
* [How to implement a new Excel function](docs/How_to_add_a_missing_function.md)

Some notes on how Excel works under the hood:

* [The Excel file structure](docs/implementation/excel_file_structure.md)
* [Relationships](docs/implementation/relationships.md)
* [Workbooks](docs/implementation/workbook.md)
* [Worksheets](docs/implementation/worksheets.md)
* [Cells](docs/implementation/cell.md)
* [Tables](docs/implementation/tables.md)
* [Shared Strings](docs/implementation/shared_strings.md)
* [Array formulae](docs/implementation/array_formulae.md)

## 官网

- 主页: http://github.com/tamc/excel_to_code
- 文档: https://www.rubydoc.info/gems/excel_to_code/0.3.20
- RubyGems: https://rubygems.org/gems/excel_to_code

## 历史版本号

- 0.3.20 (2022-01-31)
- 0.3.19 (2019-01-08)
- 0.3.18 (2019-01-05)
- 0.3.18.beta.2 (2018-12-30)
- 0.3.18.beta.1 (2018-07-16)
- 0.3.17 (2015-05-14)
- 0.3.16 (2015-05-12)
- 0.3.15 (2015-03-10)
- 0.3.14 (2015-03-10)
- 0.3.13 (2015-03-02)
- 0.3.12 (2015-02-27)
- 0.3.11 (2015-02-06)
- 0.3.10 (2015-01-16)
- 0.3.9 (2015-01-15)
- 0.3.8 (2015-01-15)
- 0.3.7 (2015-01-15)
- 0.3.5 (2014-12-18)
- 0.3.4 (2014-12-01)
- 0.3.3 (2014-10-08)
- 0.3.2 (2014-07-28)
- 0.3.1 (2014-07-25)
- 0.2.30 (2014-07-24)
- 0.2.29 (2014-07-02)
- 0.2.28 (2014-06-16)
- 0.2.27 (2014-06-16)
- 0.2.26 (2014-06-10)
- 0.2.25 (2014-05-23)
- 0.2.24 (2014-05-16)
- 0.2.23 (2014-05-07)
- 0.2.22 (2014-04-27)
- 0.2.21 (2014-04-27)
- 0.2.20 (2014-03-31)
- 0.2.19 (2014-03-18)
- 0.2.18 (2014-03-02)
- 0.2.17 (2014-02-11)
- 0.2.16 (2014-02-10)
- 0.2.15 (2014-02-06)
- 0.2.14 (2014-02-04)
- 0.2.13 (2014-02-03)
- 0.2.11 (2014-02-02)
- 0.2.10 (2014-02-01)
- 0.2.9 (2014-01-31)
- 0.2.8 (2014-01-31)
- 0.2.6 (2014-01-30)
- 0.2.7 (2014-01-30)
- 0.2.3 (2014-01-04)
- 0.2.1 (2013-12-22)
- 0.2.0 (2013-12-20)
- 0.1.23 (2013-12-04)
- 0.1.22 (2013-12-04)
- 0.1.21 (2013-11-19)
- 0.1.20 (2013-08-28)
- 0.1.18 (2013-08-22)
- 0.1.17 (2013-08-22)
- 0.1.16 (2013-08-21)
- 0.1.13 (2013-08-19)
- 0.1.12 (2013-08-01)
- 0.1.11 (2013-07-18)
- 0.1.10 (2013-06-26)
- 0.1.8 (2013-06-06)
- 0.1.6 (2013-05-03)
- 0.1.5 (2013-05-02)
- 0.1.4 (2013-03-19)
- 0.1.3 (2013-01-03)
- 0.1.2 (2012-11-14)
- 0.1.1 (2012-11-11)
- 0.0.14 (2012-10-17)
- 0.0.13 (2012-07-22)
- 0.0.11 (2012-07-18)
- 0.0.10 (2012-06-08)
- 0.0.9 (2012-06-08)
- 0.0.8 (2012-06-04)
- 0.0.7 (2012-06-01)
- 0.0.6 (2012-04-29)
- 0.0.5 (2012-04-26)
- 0.0.4 (2012-04-24)
- 0.0.2 (2012-04-17)
- 0.0.1 (2012-04-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/excel_to_code
- gem 安装: `gem install excel_to_code`
- Bundler: `gem "excel_to_code"`
- 最新版本: 0.3.20
- 最新版归档: https://rubygems.org/downloads/excel_to_code-0.3.20.gem
- 版本锁定: `gem "excel_to_code", "~> 0.3.20"`
- 中央仓库: https://rubygems.org/
