# rack-http-pipe

**Tag**: web, testing, security, networking, filesystem

## 简介

# Rack HTTP Pipe

Use to pipe directly a remote HTTP file without buffering it.

&gt; /!\ Do not work with WebBrick, tested with puma

## Use case

* Given a file named #HASH#.pdf on S3
* You want a clean URL and handling the authentication in front of it

```
GET http:/example.com/download

Content-Disposition: attachment;filename=name-fetched-from-db.pdf
Content-Length
Content-Type
etc.
```

## Usage

```ruby
get "/" do
  http_pipe "http://example.com/iso-ubuntu-1404-64bits", {
    status: 200,
    headers: {
      "Content-Type: application/octet-stream",
      "Content-Disposition: attachment;filename=ubuntu.iso",
    }
  }
end
```

See the example directory for an example app using sinatra

## 官网

- 主页: http://github.com/Scalingo/rack-http-pipe
- 文档: https://www.rubydoc.info/gems/rack-http-pipe/0.0.1
- RubyGems: https://rubygems.org/gems/rack-http-pipe

## 历史版本号

- 0.0.1 (2015-08-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack-http-pipe
- gem 安装: `gem install rack-http-pipe`
- Bundler: `gem "rack-http-pipe"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/rack-http-pipe-0.0.1.gem
- 版本锁定: `gem "rack-http-pipe", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
