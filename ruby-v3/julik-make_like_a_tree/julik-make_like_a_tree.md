# julik-make_like_a_tree

**Tag**: security

## 简介

Implement orderable trees in ActiveRecord using the nested set model, with multiple roots and scoping, and most importantly user-defined ordering of subtrees. Fetches preordered trees in one go, updates are write-heavy.  This is a substantially butchered-up version/offspring of acts_as_threaded. The main additional perk is the ability to reorder nodes, which are always fetched ordered. Example:  root = Folder.create! :name =&gt; "Main folder" subfolder_1 = Folder.create! :name =&gt; "Subfolder", :parent_id =&gt; root.id subfolder_2 = Folder.create! :name =&gt; "Another subfolder", :parent_id =&gt; root.id  subfolder_2.move_to_top # just like acts_as_list but nestedly awesome root.all_children # =&gt; [subfolder_2, subfolder_1]  See the rdocs for examples the method names. It also inherits the awesome properties of acts_as_threaded, namely materialized depth, root_id and parent_id values on each object which are updated when nodes get moved.  Thanks to the authors of acts_as_threaded, awesome_nested_set, better_nested_set and all the others for inspiration.

## 官网

- 主页: http://github.com/julik/make_like_a_tree
- 文档: https://www.rubydoc.info/gems/julik-make_like_a_tree/1.0.3
- RubyGems: https://rubygems.org/gems/julik-make_like_a_tree

## 历史版本号

- 1.0.1 (2014-08-11)
- 1.0.2 (2014-08-11)
- 1.0.3 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/julik-make_like_a_tree
- gem 安装: `gem install julik-make_like_a_tree`
- Bundler: `gem "julik-make_like_a_tree"`
- 最新版本: 1.0.3
- 最新版归档: https://rubygems.org/downloads/julik-make_like_a_tree-1.0.3.gem
- 版本锁定: `gem "julik-make_like_a_tree", "~> 1.0.3"`
- 中央仓库: https://rubygems.org/
