# authorizer

**Tag**: web, security, filesystem

## 简介

Authorizer is a gem for Ruby (in conjunction with Rails 2.3) that does authorization for you on a per-object basis. What makes this gem different from e.g. declarative_authorization and cancan is they define one role for the entire application. With Authorizer, you define roles for different users on every Rails object.

Let's use a Dropbox analogy.

With Dropbox, you can choose which folder you want to share. For instance:

Al has a home folder with these subfolders in it:
 - Music (shared with Bob)
 - Pictures (shared with Casper and Bob)
 - News (shared with no-one)
 
This causes Al to have all 3 folders in his Dropbox. Bob has 2 and Casper has only 1 folder called Pictures. 

In other words, a user has access to a subset of the entire collection of folders. Bob has access to 2 of Al's folders, namely Music and Pictures. But he doesn't even see the News folder, nor can he download files from it. 

Bob's access to the two folders is both read and write, so let's call that role "admin". Al is the owner of all 3 folders and has a role called "owner". This leads to the following Roles table:

 folder_name	user_name           role
 Music		Al                  owner
 		Bob                 admin
 Pictures	Al                  owner
 		Bob                 admin
 		Casper              admin
 News		Al                  owner

Now if we would allow Bob to also access the News folder but only read from it, we could add the role called "reader" to the table:

 folder_name	user_name           role
 News		Bob                 reader

This is exactly what Authorizer does for your Rails application.

## 官网

- 主页: https://github.com/cmdjohnson/authorizer
- RubyGems: https://rubygems.org/gems/authorizer

## 历史版本号

- 0.0.6 (2012-03-05)
- 0.0.5 (2011-12-30)
- 0.0.4 (2011-10-12)
- 0.0.3 (2011-10-03)
- 0.0.2 (2011-08-22)
- 0.0.1 (2011-07-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/authorizer
- gem 安装: `gem install authorizer`
- Bundler: `gem "authorizer"`
- 最新版本: 0.0.6
- 最新版归档: https://rubygems.org/downloads/authorizer-0.0.6.gem
- 版本锁定: `gem "authorizer", "~> 0.0.6"`
- 中央仓库: https://rubygems.org/
