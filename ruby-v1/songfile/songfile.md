# songfile

**Tag**: web, filesystem, data

## 简介

BASIC INSTRUCTIONS
This gem re-ranks your playlist according to Pink Floyd band members chosen at random.
The re-ranked playlist is then exported to your current directory after the program has finished ('quit' to exit).

TO RUN DEFAULT CSV SHEET (Some songs from 'The Wall')):
songfile

TO RUN DARK SIDE OF THE MOON ALBUM SONGS:
songfile bin/DSOTM.csv

TO RUN A CSV FILE FROM YOUR CURRENT DIRECTORY:
songfile your_file_name.csv

NOTE: All CSV files must be formatted appropriately with:
No header or other text at the top!
Column 1: lists all song titles in plain text (The program will appropriately capitalize titles for you.)
Column 2: lists integer values for your song ranks (Any negative character "-" will be ignored. If left blank, a default rank of 10,000 is given.)
Low rank # means you want the song ranked higher on the playlist.
High rank # means you want the song ranked lower on the playlist.

## 官网

- 主页: http://pragmaticstudio.com
- 文档: https://www.rubydoc.info/gems/songfile/1.0.3
- RubyGems: https://rubygems.org/gems/songfile

## 历史版本号

- 1.0.3 (2022-06-24)
- 1.0.2 (2022-06-24)
- 1.0.1 (2022-06-24)
- 1.0.0 (2022-06-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/songfile
- gem 安装: `gem install songfile`
- Bundler: `gem "songfile"`
- 最新版本: 1.0.3
- 最新版归档: https://rubygems.org/downloads/songfile-1.0.3.gem
- 版本锁定: `gem "songfile", "~> 1.0.3"`
- 中央仓库: https://rubygems.org/
