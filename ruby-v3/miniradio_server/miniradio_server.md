# miniradio_server

**Tag**: web, networking, filesystem

## 简介

This is a basic HTTP Live Streaming (HLS) server written in Ruby using the Rack interface. It serves MP3 audio files by converting them on-the-fly into HLS format (M3U8 playlist and MP3 segment files) using `ffmpeg`. Converted files are cached for subsequent requests.
    This server is designed for simplicity and primarily targets Video on Demand (VOD) scenarios where you want to stream existing MP3 files via HLS without pre-converting them.

## 官网

- 主页: https://github.com/koichiro/miniradio_server
- 源码仓库: https://github.com/koichiro/miniradio_server.git
- RubyGems: https://rubygems.org/gems/miniradio_server

## 历史版本号

- 0.0.3 (2025-06-11)
- 0.0.2 (2025-06-11)
- 0.0.1 (2025-05-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/miniradio_server
- gem 安装: `gem install miniradio_server`
- Bundler: `gem "miniradio_server"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/miniradio_server-0.0.3.gem
- 版本锁定: `gem "miniradio_server", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
