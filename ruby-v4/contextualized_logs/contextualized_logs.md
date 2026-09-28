# contextualized_logs

**Tag**: web, networking, data

## 简介

Online logging solution (like [Datadog](https://www.datadoghq.com)) have drastically transform the way we log.

An app will nowdays logs dozen (hundred) of logs per requests.

The issue is often to correlate this logs, with the initiating request (or job) and add shared metadata on this logs.

Here come `ContextualizedLogs`.

The main idea is to enhance your logs from your controller (including `ContextualizedController`, which use a before action), which will add the params to your logs (and some metadata about the request itself, like `request.uuid`).

This metadata are stored in a `ActiveSupport::CurrentAttributes` which is a singleton (reset per request).

Each subsequent logs in this thread (request) will also be enriched with this metadata, making it easier to find all the logs associated with a request (`uuid`, `ip`, `params.xxx`).

On top of this, logs can also be enriched by the ActiveRecord model they use (`create` or `find`) (models including `ContextualizedModel`). So any time a contextualized model is created or find, some metadata related to the model (`id`, ...) will also be added to the logs.

Allowing you to find all logs which "touched" this models.

## 官网

- 主页: https://github.com/babylist/contextualized_logs
- RubyGems: https://rubygems.org/gems/contextualized_logs

## 历史版本号

- 0.0.8.pre.alpha (2020-04-30)
- 0.0.7.pre.alpha (2020-04-30)
- 0.0.6.pre.alpha (2020-04-30)
- 0.0.5.pre.alpha (2020-04-26)
- 0.0.4.pre.demo (2020-04-26)
- 0.0.4.pre.alpha (2020-04-26)
- 0.0.3.pre.alpha (2020-04-25)
- 0.0.2.pre.alpha (2020-04-25)
- 0.0.1.pre.alpha (2020-04-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/contextualized_logs
- gem 安装: `gem install contextualized_logs`
- Bundler: `gem "contextualized_logs"`
- 最新版本: 0.0.8.pre.alpha
- 最新版归档: https://rubygems.org/downloads/contextualized_logs-0.0.8.pre.alpha.gem
- 版本锁定: `gem "contextualized_logs", "~> 0.0.8.pre.alpha"`
- 中央仓库: https://rubygems.org/
