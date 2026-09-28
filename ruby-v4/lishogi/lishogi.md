# lishogi

**Tag**: web, testing, serialization, networking

## 简介

# Introduction Welcome to the reference for the Lishogi API! Lishogi is free/libre, open-source shogi server forked from lichess powered by volunteers and donations.  Currently this page is a work in progress, certain information here might be wrong and incorrect! Expect it to be done during 2022. - Get help in the [Lishogi Discord channel](https://discord.gg/YFtpMGg3rR) - [Contribute to this documentation on Github](https://github.com/WandererXII/lishogi/blob/master/public/doc/lishogi-api.yaml) - Check out [Lishogi widgets to embed in your website](https://lishogi.org/developers)  ## Endpoint All requests go to `https://lishogi.org` (unless otherwise specified).  ## Rate limiting All requests are rate limited using various strategies, to ensure the API remains responsive for everyone. Only make one request at a time. If you receive an HTTP response with a [429 status](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#429), please wait a full minute before resuming API usage.  ## Streaming with ND-JSON Some API endpoints stream their responses as [Newline Delimited JSON a.k.a. **nd-json**](http://ndjson.org/), with one JSON object per line.  Here's a [JavaScript utility function (for lichess)](https://gist.github.com/ornicar/a097406810939cf7be1df8ea30e94f3e) to help reading NDJSON streamed responses.

## 官网

- 文档: https://www.rubydoc.info/gems/lishogi/0.1.0
- RubyGems: https://rubygems.org/gems/lishogi

## 历史版本号

- 0.1.0 (2024-12-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/lishogi
- gem 安装: `gem install lishogi`
- Bundler: `gem "lishogi"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/lishogi-0.1.0.gem
- 版本锁定: `gem "lishogi", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
