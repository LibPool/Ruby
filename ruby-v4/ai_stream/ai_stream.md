# ai_stream

**Tag**: web, filesystem, data

## 简介

A pure-Ruby, zero-dependency implementation of the Vercel AI SDK "Data Stream Protocol"
(UI Message Stream Protocol) — the Server-Sent-Events wire format that drives the AI SDK's
useChat / useCompletion / useObject frontend hooks. The protocol is language-agnostic by
design, but Ruby had no implementation; ai_stream lets a Rails/Rack backend stream text,
reasoning, tool calls, sources, files, and custom data parts to a Vercel-AI-SDK frontend
with the exact frames it expects. Provider-agnostic: it composes with ruby_llm, ruby-openai,
or any token source instead of competing with them.

## 官网

- 主页: https://consulting.levelbrook.com
- 源码仓库: https://github.com/tachyurgy/ai_stream
- 更新日志: https://github.com/tachyurgy/ai_stream/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/ai_stream

## 历史版本号

- 0.1.0 (2026-06-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/ai_stream
- gem 安装: `gem install ai_stream`
- Bundler: `gem "ai_stream"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/ai_stream-0.1.0.gem
- 版本锁定: `gem "ai_stream", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
