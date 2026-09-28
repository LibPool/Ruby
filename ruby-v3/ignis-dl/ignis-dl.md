# ignis-dl

**Tag**: library

## 简介

ignis-dl is the deep-learning layer of the Ignis ecosystem: NN modules
(Linear, Embedding, LayerNorm, RMSNorm, Dropout), optimizers (SGD/Adam/AdamW),
losses, and a transformer stack (multi-head + grouped-query attention, RoPE,
SwiGLU, KV cache) with HuggingFace weight loaders (GPT-2, Llama). Loads real
GPT-2 and Llama-3.2 checkpoints and matches HuggingFace logits, and trains
transformers from scratch — in Ruby, on native Windows. Installing this pulls
the whole stack (ignis + ignis-autograd), so it also serves as the meta-gem.

## 官网

- 主页: https://github.com/tigel-agm/Ignis
- RubyGems: https://rubygems.org/gems/ignis-dl

## 历史版本号

- 0.0.1 (2026-05-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/ignis-dl
- gem 安装: `gem install ignis-dl`
- Bundler: `gem "ignis-dl"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/ignis-dl-0.0.1.gem
- 版本锁定: `gem "ignis-dl", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
