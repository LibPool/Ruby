# layeredyamlconfig

**Tag**: web, serialization, template, filesystem

## 简介

LayeredYAMLConfig provides a simple config file that supports multiple
layers.  Values in the right or uppermost layers override values in lower
layers.  This makes it easy to share configuration without duplication while
still allowing what needs to be different to vary.

For example:

    program.default.conf
    program.server_foo.conf
    program.site_bar.conf
    program.conf

Optionally, leaf nodes can be evaluated using as ERB templates, feeding the
configuration into itself.

## 官网

- 主页: https://github.com/jf647/LayeredYAMLConfig
- 文档: https://www.rubydoc.info/gems/layeredyamlconfig/1.4.4
- RubyGems: https://rubygems.org/gems/layeredyamlconfig

## 历史版本号

- 1.4.4 (2013-09-24)
- 1.4.3 (2013-09-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/layeredyamlconfig
- gem 安装: `gem install layeredyamlconfig`
- Bundler: `gem "layeredyamlconfig"`
- 最新版本: 1.4.4
- 最新版归档: https://rubygems.org/downloads/layeredyamlconfig-1.4.4.gem
- 版本锁定: `gem "layeredyamlconfig", "~> 1.4.4"`
- 中央仓库: https://rubygems.org/
