# ask-web-fetch-mcp

**Tag**: web, cli, networking, template

## 简介

A minimal MCP (Model Context Protocol) server that exposes ask_web_fetch
as a callable tool over stdio. Designed for use with clients that support MCP
(ZCode, Claude Code, etc.), it fetches a URL and returns clean markdown through
the ask-web-fetch backend chain — fast pure-Ruby httpx fetch first, a real
Chrome (launched or CDP-attached) for JS-rendered and challenge-gated pages,
with Jina Reader and self-hosted Crawl4AI in between. Terminal failures
(parked domains, empty pages, dead 4xx) surface as their deterministic error
class, so clients never retry the unretryable. The tool shell (name, schema,
call) lives here, wrapping the Ask::WebFetch library.

## 官网

- 主页: https://github.com/ask-rb/ask-web-fetch-mcp
- 更新日志: https://github.com/ask-rb/ask-web-fetch-mcp/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/ask-web-fetch-mcp

## 历史版本号

- 0.7.6 (2026-09-22)
- 0.7.5 (2026-09-22)
- 0.7.4 (2026-09-17)
- 0.7.3 (2026-09-10)
- 0.7.2 (2026-09-10)
- 0.7.1 (2026-09-08)
- 0.7.0 (2026-09-08)
- 0.6.9 (2026-09-08)
- 0.6.8 (2026-09-08)
- 0.6.6 (2026-09-08)
- 0.6.5 (2026-09-08)
- 0.6.3 (2026-08-18)
- 0.6.2 (2026-08-18)
- 0.6.1 (2026-08-12)
- 0.6.0 (2026-08-12)
- 0.5.0 (2026-08-12)
- 0.4.1 (2026-08-11)
- 0.4.0 (2026-08-10)
- 0.3.0 (2026-08-08)
- 0.2.0 (2026-08-04)
- 0.1.0 (2026-08-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/ask-web-fetch-mcp
- gem 安装: `gem install ask-web-fetch-mcp`
- Bundler: `gem "ask-web-fetch-mcp"`
- 最新版本: 0.7.6
- 最新版归档: https://rubygems.org/downloads/ask-web-fetch-mcp-0.7.6.gem
- 版本锁定: `gem "ask-web-fetch-mcp", "~> 0.7.6"`
- 中央仓库: https://rubygems.org/
