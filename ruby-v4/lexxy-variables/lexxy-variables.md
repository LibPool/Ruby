# lexxy-variables

**Tag**: template

## 简介

Insert and safely resolve variables in Lexxy rich text. The gem gives you an
editor button (and a `{{` prompt) for inserting variables, each stored as an
Action Text attachment chip rather than literal markup. `with_variables`
resolves the chips and returns plain Action Text content. Register new chip types
with `register_attachment`. A :text chip resolves to an escaped string, an
:html chip splices rich content in before sanitization. Liquid is optional.
The default renderer is plain, injection-safe string substitution and pulls
in no template engine.

## 官网

- 主页: https://github.com/anquinn/lexxy-variables
- 更新日志: https://github.com/anquinn/lexxy-variables/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/anquinn/lexxy-variables/issues
- RubyGems: https://rubygems.org/gems/lexxy-variables

## 历史版本号

- 0.0.5 (2026-07-19)
- 0.0.4 (2026-07-14)
- 0.0.3 (2026-07-13)
- 0.0.2 (2026-07-07)
- 0.0.1 (2026-07-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/lexxy-variables
- gem 安装: `gem install lexxy-variables`
- Bundler: `gem "lexxy-variables"`
- 最新版本: 0.0.5
- 最新版归档: https://rubygems.org/downloads/lexxy-variables-0.0.5.gem
- 版本锁定: `gem "lexxy-variables", "~> 0.0.5"`
- 中央仓库: https://rubygems.org/
