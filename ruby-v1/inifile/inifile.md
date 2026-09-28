# inifile

**Tag**: web, networking, filesystem, data

## 简介

Although made popular by Windows, INI files can be used on any system thanks
to their flexibility. They allow a program to store configuration data, which
can then be easily parsed and changed. Two notable systems that use the INI
format are Samba and Trac.

More information about INI files can be found on the [Wikipedia Page](http://en.wikipedia.org/wiki/INI_file).

### Properties

The basic element contained in an INI file is the property. Every property has
a name and a value, delimited by an equals sign *=*. The name appears to the
left of the equals sign and the value to the right.

    name=value

### Sections

Section declarations start with *[* and end with *]* as in `[section1]` and
`[section2]` shown in the example below. The section declaration marks the
beginning of a section. All properties after the section declaration will be
associated with that section.

### Comments

All lines beginning with a semicolon *;* or a number sign *#* are considered
to be comments. Comment lines are ignored when parsing INI files.

### Example File Format

A typical INI file might look like this:

    [section1]
    ; some comment on section1
    var1 = foo
    var2 = doodle
    var3 = multiline values \
    are also possible

    [section2]
    # another comment
    var1 = baz
    var2 = shoodle

## 官网

- 主页: http://rubygems.org/gems/inifile
- 源码仓库: https://github.com/twp/inifile
- 文档: https://www.rubydoc.info/gems/inifile/3.0.0
- 问题追踪: https://github.com/twp/inifile/issues
- RubyGems: https://rubygems.org/gems/inifile

## 历史版本号

- 3.0.0 (2014-08-01)
- 2.0.2 (2012-09-15)
- 2.0.1 (2012-09-06)
- 2.0.0 (2012-08-29)
- 1.1.0 (2012-02-28)
- 1.0.0 (2012-02-28)
- 0.4.1 (2011-02-22)
- 0.4.0 (2011-02-15)
- 0.3.0 (2009-12-10)
- 0.2.1 (2009-11-08)
- 0.2.0 (2009-10-27)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/inifile
- gem 安装: `gem install inifile`
- Bundler: `gem "inifile"`
- 最新版本: 3.0.0
- 最新版归档: https://rubygems.org/downloads/inifile-3.0.0.gem
- 版本锁定: `gem "inifile", "~> 3.0.0"`
- 中央仓库: https://rubygems.org/
