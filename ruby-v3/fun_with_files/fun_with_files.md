# fun_with_files

**Tag**: filesystem

## 简介

A more intuitive syntax for performing a variety of file actions. Examples:
    "/".fwf_filepath.join('usr', 'bin', 'bash').touch
    FunWith::Files::FilePath.home("Music").glob(:ext => "mp3", :recurse => true)
    home = FunWith::Files::FilePath.home
    home.touch( "Music", "CDs", "BubbleBoyTechnoRemixxxx2011", "01-jiggypalooza.mp3" )
    home.touch_dir( "Music", "CDs", "ReggaeSmackdown2008" ) do |dir|
      dir.touch( "liner_notes.txt" )
      dir.touch( "cover.jpg" )
      dir.touch( "01-tokin_by_the_sea.mp3" )
      dir.touch( "02-tourists_be_crazy_mon.mp3" )
    end

## 官网

- 主页: http://github.com/darthschmoo/fun_with_files
- 文档: https://www.rubydoc.info/gems/fun_with_files/0.0.18
- RubyGems: https://rubygems.org/gems/fun_with_files

## 历史版本号

- 0.0.18 (2024-03-20)
- 0.0.15 (2017-02-01)
- 0.0.14 (2016-06-26)
- 0.0.13 (2015-04-13)
- 0.0.12 (2015-04-13)
- 0.0.9 (2014-05-31)
- 0.0.8 (2014-05-31)
- 0.0.7 (2014-04-04)
- 0.0.6 (2014-02-02)
- 0.0.5 (2014-02-02)
- 0.0.4 (2013-12-13)
- 0.0.3 (2013-07-09)
- 0.0.2 (2013-05-22)
- 0.0.1 (2013-04-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/fun_with_files
- gem 安装: `gem install fun_with_files`
- Bundler: `gem "fun_with_files"`
- 最新版本: 0.0.18
- 最新版归档: https://rubygems.org/downloads/fun_with_files-0.0.18.gem
- 版本锁定: `gem "fun_with_files", "~> 0.0.18"`
- 中央仓库: https://rubygems.org/
