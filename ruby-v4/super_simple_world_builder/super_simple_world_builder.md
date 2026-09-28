# super_simple_world_builder

**Tag**: web, cli, testing, tooling, filesystem

## 简介

Version 1.0.1 Update Notes:


-Updated README "HOW TO RUN"
-I'm not sure how to format this so it looks good on the gems website so please just see the README file.



USE CASES:

1. Your friends bully you because your imaginary role playing worlds are predictable and boring.
2. You like seeing chars printed in nifty patterns.

HOW TO RUN:

1. Run `super_simple_world_builder`
2. Follow the prompts

EXAMPLE INPUT:

Guten Tag! Welcome to Super Simple World Builder.
Enter 1 to build a random world
Enter 2 to build a custom world
Please enter your selection (1, 2, or exit):
2
Enter the name of your world:
Community-Town
Enter the minimum width of the world:
15
Enter the minimum height of the world:
15
What character do you want to fill the background of your world with? (i.e. any character or single space)
 
How many lake features do you want?
3
How many mountain features do you want?
2
How many town features do you want?
3
How many forest features do you want?
4

OUTPUT:

1. Console print out of the world map
2. A text file of the world map

ACHTUNG:

1. Don't worry if the width or height entered is too small. The world will automatically enlarge to fit all features.
2. World maps look better when you enter a <space> as the character to fill the background.
3. This is a quick-and-dirty project so yolo with the specs. I added comments as a consolation prize.
4. See `feature_set.rb` to tweak the features that can be added to the world map.
5. Interestingly, menu prompts may not show up in the git bash terminal. But they do show up in Windows command prompt, so lmao.
6. Feel free to tweak the code however you like. I plan to refactor in the future to dry up some sections.

## 官网

- 文档: https://www.rubydoc.info/gems/super_simple_world_builder/1.0.1
- RubyGems: https://rubygems.org/gems/super_simple_world_builder

## 历史版本号

- 1.0.1 (2020-05-21)
- 1.0.0 (2020-05-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/super_simple_world_builder
- gem 安装: `gem install super_simple_world_builder`
- Bundler: `gem "super_simple_world_builder"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/super_simple_world_builder-1.0.1.gem
- 版本锁定: `gem "super_simple_world_builder", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
