# godo

**Tag**: web, cli, testing, serialization, networking, template, filesystem, data

## 简介

go (to project) do (stuffs)  godo provides a smart way of opening a project folder in multiple terminal tabs and, in each tab, invoking a commands appropriate to that project. For example if the folder contains a Rails project the actions might include: starting mongrel, tailing one or more logs, starting consoles or IRB sessions, tailing production logs, opening an editor, running autospec, or gitk.  godo works by searching your project paths for a given search string and trying to match it against paths found in one or more configured project roots. It will make some straightforward efforts to disambiguate among multiple matches to find the one you want.  godo then uses configurable heuristics to figure out what type of project it is, for example &quot;a RoR project using RSpec and Subversion&quot;. From that it will invokes a series of action appropriate to the type of project detected with each action being run, from the project folder, in its own terminal session.  godo is entirely configured by a YAML file (~/.godo) that contains project types, heuristics, actions, project paths, and a session controller. A sample configuration file is provided that can be installed using godo --install.  godo comes with an iTerm session controller for MacOSX that uses the rb-appscript gem to control iTerm (see lib/session.rb and lib/sessions/iterm_session.rb). It should be relatively straightforward to add new controller (e.g. for Leopard Terminal.app), or a controller that works in a different way (e.g. by creating new windows instead of new tabs). There is nothing MacOSX specific about the rest of godo so creating controllers for other unixen should be straightforward if they can be controlled from ruby.  godo is a rewrite of my original 'gp' script (http://matt.blogs.it/entries/00002674.html) which fixes a number of the deficiencies of that script, turns it into a gem, has a better name, and steals the idea of using heuristics to detect project types from Solomon White's gp variant (http://onrails.org/articles/2007/11/28/scripting-the-leopard-terminal).  godo now includes contributions from Lee Marlow &lt;lee.marlow@gmail.com&gt; including support for project level .godo files to override the global configuration, support for Terminal.app, and maximum depth support to speed up the finder.  godo lives at the excellent GitHub: http://github.com/mmower/godo/ and accepts patches and forks.

## 官网

- 文档: https://www.rubydoc.info/gems/godo/1.0.8
- RubyGems: https://rubygems.org/gems/godo

## 历史版本号

- 1.0.3 (2009-07-25)
- 1.0.2 (2009-07-25)
- 1.0.1 (2009-07-25)
- 1.0.0 (2009-07-25)
- 1.0.5 (2009-07-25)
- 1.0.4 (2009-07-25)
- 1.0.8 (2009-07-25)
- 1.0.7 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/godo
- gem 安装: `gem install godo`
- Bundler: `gem "godo"`
- 最新版本: 1.0.8
- 最新版归档: https://rubygems.org/downloads/godo-1.0.8.gem
- 版本锁定: `gem "godo", "~> 1.0.8"`
- 中央仓库: https://rubygems.org/
