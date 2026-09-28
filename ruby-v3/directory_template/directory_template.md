# directory_template

**Tag**: serialization, template, filesystem

## 简介

DirectoryTemplate is a library which lets you generate directory structures and files
from a template structure. The template structure can be a real directory structure on
the filesystem, or it can be stored in a yaml file. Take a look at the examples directory
in the gem to get an idea, how a template can look.

When generating a new directory structure from a template, DirectoryTemplate will process
the pathname of each directory and file using the DirectoryTemplate#path_processor.
It will also process the contents of each file with all processors that apply to a given
file.
The standard path processor allows you to use `%{variables}` in pathnames. The gem comes
with a .erb (renders ERB templates) and .html.markdown processor (renders markdown to
html).
You can use the existing processors or define your own ones.

## 官网

- 主页: https://github.com/apeiros/directory_template
- RubyGems: https://rubygems.org/gems/directory_template

## 历史版本号

- 1.0.1 (2012-05-03)
- 1.0.0 (2012-05-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/directory_template
- gem 安装: `gem install directory_template`
- Bundler: `gem "directory_template"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/directory_template-1.0.1.gem
- 版本锁定: `gem "directory_template", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
