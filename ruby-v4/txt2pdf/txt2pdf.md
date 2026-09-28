# txt2pdf

**Tag**: cli, filesystem

## 简介

Reads a text file (if supplied as the first argument) and creates a pdf file with the same name but with .pdf as extension in the current directory via the program pdflatex (the only requirement besides ruby itself). If '-h' is the first argument, then the program displays the helptext and exits.

The program can also read the input text from STDIN (STanDard IN) and create the pdf file in the user's home directory. When this method is used, no argument is given to the program and the text is simply piped directly into the program like this: $ echo 'Hello' | txt2pdf

This would create a pdf file with only 'Hello' and the page number at the bottom of the resulting pdf page.

With this, you could map a key binding in your window manager to create a pdf file from the text you selected in any program, be it the terminal, your browser or your text editor. In my wm of choice, i3, I have added the following to my i3 config: bindsym $mod+p exec xclip -o | txt2pdf

This would create a pdf file from the text I have selected as I hit the 'Window Button' and 'p'.

## 官网

- 主页: https://isene.com/
- 源码仓库: https://github.com/isene/txt2pdf
- RubyGems: https://rubygems.org/gems/txt2pdf

## 历史版本号

- 1.1.1 (2026-03-21)
- 1.1.0 (2021-09-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/txt2pdf
- gem 安装: `gem install txt2pdf`
- Bundler: `gem "txt2pdf"`
- 最新版本: 1.1.1
- 最新版归档: https://rubygems.org/downloads/txt2pdf-1.1.1.gem
- 版本锁定: `gem "txt2pdf", "~> 1.1.1"`
- 中央仓库: https://rubygems.org/
