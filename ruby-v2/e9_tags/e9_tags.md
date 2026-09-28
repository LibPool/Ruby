# e9_tags

**Tag**: web, networking, template, tooling

## 简介

== E9Tags

An extension to ActsAsTaggableOn[http://github.com/mbleigh/acts-as-taggable-on] which "improves" on custom tagging, or at least makes it more dynamic. Additionally it 
provides some autocomplete rack apps and the corresponding javascript.

== Installation

1.  E9Tags requires jquery and jquery-ui for the autocompletion and tag-adding form, be sure they're loaded in your 
    pages where the tags form will be rendered.

2.  E9Tags extends ActsAsTaggableOn and requires it.  Run it's generator if you have not.

3.  Run the E9Tags install script to copy over the required JS

        rails g e9_tags:install

4.  Then make sure it is loaded, how you do that doesn't matter, e.g.

        <%= javascript_include_tag 'e9_tags' %>

5.  Create an initializer for that sets up the taggable models and their controllers.  This gives the models the tag
    associations and methods and prepares their controller to handle the otherwise unexpected tag params.

        require 'e9_tags'
        require 'contacts_controller'
        require 'contact'

        E9Tags.controllers << ContactsController
        E9Tags.models << Contact

    OR

    You can just include the modules in your classes yourself.  The first way really exists for the case where the
    classes you wish to extend are part of another plugin/gem.

        # in contact.rb
        include E9Tags:Model

        # in contacts_controller.rb
        include E9Tags::Controller

6.  Render the tags form partial in whatever model forms require it.  

        = render 'e9_tags/form', :f => f

    If you pass a context, it will be locked and no longer possible to change/add the contexts on the form (and as 
    a side effect, the tags autocompletion will be restricted to that context).

        = render 'e9_tags/form', :f => f, :context => :users

    Finally if you pass a 2nd arg to :context you can set a tag context to be "private" (default is false).  In this
    case the tag context will be locked as private (typically suffixed with *), meaning that the tags will not be
    publicly searchable/visible.  This is useful for organizational tags tags, say if you wanted to arbitrarily
    group records, or create a custom search based on a tag context.

        = render 'e9_tags/form', :f => f, :context => [:users, true]

    NOTE: The form and javascript are intended to work out of the box, but the certainly aren't going to look pretty.
    If you do intend to use the forms, you'll no doubt need to style them.

## 官网

- 主页: http://github.com/e9digital/e9_tags
- RubyGems: https://rubygems.org/gems/e9_tags

## 历史版本号

- 0.0.14 (2011-10-07)
- 0.0.13 (2011-07-20)
- 0.0.12 (2011-05-26)
- 0.0.11 (2011-05-02)
- 0.0.10 (2011-05-02)
- 0.0.9 (2011-04-21)
- 0.0.8 (2011-04-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/e9_tags
- gem 安装: `gem install e9_tags`
- Bundler: `gem "e9_tags"`
- 最新版本: 0.0.14
- 最新版归档: https://rubygems.org/downloads/e9_tags-0.0.14.gem
- 版本锁定: `gem "e9_tags", "~> 0.0.14"`
- 中央仓库: https://rubygems.org/
