# request_refinery

**Tag**: web, security, networking

## 简介

Creates the following tables:
                      Users
                      Roles
                      Permissions
                      ControllerFilters
                    Implements a devise authentication strategy already configured.
                    Makes available an 'authorized_to? method in application controller that returns true if the users permissions match the given permissions/list of permissions.
                    Implements whitelisting of all requests.  Every http request needs to have an associated ControllerFilter.  If the filter exists, then the current_user's permissions must satisfy the permissions required by the filter.

## 官网

- 主页: https://github.com/jnathanh/request_refinery
- 文档: https://www.rubydoc.info/gems/request_refinery/0.0.2
- RubyGems: https://rubygems.org/gems/request_refinery

## 历史版本号

- 0.0.2 (2014-10-07)
- 0.0.1 (2014-10-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/request_refinery
- gem 安装: `gem install request_refinery`
- Bundler: `gem "request_refinery"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/request_refinery-0.0.2.gem
- 版本锁定: `gem "request_refinery", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
