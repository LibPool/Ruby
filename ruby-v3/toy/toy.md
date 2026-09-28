# toy

**Tag**: serialization, filesystem

## 简介

Toy is a pure-Ruby transformer LM that compiles to a native binary
via Spinel. Inference (KV-cache decode on CPU/CUDA/Metal), training
(LoRA/full-FT/from-scratch via tinynn-FFI'd ggml), GGUF load + save,
Tao-compatible events.jsonl emission. As a gem, it exposes the
primitives a research project composes: tinynn FFI bridges,
the sequence-forward training graph, ViT-Tiny, the Llama / SmolLM2 /
Qwen2.5 inference cache, the GGUF loader, drift/grad/CKA observability,
cosine LR schedules, and the GGUF checkpoint writer. Filed as toy#19;
pairs with bundler-spinel / spinelgems for the consumer vendor flow.

## 官网

- 主页: https://github.com/OriPekelman/toy
- 文档: https://github.com/OriPekelman/toy#readme
- 问题追踪: https://github.com/OriPekelman/toy/issues
- RubyGems: https://rubygems.org/gems/toy

## 历史版本号

- 0.9.0 (2026-06-27)
- 0.8.0 (2026-06-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/toy
- gem 安装: `gem install toy`
- Bundler: `gem "toy"`
- 最新版本: 0.9.0
- 最新版归档: https://rubygems.org/downloads/toy-0.9.0.gem
- 版本锁定: `gem "toy", "~> 0.9.0"`
- 中央仓库: https://rubygems.org/
