# game_2d

**Tag**: web, cli, testing, networking, tooling

## 简介

Built on top of Gosu, an engine for making 2-D games.  Gosu provides the means
to handle the graphics, sound, and keyboard/mouse events.  It doesn't provide
any sort of client/server network architecture for multiplayer games, nor a
system for tracking objects in game-space.  This gem aims to fill that gap.

Originally I tried using Chipmunk as the physics engine, but its outcomes were
too unpredictable for the client to anticipate the server.  It was also hard to
constrain in the ways I wanted.  So I elected to build something integer-based.

In the short term, I'm throwing anything into this gem that interests me.  There
are reusable elements (GameSpace, Entity, ServerPort), and game-specific
elements (particular Entity subclasses with custom behaviors).  Longer term, I
could see splitting it into two gems.  This gem, game_2d, would retain the
reusable platform classes.  The other classes would move into a new gem specific
to the game I'm developing, as a sort of reference implementation.

## 官网

- 主页: https://github.com/sereneiconoclast/game_2d
- 文档: https://www.rubydoc.info/gems/game_2d/0.0.3
- RubyGems: https://rubygems.org/gems/game_2d

## 历史版本号

- 0.0.3 (2014-12-13)
- 0.0.2 (2014-12-01)
- 0.0.1 (2014-11-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/game_2d
- gem 安装: `gem install game_2d`
- Bundler: `gem "game_2d"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/game_2d-0.0.3.gem
- 版本锁定: `gem "game_2d", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
