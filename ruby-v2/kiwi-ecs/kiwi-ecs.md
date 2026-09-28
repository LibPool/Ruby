# kiwi-ecs

**Tag**: web, testing, networking, filesystem

## 简介

== Description

["Kiwi is a versatile entity component system focussing on fast iteration and a nice api.\n", "\n", "To get started, read the [usage guide](#usage) below.\n", "\n", "[![Tests](https://github.com/Jomy10/kiwi-ecs-ruby/actions/workflows/tests.yml/badge.svg)](https://github.com/Jomy10/kiwi-ecs-ruby/actions/workflows/tests.yml)\n", "\n", "## Installation\n", "\n", "The library is available from [ruby gems](https://rubygems.org/gems/kiwi-ecs):\n", "\n", "```sh\n", "gem install kiwi-ecs\n", "```\n", "\n", "To use it in your ruby source files:\n", "\n", "```ruby\n", "require 'kiwi-ecs'\n", "```\n", "\n", "## Usage\n", "\n", "### The world\n", "\n", "The world is the main object that controls the ecs.\n", "\n", "```ruby\n", "world = Kiwi::World.new\n", "```\n", "\n", "### Components\n", "\n", "Creating a component is as simple as declaring a struct:\n", "\n", "```ruby\n", "Position = Struct.new :x, :y\n", "```\n", "\n", "Classes can also be used instead of structs\n", "\n", "```ruby\n", "class Velocity\n", "  attr_accessor :x\n", "  attr_accessor :y\n", "end\n", "```\n", "\n", "### Entities\n", "\n", "An entity is spawned with a set of components:\n", "\n", "```ruby\n", "entityId = world.spawn(Position.new(10, 10))\n", "\n", "world.spawn(Position.new(3, 5), Velocity.new(1.5, 0.0))\n", "```\n", "\n", "The `world.spawn(*components)` function will return the id of the spawned entity.\n", "\n", "Killing an entity can be done using `world.kill(entityId)`:\n", "\n", "```ruby\n", "world.kill(entityId)\n", "```\n", "\n", "### Systems\n", "\n", "#### Queries\n", "\n", "Queries can be constructed as follows:\n", "\n", "```ruby\n", "# Query all position componentss\n", "world.query(Position) do |pos|\n", "    puts pos\n", "end\n", "\n", "# Query all entities having a position and a velocity component, and their entity ids\n", "world.query_with_ids(Position, Velocity) do |id, pos, vel|\n", "  # ...\n", "end\n", "```\n", "\n", "### Flags\n", "\n", "Entities can be tagged using flags\n", "\n", "#### Defining flags\n", "\n", "A flag is an integer\n", "\n", "```ruby\n", "module Flags\n", "  Player = 0\n", "  Enemy = 1\n", "end\n", "```\n", "\n", "#### Setting flags\n", "\n", "```ruby\n", "id = world.spawn\n", "\n", "world.set_flag(id, Flags::Player)\n", "```\n", "\n", "#### Removing a flag\n", "\n", "```ruby\n", "world.remove_flag(id, Flags::Player)\n", "```\n", "\n", "#### Checking wether an entity has a flag\n", "\n", "```ruby\n", "world.has_flag(id, Flags::Player)\n", "```\n", "\n", "#### Filtering queries with flags\n", "\n", "```ruby\n", "world.query_with_ids(Pos)\n", "  .filter do |id, pos|\n", "    world.has_flag(id, Flags::Player)\n", "  end\n", "  .each do |id, pos|\n", "    # Do something with the filtered query\n", "  end\n", "```\n", "\n", "The `hasFlags` function is also available for when you want to check multiple flags.\n", "\n", "## Road map\n", "\n", "- [ ] System groups\n", "\n", "## Contributing\n", "\n", "Contributors are welcome to open an issue requesting new features or fixes or opening a pull request for them.\n", "\n", "## License\n", "\n", "The library is licensed under LGPLv3.\n"]

## 官网

- 主页: https://github.com/jomy10/kiwi-ecs-ruby
- 文档: https://www.rubydoc.info/gems/kiwi-ecs/0.1.1
- RubyGems: https://rubygems.org/gems/kiwi-ecs

## 历史版本号

- 0.1.1 (2023-08-13)
- 0.1.0 (2023-08-11)
- 0.0.3 (2023-08-11)
- 0.0.2 (2023-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiwi-ecs
- gem 安装: `gem install kiwi-ecs`
- Bundler: `gem "kiwi-ecs"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/kiwi-ecs-0.1.1.gem
- 版本锁定: `gem "kiwi-ecs", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
