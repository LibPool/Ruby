# ottogen

**Tag**: web, cli, serialization, networking, template, tooling, filesystem, data

## 简介

# Otto

AsciiDoc-powered static site generator with Jekyll-style conventions: layouts, includes, data files, posts, drafts, permalinks, and custom collections.

## Install

```sh
gem install ottogen
```

Requires Ruby 3.0 or newer.

## Quickstart

```sh
mkdir mysite && cd mysite
otto init
otto build
otto serve
open http://127.0.0.1:8778/
```

For a longer walkthrough including AsciiDoc syntax, see [GUIDE.md](GUIDE.md).

## Commands

| Command | Description |
|---|---|
| `otto init [DIR]` | Scaffold a new site (current dir if omitted) |
| `otto build` | Render the site to `_build/` |
| `otto build --drafts` | Include posts from `_drafts/` |
| `otto watch` | Rebuild on file change |
| `otto serve` | Serve `_build/` on port 8778 |
| `otto generate PAGE` | Create a new page in `pages/` |
| `otto post "Title"` | Create a new dated post in `_posts/` |
| `otto clean` | Delete `_build/` |
| `otto doctor` | Sanity-check project layout |

## Project layout

```
my-site/
├── .otto                 # marker
├── config.yml            # site config
├── assets/               # copied verbatim into _build/
├── pages/                # AsciiDoc pages, output mirrors path
├── _layouts/             # ERB layouts (.html.erb)
├── _includes/            # ERB partials
├── _data/                # YAML/JSON files exposed as site.data.*
├── _posts/               # YYYY-MM-DD-slug.adoc
└── _drafts/              # undated drafts (excluded by default)
```

## Configuration (`config.yml`)

```yaml
title: My Otto Site
description: Things I write
url: https://example.com
baseurl: ""

permalink: /:year/:month/:day/:slug/

collections:
  recipes:
    output: true
```

`permalink` accepts these tokens: `:year`, `:month`, `:day`, `:slug`, `:title`. Templates ending in `/` produce pretty URLs (`<path>/index.html`).

## Pages and posts

Both support YAML front matter:

```adoc
---
layout: default
title: Hello
tags: [ruby, cli]
---
= Hello

Welcome to {site_title}. This page is at {page_url}.
```

Pages live under `pages/`; posts under `_posts/` with `YYYY-MM-DD-slug.adoc` names. Layouts wrap rendered AsciiDoc; partials in `_includes/` are pulled in via `<%= partial 'header.html' %>`.

## License

MIT

## 官网

- 主页: https://www.tacoda.dev/otto/
- 文档: https://www.rubydoc.info/gems/ottogen/1.0.0
- RubyGems: https://rubygems.org/gems/ottogen

## 历史版本号

- 1.0.0 (2026-05-01)
- 0.2.0 (2025-04-20)
- 0.1.0 (2025-04-17)
- 0.0.1 (2022-10-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/ottogen
- gem 安装: `gem install ottogen`
- Bundler: `gem "ottogen"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/ottogen-1.0.0.gem
- 版本锁定: `gem "ottogen", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
