# htmlsafeslip

**Tag**: web, template

## 简介

htmlsafeslip parses Ruby source with Ripper to find a call to
`.html_safe` directly on an expression, or a `raw(...)` wrapping one,
where that expression is traceable (directly, or via a same-method
local-variable assignment) to `params[...]`/`params.dig(...)`, with no
`sanitize(...)`/`strip_tags(...)`/`h(...)`/`ERB::Util.html_escape(...)`
call applied to it first. Both `.html_safe` and `raw(...)` tell Rails'
view layer "this string is already safe HTML, don't auto-escape it" --
calling either directly on unsanitized, user-controlled input defeats
Rails' single biggest built-in XSS defense, turning a reflected or
stored script-tag payload into live, executing HTML the instant it's
rendered.

## 官网

- 主页: https://github.com/jay-tank/htmlsafeslip
- RubyGems: https://rubygems.org/gems/htmlsafeslip

## 历史版本号

- 0.1.0 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/htmlsafeslip
- gem 安装: `gem install htmlsafeslip`
- Bundler: `gem "htmlsafeslip"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/htmlsafeslip-0.1.0.gem
- 版本锁定: `gem "htmlsafeslip", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
