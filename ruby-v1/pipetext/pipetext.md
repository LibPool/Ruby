# pipetext

**Tag**: web, cli, testing, networking, template, filesystem, data

## 简介

== Easily add colors, boxes, repetitions and emojis to your terminal output using pipes (|).
  
  Install using the Ruby Gem:
  
  > gem install pipetext
  
  Includes a library module which can be included in your code:
  
  require 'pipetext'
  
  class YellowPrinter
    include PipeText
    def print(string)
      write('|Y' + string + '|n')
    end
  end
  
  printer = YellowPrinter.new
  printer.print('This is yellow')
  
  The gem includes a command line interface too:
  
  > pipetext

  > pipetext '|Ccyan|n'

  Easily set your bash prompt colors using pipetext:

  > PS1=$(pipetext '|$|g\u|n@|g\h|n:|g\w|n$ ')

  Works with files:

  > pipetext <filename>

  Works with pipes too:

  > echo '|RRed test |u1f49c|n' | pipetext

---
  | pipe  ||  & ampersand    &&  Toggle (&) background color mode  |&
  smoke   |s  white          |W  black text on white background    |k&w
  red     |r  bright red     |R  red background      &r
  green   |g  bright green   |G  green background    &g
  blue    |b  bright blue    |B  blue background     &b
  cyan    |c  bright cyan    |C  cyan background     &c
  yellow  |y  bright yellow  |Y  yellow background   &y
  magenta |m  bright magenta |M  magenta background  &m
---
  Hex RGB color codes:    Foreground |#RRGGBB  Background      &#RRGGBB
  Palette colors (256) using Hex:    |p33&pF8  Clear Screen    |!
  black with white background        |K&w      Blinking        |@
  white with magenta background      |w&m      invert          |i
  smoke with green background        |s&g      Underlined      |_
  red with cyan background           |r&c      Italics         |~
  bright red with blue background    |R&b      Bold            |+
  green with yellow background       |g&y      Faint           |.
  bright green with red background   |G&r      Crossed out     |x
  normal color and background        |n&n      Escape Sequence |\

  Center text using current position and line end number       |{text to center}
  Add spaces to line end             |;         Set line end   |]#
  Set current x,y cursor position    |[x,y]     Terminal bell  |[bell]
  Move cursor up 1 line              |^         Hide cursor    |h
  Move cursor down 1 line            |v         Unhide cursor  |H
  Move cursor forward 1 character    |>         Sleep timer in seconds      |[#s]
  Move cursor back 1 character       |<         Sleep timer in milliseconds |[#ms]
  Capture variable  |(variable name=data)       Display variable        |(variable name)
  Add to variable   |(variable name+=data)      Subtract from variable  |(variable name-=data)
  Multiple variable |(variable name*=data)      Divide variable         |(variable name/=data)
  Copy variable to current number    |(#variable name)

  |$ toggles [ and ] around empty sequences automatically for bash command prompts

---
  Emojis:  https://unicode.org/emoji/charts/full-emoji-list.html
         |[Abbreviated CLDR Short Name]     😍 |[smiling face with heart-eyes] or
      ⚙  |[gear]   💤 |[zzz]   👨 |[man]    😍 |[sm f w he e]
      ✔  |U2714    ❌ |U274c    ☮ |u262E    💎 |u1f48e    💜 |u1f49c
---

  Single or double line box mode with |- or |=
  
                 ┌──┬──┐ ╔══╦══╗ +--+--+  <-- Draw this with this:  |15 |-[--v--] |=[--v--] |o[--v--]
                 │  │  │ ║  ║  ║ |  |  |                            |15 |-!  !  ! |=!  !  ! |o!  !  !
  123456789012345├──┴──┤ ╠══╩══╣ +--+--+           |y1234567890|g12345|n|->--^--< |=>--^--< |o>--^--< 
  15 Spaces      │     │ ║     ║ |     |                |c15|n Spaces|6 |-!     ! |=!     ! |o!     !
  (|15 )         └─────┘ ╚═════╝ +-----+                      (||15 )|9 |-{-----} |={-----} |o{-----}
  
  ┌──────────────────┐    ╔════════════════════╗            |-[|18-]|4 |g&m|=[|20-]|n&n|O
  │                  │    ║                    ║            |-!|18 !|4 |g&m|=!|20 !|n&n|O
  ├──────────────────┤    ╠════════════════════╣            |->|18-<|4 &m|g|=>|20-<|n&n|O
  │                  │    ║                    ║            |-!|18 !|4 |g&m|=!|20 !|n&n|O
  └──────────────────┘    ╚════════════════════╝            |-{|18-}|4 |g&m|={|20-}|n&n|O
---
  Repetition using | followed by the number of characters to repeat and then the character to repeat.
  |15* does the * character 15 times like this: ***************
---
==Use the ++pipetext++ command to see other options and examples.

## 官网

- 主页: https://github.com/MinaswanNakamoto/pipetext
- 文档: https://www.rubydoc.info/gems/pipetext/0.2.7
- RubyGems: https://rubygems.org/gems/pipetext

## 历史版本号

- 0.2.7 (2026-04-24)
- 0.2.6 (2026-01-24)
- 0.2.5 (2026-01-11)
- 0.2.4 (2026-01-11)
- 0.2.3 (2025-12-28)
- 0.2.2 (2025-11-28)
- 0.2.1 (2025-11-28)
- 0.2.0 (2025-11-27)
- 0.1.6 (2025-11-25)
- 0.1.5 (2025-11-23)
- 0.1.4 (2025-11-22)
- 0.1.3 (2025-11-18)
- 0.1.2 (2025-11-03)
- 0.1.1 (2025-10-26)
- 0.1.0 (2025-10-26)
- 0.0.12 (2025-10-26)
- 0.0.11 (2025-10-26)
- 0.0.10 (2025-10-26)
- 0.0.9 (2025-10-26)
- 0.0.8 (2025-10-26)
- 0.0.7 (2025-10-26)
- 0.0.6 (2025-10-19)
- 0.0.5 (2025-10-19)
- 0.0.4 (2025-10-19)
- 0.0.3 (2025-10-19)
- 0.0.2 (2025-10-19)
- 0.0.1 (2025-10-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/pipetext
- gem 安装: `gem install pipetext`
- Bundler: `gem "pipetext"`
- 最新版本: 0.2.7
- 最新版归档: https://rubygems.org/downloads/pipetext-0.2.7.gem
- 版本锁定: `gem "pipetext", "~> 0.2.7"`
- 中央仓库: https://rubygems.org/
