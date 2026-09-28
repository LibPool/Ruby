# rails_source_path

**Tag**: web, testing, template, filesystem

## 简介

Remember the route prior to the current controller and redirect/use later
    In rails project, one common case is one form used to create or update
    an object can be routed from more than one page, when the object is created or updated, it
    should be redirected back to wherever it came from. Rails redirect_back doesn't work in this
    case because: 1. redirect_back in create/update action will go back to new/edit form. 2.
    usually the form is re-rendered if any error exists, which basically breaks the redirect_back.
    rails-source-path can hanlde this by explicily specifying the entry actions and remember the
    previous route in session store, hence can be used in the whole controller. Also a helper
    method is providered so it can be used in view like 'back' or 'cancel' button.

## 官网

- 主页: https://github.com/xiuzhong/rails_source_path
- 文档: https://www.rubydoc.info/gems/rails_source_path/1.0.3
- RubyGems: https://rubygems.org/gems/rails_source_path

## 历史版本号

- 1.0.3 (2020-04-18)
- 1.0.2 (2019-09-06)
- 1.0.1 (2019-09-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails_source_path
- gem 安装: `gem install rails_source_path`
- Bundler: `gem "rails_source_path"`
- 最新版本: 1.0.3
- 最新版归档: https://rubygems.org/downloads/rails_source_path-1.0.3.gem
- 版本锁定: `gem "rails_source_path", "~> 1.0.3"`
- 中央仓库: https://rubygems.org/
