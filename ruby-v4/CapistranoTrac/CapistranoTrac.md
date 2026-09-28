# CapistranoTrac

**Tag**: web, networking, devops, filesystem

## 简介

== FEATURES/PROBLEMS:  * Failure is incredibly ungraceful, though generally unlikely, given that the requirements for accessing the Trac site are roughly the same as those for accessing the repository. * Currently, the trac user/pass must be the same as the SCM user/pass. It remains to be seen how much of a problem this will be.  == SYNOPSIS:  Include the recipes: require 'capistrano_trac/recipes'  For the trac tasks to work, the :trac_url variable must be set to the root of your trac site. For example: set :trac_url, &quot;http://www.yourtrachost/trac/yourproject&quot;  The 2 trac ticketing tasks are designed to be run in conjunction with a deployment or rollback, although this isn't mandatory.  To automatically document deployments and rollbacks in your capistrano deployment, add the lines:  * after &quot;deploy&quot;, &quot;trac:record_deployment&quot; * before &quot;deploy:rollback&quot;, &quot;trac:record_rollback&quot;  Order is important, otherwise the tasks will be looking at the wrong revisions.  To manually record changes, simply run the record_deployment task to document the most recent deployment changes, or the record_rollback task to document a rollback that is about to be run.  == REQUIREMENTS:  * capistrano &gt;= 2.0.0 * mechanize &gt;= 0.6.10  == INSTALL:  * sudo gem install capistrano_trac  == LICENSE:  (The MIT License)  Copyright (c) 2007 FIX  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

## 官网

- 主页: http://handle.rubyforge.org
- RubyGems: https://rubygems.org/gems/CapistranoTrac

## 历史版本号

- 0.5.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/CapistranoTrac
- gem 安装: `gem install CapistranoTrac`
- Bundler: `gem "CapistranoTrac"`
- 最新版本: 0.5.0
- 最新版归档: https://rubygems.org/downloads/CapistranoTrac-0.5.0.gem
- 版本锁定: `gem "CapistranoTrac", "~> 0.5.0"`
- 中央仓库: https://rubygems.org/
