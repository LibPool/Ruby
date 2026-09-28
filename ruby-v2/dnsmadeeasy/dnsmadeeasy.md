# dnsmadeeasy

**Tag**: web, cli, security, template, filesystem

## 简介

This gem ships "dmez" — a Terraform-style command line tool for the
DNS provider DnsMadeEasy.com — together with an authoritative,
fully-featured Ruby client for their REST API v2.0.

The dmez CLI manages your zones as standard DNS zone files with the
familiar read -> plan -> apply loop: "dmez zone export" writes a
canonical, TTL-lossless zone file with fixed aligned columns;
"dmez zone plan" diffs it against the live records (conservatively:
deletes are skipped by default and ambiguous record groups are
flagged for manual review); "dmez zone apply" executes the plan in
merge, add-only, or delete-only mode. Zone files can also be
validated and formatted, ANAME records are preserved as first-class
citizens (with optional --strict-rfc flattening on export), and
every account API operation is available under "dmez account".

The Ruby API supports storing credentials in
~/.dnsmadeeasy/credentials.yml, including multiple accounts and
sym-encrypted values.

ACKNOWLEDGEMENTS:

1. This gem is based on the original work contributed by Wanelo.com to the
   now abandonded "dnsmadeeasy-rest-api" client.

2. We also wish to thank the gem author Phil Cohen who
   kindly yielded the "dnsmadeeasy" RubyGems namespace to this gem.

3. We also thank Praneeth Are for contributing the support for
   secondary domains in 0.3.5.

## 官网

- 主页: https://github.com/kigster/dnsmadeeasy
- 文档: https://www.rubydoc.info/gems/dnsmadeeasy/1.0.5
- RubyGems: https://rubygems.org/gems/dnsmadeeasy

## 历史版本号

- 1.0.5 (2026-07-19)
- 1.0.3 (2026-07-18)
- 0.4.0 (2020-04-15)
- 0.3.5 (2019-12-04)
- 0.3.2 (2018-01-16)
- 0.3.1 (2018-01-12)
- 0.3.0 (2017-12-23)
- 0.2.3 (2017-12-14)
- 0.1.1 (2017-12-09)
- 0.1.0 (2017-12-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/dnsmadeeasy
- gem 安装: `gem install dnsmadeeasy`
- Bundler: `gem "dnsmadeeasy"`
- 最新版本: 1.0.5
- 最新版归档: https://rubygems.org/downloads/dnsmadeeasy-1.0.5.gem
- 版本锁定: `gem "dnsmadeeasy", "~> 1.0.5"`
- 中央仓库: https://rubygems.org/
