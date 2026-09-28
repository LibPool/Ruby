# change_requests

**Tag**: web, template

## 简介

ChangeRequests puts an approval gate in front of any action in your Rails application. Instead of running a guarded operation immediately, you record it as a change request — the service class, the method, and its arguments — and it stays pending until one ore more other actors approve. Nothing executes until someone other than the requester has signed off.

Each request moves through a guarded lifecycle: pending, approved, successful or failed, with cancellation and comments available at any point before it reaches a final state. Every transition is a small command object that validates the actor's permissions and the current status before touching the record, so invalid transitions raise rather than silently succeed. Failed requests keep their approval and can be retried.

The engine makes no assumptions about your user model. You tell it which controller methods return the current actor and their permissions, choose which routes to mount, and it stays out of the way of the rest of your app. Reference views ship with it for a working approvals screen, and every one of them can be replaced or overridden without forking the gem.

## 官网

- 主页: https://github.com/mediafinger/change_requests
- 更新日志: https://github.com/mediafinger/change_requests/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/change_requests

## 历史版本号

- 0.4.0 (2026-09-12)
- 0.3.0 (2026-09-12)
- 0.2.5 (2026-09-11)
- 0.2.2 (2026-09-11)
- 0.2.0 (2026-09-11)
- 0.1.8 (2026-09-10)
- 0.1.6 (2026-09-10)
- 0.1.0 (2026-09-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/change_requests
- gem 安装: `gem install change_requests`
- Bundler: `gem "change_requests"`
- 最新版本: 0.4.0
- 最新版归档: https://rubygems.org/downloads/change_requests-0.4.0.gem
- 版本锁定: `gem "change_requests", "~> 0.4.0"`
- 中央仓库: https://rubygems.org/
