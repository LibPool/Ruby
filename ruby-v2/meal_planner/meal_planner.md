# meal_planner

**Tag**: cli, database, filesystem, data

## 简介

A program to ease and automate the planning of meals.

Each meal has a main dish and optionally side dishes as well. These are currently loaded from the meals.csv file in the directory of the command line script. That will be changed in a future release when they will be loaded from a database instead.

A menu consists of any number of days that the user chooses. Each day can have any meal as user wishes. When the program is run, the meals are loaded at random from the meal source and presented to the user. The user then has the option to switch out any that she doesn't want on a particular day. If two meals are given, the two meals are switched between each other. If only one meal is given, that meal is switched with another from the meal source that isn't already in the menu.

When the user quits the program, the current menu is stored in a menu.txt file so that it can be printed and used in shopping, preparing meals, etc.

In a future release, each dish in a meal will be associated with a recipe so that a shopping list and recipe book can be created directly from the same source.

## 官网

- 主页: https://github.com/sumsionp/meal_planner
- 文档: https://www.rubydoc.info/gems/meal_planner/1.0.1
- RubyGems: https://rubygems.org/gems/meal_planner

## 历史版本号

- 1.0.1 (2014-02-25)
- 1.0.0 (2013-12-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/meal_planner
- gem 安装: `gem install meal_planner`
- Bundler: `gem "meal_planner"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/meal_planner-1.0.1.gem
- 版本锁定: `gem "meal_planner", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
