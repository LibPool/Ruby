# syc-spector

**Tag**: web, cli, testing, networking, filesystem

## 简介

== Welcome to syc-spector
 home :: https://github.com/sugaryourcoffee/syc-spector

== Description
The sycspector scans a file for patterns provided on the command line.
Lines that match the pattern are saved to a file with valid values and those lines that don't match the pattern are added to a file with invalid values.
The valid and invalid files as well as the used pattern are stored in a
history file. The saved values are used for a subsequent call to sycspector
with --show and -f for fix to show the results or to prompt the invalid values to fix them. Fixed values can be appended to the valid values file.

== Installation
sycspector can be installed as a gem from http://RubyGems.org with
  $ gem install syc-spector

== Invokation Examples
Rearches for email addresses in the provided file 'email_addresses'
  $ sycspector email_addresses -p email

Lines that are not recognized can be prompted, fixed and appended to the
valid file with
  $ sycspector -fa

To show the result of the invokation use
  $ sycspector --show

To fix the values from the input file at the first scan
  $ sycspector -f email-addresses -p email

To sort the values
  $ sycspector -s email-addresses -p email

To fix, sort and remove duplicates (individualize)
  $ sycspector -fsi email-addresses -p email

Matching patterns like 'name, firstname'
  $ syscpector name -p "\w+, \w+"

Scanning only whole lines use
  $ sycspector name -p "\A\w+, \w+\A"

If the file contains lines like "Doe, John and Doe, Jane" these won't be saved at the first scan but can be scanned with the --fix switch and appended to the valid values from the last run
  $ sycspector -fa

Fixing a specific file by specifying the invalid file as inputfile
  $ sycspector -fa 2013016-083346_invalid_name -o 2013016-083346_valid_name

Specifying the file where the results (valid and invalid) should go to
  $ sycspector -fa -o outputfile

To process all at once
  $ sycspector -fis inputfile -o outputfile -p "\A\w+, w+\Z" --show

== License
syc-spector is released under the {MIT License}[http://www.opensource.org/licenses/MIT].

## 官网

- 主页: http://syc.dyndns.org/drupal
- RubyGems: https://rubygems.org/gems/syc-spector

## 历史版本号

- 0.0.3 (2013-01-19)
- 0.0.2 (2013-01-16)
- 0.0.1 (2013-01-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/syc-spector
- gem 安装: `gem install syc-spector`
- Bundler: `gem "syc-spector"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/syc-spector-0.0.3.gem
- 版本锁定: `gem "syc-spector", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
