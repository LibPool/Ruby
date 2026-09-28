# musicube_api_client_ruby

**Tag**: web, cli, security, devops, filesystem, data

## 简介

This is the Songtradr API. Use it to retrieve deep music metadata and trigger processes like auto-tagging.  You can also use the API to manage your account and musicube cloud data.  **Authentication**  1. Reach out to support@songtradr.com to receive a free account or use your login data if you are already signed up.  2. To authenticate, you need to login via the POST /api/v1/user/login endpoint.  3. The endpoint responds with a jwtToken which you can use in all following API requests as a bearer token.  **Rate Limiting**  The current limit is 120 Requests per minute. Reach out to us via support@songtradr.com if you need to request more.  **Getting Started with auto-tagging**  1. If you want to get your own files auto-tagged, use the POST /api/v1/user/file/{name}/initUpload endpoint. It responds with a presigned S3 link where you can upload your file. 2. You can check the processing status of your file via the GET /api/v1/user/file/{name}/filesStatus endpoint. 3. As soon as processing is done, you can request the generated data via the GET /api/v1/user/files endpoint.  **Getting Started with search**  You can either search the released music via the /public/recording endpoints or your own private uploaded music via the /user/file/ endpoints.  1. If you want to search the world's released music, a good starting point is the GET /api/v1/public/recording/search endpoint. Please find the extensive list of parameters that serve as semantic search filters. 2. If you want to search your own previously uploaded music, a good starting point is the GET GET /api/v1/user/files endpoint. It has the same extensive list of parameters that serve as semantic search filters.

## 官网

- 主页: https://github.com/songtradr/musicube-backend
- 文档: https://www.rubydoc.info/gems/musicube_api_client_ruby/1.1.5
- RubyGems: https://rubygems.org/gems/musicube_api_client_ruby

## 历史版本号

- 1.1.5 (2023-06-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/musicube_api_client_ruby
- gem 安装: `gem install musicube_api_client_ruby`
- Bundler: `gem "musicube_api_client_ruby"`
- 最新版本: 1.1.5
- 最新版归档: https://rubygems.org/downloads/musicube_api_client_ruby-1.1.5.gem
- 版本锁定: `gem "musicube_api_client_ruby", "~> 1.1.5"`
- 中央仓库: https://rubygems.org/
