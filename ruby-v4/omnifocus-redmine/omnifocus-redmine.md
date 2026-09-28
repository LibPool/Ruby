# omnifocus-redmine

**Tag**: web, security, serialization, networking, filesystem, data

## 简介

Plugin for the omnifocus gem to provide synchronization with Redmine Issues.

This plugin uses the Redmine REST API. It must be enabled by an administrator
for the plugin to work.  

The first time this runs it creates a yaml file in your home directory for 
the configuration data.

* redmine_url is required. This is the base url for the redmine repository.

* user_id is required. To find your user id login and go to the my account
  page. Your user_id is the number at the end of the url for my account.

* username is optional. It is used if the redmine server requires 
  authentication.  

* password is optional. It is used if the redmine server requires 
  authentication.  

* queries is optional. It is used for custom queries or multiple queries. 
  The queries config is an array of strings.  The strings will be appended 
  to a query of the form: 

    "http://redmine_url/issues.xml?assigned_to_id=user_id"

* just_project is optional.  It is used to configure how to name the 
  omnifocus projects used for issues.  If just_project is true each redmine
  project will correspond to an omnifocus project.  If it is false the 
  omnifocus projects will be name with redmine_project-redmine_component.

Example:

    ---
    user_id: 20
    redmine_url: http://redmine/
    username: me
    password: 1234
    queries: ["status_id=1", "status_id=2"]
    just_project: false

## 官网

- 主页: https://github.com/seattlerb/omnifocus-redmine
- 文档: https://www.rubydoc.info/gems/omnifocus-redmine/1.2.6
- RubyGems: https://rubygems.org/gems/omnifocus-redmine

## 历史版本号

- 1.2.6 (2014-07-18)
- 1.2.5 (2013-07-24)
- 1.2.4 (2012-05-01)
- 1.2.3 (2011-08-16)
- 1.2.2 (2011-08-04)
- 1.2.1 (2011-07-17)
- 1.2.0 (2011-02-16)
- 1.1.0 (2011-02-09)
- 1.0.1 (2010-12-15)
- 1.0.0 (2010-12-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/omnifocus-redmine
- gem 安装: `gem install omnifocus-redmine`
- Bundler: `gem "omnifocus-redmine"`
- 最新版本: 1.2.6
- 最新版归档: https://rubygems.org/downloads/omnifocus-redmine-1.2.6.gem
- 版本锁定: `gem "omnifocus-redmine", "~> 1.2.6"`
- 中央仓库: https://rubygems.org/
