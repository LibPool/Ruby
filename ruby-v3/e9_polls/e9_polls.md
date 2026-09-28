# e9_polls

**Tag**: web, database, template, tooling, filesystem, data

## 简介

** NOTE - This gem depends on e9_base, but does not reference it.  It WILL NOT FUNCTION for apps which aren't built on the e9 Rails 3 CMS **

== E9Polls

Provites a Poll renderable for the e9 Rails 3 CMS.

== Installation

1.  Include the gem and run the install generator to copy over the necessary files, 
    then migrate.
        
        rails g e9_polls:install

    This will install the db migration, the JS and CSS required for the plugin to 
    function properly, and an initializer.
    
    Modify the CSS as you see fit and the JS as required (carefully).

    Check out the initializer and modify if necessary.  For non-Ajax fallbacks it uses 
    the 'application' layout.  This should be changed if the app doesn't use application 
    layout as a sensible default.

2.  Migrate the database. 

        rake db:migrate

3.  Finally, include the generated javascript and css (e9_polls.js and e9_polls.css) 
    in the fashion suited to the app.

4.  There is no #4.

## 官网

- 主页: http://github.com/e9digital/e9_polls
- 文档: https://www.rubydoc.info/gems/e9_polls/1.0.10
- RubyGems: https://rubygems.org/gems/e9_polls

## 历史版本号

- 1.0.10 (2013-08-19)
- 1.0.9 (2011-10-14)
- 1.0.8 (2011-08-08)
- 1.0.7 (2011-07-29)
- 1.0.6 (2011-07-28)
- 1.0.5 (2011-07-28)
- 1.0.4 (2011-05-02)
- 1.0.3 (2011-05-02)
- 1.0.2 (2011-04-29)
- 1.0.1 (2011-04-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/e9_polls
- gem 安装: `gem install e9_polls`
- Bundler: `gem "e9_polls"`
- 最新版本: 1.0.10
- 最新版归档: https://rubygems.org/downloads/e9_polls-1.0.10.gem
- 版本锁定: `gem "e9_polls", "~> 1.0.10"`
- 中央仓库: https://rubygems.org/
