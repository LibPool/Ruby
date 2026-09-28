# kematzy-dm-is-published

**Tag**: web, testing, security, networking, filesystem, data

## 简介

= dm-is-published  This plugin makes it very easy to add different states to your models, like 'draft' vs 'live'.  By default it also adds validations of the field value.  Originally inspired by the Rails plugin +acts_as_publishable+ by &lt;b&gt;fr.ivolo.us&lt;/b&gt;.    == Installation  #  Add GitHub to your RubyGems sources  $  gem sources -a http://gems.github.com  $  (sudo)? gem install kematzy-dm-is-published  &lt;b&gt;NB! Depends upon the whole DataMapper suite being installed, and has ONLY been tested with DM 0.10.0 (next branch).&lt;/b&gt;   == Getting Started  First of all, for a better understanding of this gem, make sure you study  the '&lt;tt&gt;dm-is-published/spec/integration/published_spec.rb&lt;/tt&gt;' file.  ----  Require +dm-is-published+ in your app.  require 'dm-core'         # must be required first require 'dm-is-published'  Lets say we have an Article class, and each Article can have a current state,  ie: whether it's Live, Draft or an Obituary awaiting the death of someone famous (real or rumored)   class Article include DataMapper::Resource property :id,     Serial property :title,   String ...&lt;snip&gt;  is :published  end  Once you have your Article model we can create our Articles just as normal  Article.create(:title =&gt; 'Example 1')   The instance of &lt;tt&gt;Article.get(1)&lt;/tt&gt; now has the following things for free:  * a &lt;tt&gt;:publish_status&lt;/tt&gt; attribute with the value &lt;tt&gt;'live'&lt;/tt&gt;. Default choices are &lt;tt&gt;[ :live, :draft, :hidden ]&lt;/tt&gt;.  * &lt;tt&gt;:is_live?, :is_draft? or :is_hidden?&lt;/tt&gt; methods that returns true/false based upon the state.  * &lt;tt&gt;:save_as_live&lt;/tt&gt;, &lt;tt&gt;:save_as_draft&lt;/tt&gt; or &lt;tt&gt;:save_as_hidden&lt;/tt&gt; converts the instance to the state and saves it.  * &lt;tt&gt;:publishable?&lt;/tt&gt; method that returns true for models where &lt;tt&gt;is :published &lt;/tt&gt; has been declared, but &lt;b&gt;false&lt;/b&gt; for those where it has not been declared.   The Article class also gets a bit of new functionality:  Article.all(:draft)  =&gt;  finds all Articles with :publish_status = :draft   Article.all(:draft, :author =&gt; @author_joe )  =&gt;  finds all Articles with :publish_status = :draft and author == Joe    Todo Need to write more documentation here..   == Usage Scenarios  In a Blog/Publishing scenario you could use it like this:  class Article  ...&lt;snip&gt;...  is :published :live, :draft, :hidden  end  Whereas in another scenario - like in a MenuItem model for a Restaurant - you could use it like this:  class MenuItem ...&lt;snip&gt;...  is :published  :on, :off  # the item is either on the menu or not  end   == RTFM   As I said above, for a better understanding of this gem/plugin, make sure you study the '&lt;tt&gt;dm-is-published/spec/integration/published_spec.rb&lt;/tt&gt;' file.   == Errors / Bugs  If something is not behaving intuitively, it is a bug, and should be reported. Report it here: http://github.com/kematzy/dm-is-published/issues  == Credits  Copyright (c) 2009-07-11 [kematzy gmail com]  Loosely based on the ActsAsPublishable plugin by [http://fr.ivolo.us/posts/acts-as-publishable]  == Licence  Released under the MIT license.

## 官网

- 主页: http://github.com/kematzy/dm-is-published
- 文档: https://www.rubydoc.info/gems/kematzy-dm-is-published/0.0.3
- RubyGems: https://rubygems.org/gems/kematzy-dm-is-published

## 历史版本号

- 0.0.2 (2014-08-11)
- 0.0.3 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/kematzy-dm-is-published
- gem 安装: `gem install kematzy-dm-is-published`
- Bundler: `gem "kematzy-dm-is-published"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/kematzy-dm-is-published-0.0.3.gem
- 版本锁定: `gem "kematzy-dm-is-published", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
