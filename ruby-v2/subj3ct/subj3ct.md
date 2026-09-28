# subj3ct

**Tag**: web, testing, networking, filesystem, data

## 简介

==== subj3ct - The DNS for the Semantic Web

This is a Ruby adapter for the subj3ct.com webservice.

Subj3ct is an infrastructure technology for Web 3.0 applications. These are
applications that are organised around subjects and semantics rather than
documents and links. Subj3ct provides the technology and services to enable
Web 3.0 applications to define and exchange subject definitions.

Or in other words: Subj3ct.com is for the Semantic Web what DNS is for the internet.

==== Installing

Install the gem:

    gem install subj3ct

==== Usage

Query a specific subject - to be specific: its subject identity record -  using it's identifier:

 Subj3ct.identifier("http://www.topicmapslab.de/publications/TMRA_2009_subj3ct_a_subject_identity_resolution_service")

See the README or the github page for more examples.

==== Subj3ct vs. Subject

The official name is "Subj3ct", however in this API, you can also use "Subject" which may be easier to remember or to type for normal, n0n-1337 people. It should work for the gem, for the require and for the main module.

==== Contribute!

Subj3ct is a young and ambitious service. It's free, will stay free and needs your help. Contribute to this library! Create bindings for other languages! Publish your data as linked data to the web and register it with subj3ct.com.

==== Note on Patches/Pull Requests

 * Fork the project on http://github.bb/subj3ct
 * Make your feature addition or bug fix.
 * Add tests for it. This is important so I don't break it in a future version unintentionally.
 * Commit, do not mess with rakefile, version, or history. (if you want to have your own version, that is fine but bump version in a commit by itself I can ignore when I pull)
 * Send me a pull request. Bonus points for topic branches.

==== Copyright

Copyright (c) 2010 Benjamin Bock, Topic Maps Lab. See LICENSE for details.

## 官网

- 主页: http://github.com/bb/subj3ct
- 文档: http://github.com/bb/subj3ct/blob/master/README.markdown
- 问题追踪: http://github.com/bb/subj3ct/issues
- RubyGems: https://rubygems.org/gems/subj3ct

## 历史版本号

- 0.0.2 (2010-06-21)
- 0.0.1 (2010-06-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/subj3ct
- gem 安装: `gem install subj3ct`
- Bundler: `gem "subj3ct"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/subj3ct-0.0.2.gem
- 版本锁定: `gem "subj3ct", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
