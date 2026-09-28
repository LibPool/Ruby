# selenium-webdriver-element-extend_click_again

**Tag**: web, cli, template, tooling

## 简介

Selenium::WebDriver::Element#click sometimes fails because the element is not clickable and other element receives the click.
This gem extends `click` to avoid that.
When `click` fails with `not clickable` error, this tries to center the element with executing JavaScript `Element.scrollIntoView()` and click it again.

## 官网

- 主页: https://github.com/oieioi/selenium-webdriver-element-extend_click_again
- 文档: https://www.rubydoc.info/gems/selenium-webdriver-element-extend_click_again/0.1.1
- RubyGems: https://rubygems.org/gems/selenium-webdriver-element-extend_click_again

## 历史版本号

- 0.1.1 (2019-07-22)
- 0.1.0 (2019-07-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/selenium-webdriver-element-extend_click_again
- gem 安装: `gem install selenium-webdriver-element-extend_click_again`
- Bundler: `gem "selenium-webdriver-element-extend_click_again"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/selenium-webdriver-element-extend_click_again-0.1.1.gem
- 版本锁定: `gem "selenium-webdriver-element-extend_click_again", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
