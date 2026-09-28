# hexflex

**Tag**: web, testing, security, networking, template, tooling, filesystem

## 简介

# Hexflex
[![Build Status](https://travis-ci.org/aauthor/hexflex.svg?branch=master)](https://travis-ci.org/aauthor/hexflex)

Hexflex is a Ruby gem and command-line tool for automatically generating
[hexaflexagon] templates.

## Installation

    gem install 'hexaflexa'

...or you can put it in your Gemfile.

## Usage

### as a gem in your ruby project

To create an [RVG] object containing a vector of the hexaflexagon template:

    Hexflex.make_template_vector(side_fills: ARRAY_OF_SIDE_FILLS, template: TEMPLATE)

To save the hexaflexagon template as a file to the disk:

    Hexflex.create_template_image!(side_fills: ARRAY_OF_SIDE_FILLS, template: TEMPLATE, output_file_name: OUTPUT)

Where:
- a `SIDE_FILL` is a [standard X color] or path to file for a side of the hexaflexagon.  Either three or zero sides should be specified.  The default are cyan, magenta, and yellow.
- `TEMPLATE` is template the form for the hexaflexagon. It can either be "tape" or "glue". The default is "tape".
- `OUTPUT` is a path to save the hexaflexagon template image. The default is "out.png".

### as a command-line tool

    hexflex [-s SIDE_FILL -s SIDE_FILL -s SIDE_FILL] [-t TEMPLATE] [-o OUTPUT]

See above for definitions of `SIDE_FILL`, `TEMPLATE`, AND `OUTPUT`.

[hexaflexagon]: https://en.wikipedia.org/wiki/Flexagon#Trihexaflexagon
[standard X color]: https://en.wikipedia.org/wiki/X11_color_names
[RVG]: https://rmagick.github.io/rvg.html

## 官网

- 主页: http://github.com/aauthor/hexflex
- 文档: https://www.rubydoc.info/gems/hexflex/1.0.0
- RubyGems: https://rubygems.org/gems/hexflex

## 历史版本号

- 1.0.0 (2016-02-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/hexflex
- gem 安装: `gem install hexflex`
- Bundler: `gem "hexflex"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/hexflex-1.0.0.gem
- 版本锁定: `gem "hexflex", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
