# gpt_helpr

**Tag**: cli, template, filesystem

## 简介

=== What is GptHelpr?

It is sometime necessary to provide context and explanations for your code. Instead of manually copying and formatting code snippets, GPT-Helpr automates the process with an interactive cli, generating a well-structured Markdown output, which can be copied to your clipboard or printed to file.

=== Example Usage

  # note lmk is an alias for gpt_helpr -i -ln
  $ lmk
  == 🏴‍☠️ GptHelpr 0.2.3 == Helping to dig your codebase and cook GPT-XX instructions [current directory /Users/etozzato/WorkSpace/_AINZ/pizzatarians.com]

  File Path (optional :start:end): TAB ->
  favicon.ico                 hey.md                      js                          random-acts-of-pizza.md
  _config.yml                 _site                       draft                       fonts
  images                      kneading-baking-academy.md  _exe                        academy
  favicon.gif                 hands-in-dough.md           index.md                    parties-and-events.md

  File Path (optional :start:end): hey.md 1:22
  Instructions: can you improve this text? Do you see any issues with the template?
  File Path (optional :start:end):

  # this is the generated output (also copied to the clipboard)
  ==== file source  `hey.md 1:22`

  1: ---
  2: title: Hey, hello!
  3: layout: default
  4: ---
  5:
  6: # {{ page.title }}
  7: ----
  8:
  9: <div class="row">
  10:   <div class="col-md-12">
  11:     <p class='justin'>
  12:       Nice to meet you, I am *Mek*!
  13:     </p>
  14:     <p class='listo'>
  15:       I am a self-proclaimed pizza guru and I am here to teach & learn. Originally from Venice, Italy you can find me in San Diego, CA.
  16:     </p>
  17:     <p class='listo'>
  18:       In my spare time, I write code @ PlayStation!
  19:     </p>
  20:   </div>
  21: </div>
  22:

  can you improve this text? Do you see any issues with the template?

  ==== end of  `hey.md`

## 官网

- 主页: https://www.etozzato.com
- 源码仓库: https://github.com/etozzato/gpt-helpr
- 更新日志: https://github.com/etozzato/gpt-helpr/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/gpt_helpr

## 历史版本号

- 0.2.3 (2024-07-03)
- 0.2.2 (2024-07-03)
- 0.2.1 (2024-07-03)
- 0.2.0 (2024-07-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/gpt_helpr
- gem 安装: `gem install gpt_helpr`
- Bundler: `gem "gpt_helpr"`
- 最新版本: 0.2.3
- 最新版归档: https://rubygems.org/downloads/gpt_helpr-0.2.3.gem
- 版本锁定: `gem "gpt_helpr", "~> 0.2.3"`
- 中央仓库: https://rubygems.org/
