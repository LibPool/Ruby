# tca_client

**Tag**: web, cli, security, networking, template, devops, filesystem

## 简介

Turnitin Core API (TCA) provides direct API access to the core functionality provided by Turnitin. TCA supports file submission, similarity report generation, group management, and visualization of report matches via Cloud Viewer or PDF download. Below is the full flow to successfully set up an integration scope, an API Key, and make calls to TCA. Integration Scope and API Key management is done via the Admin Console UI by logging in as an admin user. For more details, go to our [developer portal documentation page](https://developers.turnitin.com/docs). ## Integration Scope and API Key Management TCA API calls must provide an API Key for authentication, so you must first have at least one integration scope associated with at least one API Key to use TCA. ### Admin Console UI First, login to Admin Console UI as an *Admin* user with permission to create Integration Scopes, under a tenant that is licensed to use the TCA product Integration Scopes (you can create a new one, or add keys to existing)    * Click `Integrations` in the side bar --> `+ Add Integration` at top the top of the page --> Enter a name --> `Add` Button   API Keys   * Click `Integrations` in the side bar --> `Create API Key` Button next to a given Integration Scope -->   Enter a name --> click `Create and View button`   * Copy/Save the key manually or click save to clipboard button to copy it (this is the only time it will show)  ## TCA Flow    *  Register a webhook   *  Create a submission   *  Upload a file for the submission   *  Wait for the submission upload to process      * If you registered a webhook, a callback will be sent to it when upload is complete      * The status of the *submission* will also update to `COMPLETE`   *  Request a Similarity Report   *  Wait for similarity report to process      * If you registered a webhook, a callback will be sent to it when report is complete      * The status of the *report* will also be updated to `COMPLETE`   *  Request a URL with parameters to view the Similarity Report

## 官网

- 主页: https://openapi-generator.tech
- 文档: https://www.rubydoc.info/gems/tca_client/1.0.4
- RubyGems: https://rubygems.org/gems/tca_client

## 历史版本号

- 1.0.4 (2023-04-15)
- 1.0.3 (2023-04-15)
- 1.0.2 (2023-04-15)
- 1.0.1 (2022-11-22)
- 1.0.0 (2022-11-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/tca_client
- gem 安装: `gem install tca_client`
- Bundler: `gem "tca_client"`
- 最新版本: 1.0.4
- 最新版归档: https://rubygems.org/downloads/tca_client-1.0.4.gem
- 版本锁定: `gem "tca_client", "~> 1.0.4"`
- 中央仓库: https://rubygems.org/
