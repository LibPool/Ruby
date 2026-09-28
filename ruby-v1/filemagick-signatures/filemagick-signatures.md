# filemagick-signatures

**Tag**: web, serialization, networking, template, filesystem

## 简介

This module contains the signatures for use either independently or via the
`filemagick` gem. The various file signatures currently supported are taken
from [Gary Kessler's website][http://www.garykessler.net/library/file_sigs.html]


The signatures are stored in a YAML file in the following format:

```yaml
- mime: 'application/pdf'
  extensions:
    - 'pdf'
  signatures:
    starting:
      offset: 0
      hexcodes:
        - '25504446'
    trailing:
      offset: 0
      hexcodes:
        - '0a2525454f46'
        - '0a2525454f460a'
        - '0d0a2525454f460d0a'
        - '0d2525454f460d'
```

## 官网

- 文档: https://www.rubydoc.info/gems/filemagick-signatures/0.0.1
- RubyGems: https://rubygems.org/gems/filemagick-signatures

## 历史版本号

- 0.0.1 (2014-10-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/filemagick-signatures
- gem 安装: `gem install filemagick-signatures`
- Bundler: `gem "filemagick-signatures"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/filemagick-signatures-0.0.1.gem
- 版本锁定: `gem "filemagick-signatures", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
