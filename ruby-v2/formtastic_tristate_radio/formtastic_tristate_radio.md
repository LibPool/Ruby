# formtastic_tristate_radio

**Tag**: web, template

## 简介

Have 3-state radiobuttons instead of a 2-state checkbox for your Boolean columns which can store NULL. This gem:
1. Provides a custom Formtastic input type `:tristate_radio` which renders 3 radios (“Yes”, “No”, “Unset”) instead of a checkbox (only where you put it).
2. Teaches Rails recognize `"null"` and `"nil"` param values as `nil`
3. Encourages you to add translations for ActiveAdmin “status tag” so that `nil` be correctly translated as “Unset” instead of “False”.
Does not change controls, you need to turn it on via `as: :tristate_radio` option.

## 官网

- 主页: https://github.com/sergeypedan/formtastic-tristate-radio
- 文档: https://www.rubydoc.info/gems/formtastic_tristate_radio
- 更新日志: https://github.com/sergeypedan/formtastic-tristate-radio/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/formtastic_tristate_radio

## 历史版本号

- 0.2.8 (2024-10-04)
- 0.2.7 (2022-06-10)
- 0.2.6 (2022-06-09)
- 0.2.5 (2021-11-09)
- 0.2.4 (2021-11-09)
- 0.2.3 (2021-11-09)
- 0.2.2 (2021-11-04)
- 0.2.1 (2021-11-04)
- 0.2.0 (2021-11-04)
- 0.1.0 (2021-11-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/formtastic_tristate_radio
- gem 安装: `gem install formtastic_tristate_radio`
- Bundler: `gem "formtastic_tristate_radio"`
- 最新版本: 0.2.8
- 最新版归档: https://rubygems.org/downloads/formtastic_tristate_radio-0.2.8.gem
- 版本锁定: `gem "formtastic_tristate_radio", "~> 0.2.8"`
- 中央仓库: https://rubygems.org/
