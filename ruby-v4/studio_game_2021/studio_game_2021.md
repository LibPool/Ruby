# studio_game_2021

**Tag**: web, cli, testing, networking, template, tooling, filesystem, data

## 简介

<!-- TABLE OF CONTENTS -->
<details open="open">
<summary>Table of Contents</summary>
<ol>
<li>
<a href="#about-the-project">About The Project</a>
<ul>
<li><a href="#built-with">Built With</a></li>
</ul>
</li>
<li>
<a href="#getting-started">Getting Started</a>
<ul>
<li><a href="#prerequisites">Prerequisites</a></li>
<li><a href="#installation">Installation</a></li>
</ul>
</li>
<li><a href="#usage">Usage</a></li>
<li><a href="#roadmap">Roadmap</a></li>
<li><a href="#contributing">Contributing</a></li>
<li><a href="#license">License</a></li>
<li><a href="#contact">Contact</a></li>
<li><a href="#acknowledgements">Acknowledgements</a></li>
</ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][Screenshot of gameplay and test list]](https://www.dropbox.com/s/mu1rrbx2mqowjkn/studio-game.png?dl=0)

This game is a project built following the [Pragmatic Studio Ruby Course](https://online.pragmaticstudio.com/courses/ruby/). I absolutely adored going through this course, because it was unlike other courses in that the main focus wasn't syntax, but how to build a principle-driven, object-oriented program that contains many of the skills we'd need to build real-world projects. The instructors purposefully created exercises to let us build a program using the skills they demonstrated by building a different program. This wasn't a copy and paste kind of course. This game was actually my second run-through, where I test-drove everything from the start based on the objectives only.

Skills I valued developing further with this project:
- Test-driven development (50+ tests).
- Using inheritance to model "is-a" relationships. For example, a clumsy player *is a* kind of player.
- Using mixins (modules) to reuse behaviours that are common between classes, but should not be modeled with an inheritance relationship. A good tip was to look for 'able' behaviors in a class to extract, like 'playable', 'printable', 'taxable' etc.
- Using a file block which lets you add in class usage examples that are only run when you run the class file specifically.
- Overriding default methods (like sort, and renaming things so that they keep a specific format)

Things I struggled with:
- Testing behaviour that uses blocks. I had a lightbulb moment when I realised I should test the behaviour performed inside the block on a single item. Testing the output of an entire block is like testing Ruby syntax works. Alternatively, test the before and after state of something that changes as a result of using a block. Cooool.
- Puts. It felt wrong to use puts to show the output in the console. I'd like to learn how to seperate the view logic for a command-line project later.

Things I did to make it my own:
- Wrote a lot more tests for my second run-through.
- Noticed and extracted further 'able' behaviours into modules (like printing stats, formatting output and handling csv files).


### Built With

* [Ruby (language)](https://www.ruby-lang.org/en/)
* [RSpec (framework)](https://rspec.info/)
* [Vim (text-editor)](https://www.vim.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps:

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* gem
```sh
npm install npm@latest -g
```

### Installation

1. Install the gem
```sh
gem install studio_game_2021
```

<!-- USAGE EXAMPLES -->
## Usage
To play a game from the command-line, open a new command project and run the command-line script like so:
```sh
studio_game
```

Or, if you'd like to use the game as a library, here's an example of how to use it in `irb`. You can also check the bottom of each class or module file for further usage instructions

```
>> require 'studio_game/game'
=> true

>> game = StudioGame::Game.new("Knuckleheads")
=> #<StudioGame::Game:0x007fdea10252d8 @title="Knuckleheads", @players=[]>

>> player = StudioGame::Player.new("Moe", 90)
=> I'm Moe with health = 90, points = 0, and score = 90.

>> game.add_player(player)
=> [I'm Moe with health = 90, points = 0, and score = 90.]

>> game.play(1)
```


<!-- ROADMAP -->
## Roadmap

I plan to customize this game further now that I have a solid foundation to explore from. It'll be fun to let the players interact with each other more, like swapping treasures, and maybe add some kind of board game with it's own features. That's my next focus.


## Contributing

Feel free to fork this project and play around with it. Open to feedback-related pr requests.


  <!-- LICENSE -->
## License

  Distributed under the MIT License. See `LICENSE` for more information.



  <!-- CONTACT -->
## Contact

  Becca - [@becca9941](https://twitter.com/Becca9941) - becca@essentialistdev.com

  Project Link: [https://gitlab.com/EssentialistDev/studio-game](https://gitlab.com/EssentialistDev/studio-game)



  <!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

- [Pragmatic Studio](https://online.pragmaticstudio.com/courses/ruby/) for empowering me with awesome new development skills.
- [Best-README-Template](https://github.com/Becca9941/Best-README-Template) for helping me write a README for this project.

## 官网

- 主页: https://gitlab.com/EssentialistDev/studio-game
- 文档: https://www.rubydoc.info/gems/studio_game_2021/1.0.0
- RubyGems: https://rubygems.org/gems/studio_game_2021

## 历史版本号

- 1.0.0 (2021-05-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/studio_game_2021
- gem 安装: `gem install studio_game_2021`
- Bundler: `gem "studio_game_2021"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/studio_game_2021-1.0.0.gem
- 版本锁定: `gem "studio_game_2021", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
