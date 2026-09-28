# javascript_util_asset_pack

**Tag**: web, networking, template, tooling, filesystem, data

## 简介

== Rails 3.1 javascript - Util asset pack

== Sets up a window.Util object which includes

* Spinner, with methods to set spinner next to element or hide the spinner
* AjaxForm, to ajax enable simple forms
* jQuery ajaxError global handler, exception data during development and friendly message in production

== Usage

spinner (js version)

    window.Util.spinner.nextTo('#my_button');
    window.Util.spinner.nextTo('#my_button', 3, 4); // selector, top offset, left offset
    window.Util.spinner.hide();

ajax form (coffee script version)

    jQuery ->
        new window.Util.AjaxForm '#my_form', ->
            log "my_form submit success callback"

== Install

Update the Gemfile in your rails project, add the following line

    gem 'javascript_util_asset_pack'

Run the generator

    rails generate javascript_util_asset_pack

does the following:

* Copy spinner.gif to /app/assets/images
* Update application.html.erb adding javascript create window.Rails.env variable
* Update application.html.erb adding image_tag for spinner.gif
* Update application.js adding util_pack

== WARNING

* 0.0.10 and 0.0.11 are bad versions, use 0.0.12 or above

== Coming Soon

* configuration object
  * text in ajaxError overrides
  * spinner id override

== Resources

* spinner.gif generated using http://www.ajaxload.info

== License

The Unlicense (aka: public domain)
http://unlicense.org

== Ruby Gems

* https://rubygems.org/gems/javascript_util_asset_pack

## 官网

- 主页: https://github.com/house9/javascript_util_asset_pack
- 文档: https://www.rubydoc.info/gems/javascript_util_asset_pack/0.2.0
- RubyGems: https://rubygems.org/gems/javascript_util_asset_pack

## 历史版本号

- 0.2.0 (2013-12-04)
- 0.2.0.rc2 (2013-12-04)
- 0.2.0.rc1 (2013-12-04)
- 0.1.0 (2013-05-31)
- 0.0.12 (2012-12-01)
- 0.0.11 (2012-12-01)
- 0.0.10 (2012-12-01)
- 0.0.9 (2012-03-02)
- 0.0.8 (2012-02-07)
- 0.0.7.rc (2012-02-07)
- 0.0.6.rc (2012-02-07)
- 0.0.5.rc (2012-01-26)
- 0.0.4 (2011-06-28)
- 0.0.3 (2011-06-28)
- 0.0.2 (2011-06-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/javascript_util_asset_pack
- gem 安装: `gem install javascript_util_asset_pack`
- Bundler: `gem "javascript_util_asset_pack"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/javascript_util_asset_pack-0.2.0.gem
- 版本锁定: `gem "javascript_util_asset_pack", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
