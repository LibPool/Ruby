# feratel-check-api-client

**Tag**: web, cli, security

## 简介

This documentation describes your available CheckAPI REST services: Get your checkpoints and their details, check the permission of a customer's ID, take a look at your checkpoint's history - everything a checkpoint needs can be found here in one place.  Please look at the descriptions in each service below.  <div id="authorize-information-wrap"><h1>Authorize</h1><p>You can use this automated authentication to try out your activated methods - just click „Authorize“, enter CardAPI credentials and have a try! You received the CardAPI username and password via e-mail – credentials are different from your developer-portal credentials. Authentication is based on OAUTH2 (implicit grant flow) and needs to be implemented and called prior to using any API method.  <b>CLIENT_ID</b><br>The client ID is pre-filled automatically according to the chosen application. You can find your available client IDs in the "Applications" - Area.  <b>GRANT_TYPE</b><br>With grant_type=password you get an access-token and a refresh-token for your request. The received access token can be used for 10 minutes, there are two ways to renew it. Either you can send the same request again or you can use the grant_type=refresh_token. The refresh token needs to be used every 30 minutes and can provide new access tokens for 10 hours without using your credentials.</p></div>

## 官网

- 文档: https://www.rubydoc.info/gems/feratel-check-api-client/1.0.0
- RubyGems: https://rubygems.org/gems/feratel-check-api-client

## 历史版本号

- 1.0.0 (2024-08-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/feratel-check-api-client
- gem 安装: `gem install feratel-check-api-client`
- Bundler: `gem "feratel-check-api-client"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/feratel-check-api-client-1.0.0.gem
- 版本锁定: `gem "feratel-check-api-client", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
