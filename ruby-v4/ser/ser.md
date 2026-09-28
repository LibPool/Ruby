# ser

**Tag**: web, testing, networking, template

## 简介

Ser(ve) your web app with HTTPS to any device on your network (mDNS):
1. Use convenient domain names without ports (https://app.local vs http://127.0.0.1:3000);
2. Use mDNS for .local domains, so you can visit them from your phone or any other device connected to the same network;
3. Locally-trusted development certificates (read on filosottile/mkcert how to trust certificates on mobile devices).

Use-cases:
1. Simulate production-like subdomains (e.g., blog.example.com, api.example.com);
2. Test cookies scoped to specific domains;
3. Preview multi-tenant routing (e.g., tenant1.example.com, tenant2.example.com);
4. Use third-party APIs that need HTTPS.

## 官网

- 主页: https://github.com/3v0k4/ser
- RubyGems: https://rubygems.org/gems/ser

## 历史版本号

- 0.1.0 (2025-10-15)
- 0.1.0-x86_64-linux (2025-10-15)
- 0.1.0-x86_64-darwin (2025-10-15)
- 0.1.0-arm64-darwin (2025-10-15)
- 0.1.0-aarch64-linux (2025-10-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/ser
- gem 安装: `gem install ser`
- Bundler: `gem "ser"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/ser-0.1.0.gem
- 版本锁定: `gem "ser", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
