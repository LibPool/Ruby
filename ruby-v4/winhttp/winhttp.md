# winhttp

**Tag**: web, cli, networking, filesystem

## 简介

winhttp is a native extension that binds the asynchronous WinHTTP API into a
thin, hard-to-misuse Ruby HTTP client: system TLS via Schannel with the OS
certificate store and revocation policy, the user's proxy and PAC settings,
HTTP/2 negotiation, transparent gzip/deflate, safe redirect defaults, and
streaming downloads. Requests park the calling fiber under a Fiber scheduler
(e.g. winloop) and block plainly without one — one code path. Windows MSVC
(mswin) Ruby only.

## 官网

- 主页: https://github.com/main-path/winhttp
- 更新日志: https://github.com/main-path/winhttp/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/main-path/winhttp/issues
- RubyGems: https://rubygems.org/gems/winhttp

## 历史版本号

- 0.1.0 (2026-06-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/winhttp
- gem 安装: `gem install winhttp`
- Bundler: `gem "winhttp"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/winhttp-0.1.0.gem
- 版本锁定: `gem "winhttp", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
