# pikuri-vectordb

**Tag**: web, cli, networking, template, filesystem

## 简介

pikuri-vectordb gives a pikuri-core agent a +vectordb_search+
tool over a local document corpus — agentic search, the agent
decides when to retrieve. Ships a swappable backend (a
pure-Ruby +Backend::InMemory+ for teaching, plus thin
+Backend::Qdrant+ / +Backend::Chroma+ HTTP clients for
persistence — Qdrant recommended), a chunker, an
embedder wrapper over +RubyLLM.embed+, and an optional
+Reranker::LlamaServer+ that speaks +/v1/rerank+ against a
cross-encoder model. Text extraction goes through
+Pikuri::FileType.read_as_text+ in pikuri-core, which handles
plain text / Markdown / PDF; HTML extraction is a deferred
follow-up. Hosts wire the feature via
+c.add_extension Pikuri::VectorDb::Extension.new(...)+ inside
the +Agent.new+ block — same opt-in shape as +pikuri-tasks+ /
+pikuri-skills+. The bundled +Pikuri::VectorDb::LIBRARIAN+
persona is the privilege-separated sub-agent counterpart for
hosts that want recall to flow through a child rather than the
parent's context.

Three model endpoints in the full setup — chat (via ruby_llm),
an embedder (via +RubyLLM.embed+), and an optional reranker
(HTTP +/v1/rerank+). A single +llama-server+ in router mode
serves all three by default, loading each cached GGUF on
demand; see the gem's README for details.

## 官网

- 主页: https://codeberg.org/mvysny/pikuri
- 源码仓库: https://codeberg.org/mvysny/pikuri/src/branch/master
- 更新日志: https://codeberg.org/mvysny/pikuri/src/branch/master/CHANGELOG.md
- 问题追踪: https://codeberg.org/mvysny/pikuri/issues
- RubyGems: https://rubygems.org/gems/pikuri-vectordb

## 历史版本号

- 0.1.0 (2026-08-30)
- 0.0.7 (2026-06-11)
- 0.0.6 (2026-06-04)
- 0.0.5 (2026-06-04)
- 0.0.4 (2026-05-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/pikuri-vectordb
- gem 安装: `gem install pikuri-vectordb`
- Bundler: `gem "pikuri-vectordb"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pikuri-vectordb-0.1.0.gem
- 版本锁定: `gem "pikuri-vectordb", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
