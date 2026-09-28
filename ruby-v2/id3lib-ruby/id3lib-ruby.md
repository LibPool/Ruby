# id3lib-ruby

**Tag**: web, security, networking, filesystem, data

## 简介

= id3lib-ruby

id3lib-ruby provides a Ruby interface to the id3lib C++ library for easily
editing ID3 tags (v1 and v2) of MP3 audio files.

The class documentation starts at ID3Lib::Tag.


== Features

* Read and write ID3v1 and ID3v2 tags
* Simple interface for adding, changing and removing frames
* Quick access to common text frames like title and performer
* Custom data frames like attached picture (APIC)
* Pretty complete coverage of id3lib's features
* UTF-16 support (warning: id3lib writes broken UTF-16 frames)
* Windows binary gem available

The CHANGES file contains a list of changes between versions.


== Installation

See INSTALL.


== Online Information

The home of id3lib-ruby is http://id3lib-ruby.rubyforge.org


== Usage

  require 'rubygems'
  require 'id3lib'

  # Load a tag from a file
  tag = ID3Lib::Tag.new('talk.mp3')

  # Get and set text frames with convenience methods
  tag.title  #=> "Talk"
  tag.album = 'X&Y'
  tag.track = '5/13'

  # Tag is a subclass of Array and each frame is a Hash
  tag[0]
  #=> { :id => :TPE1, :textenc => 0, :text => "Coldplay" }

  # Get the number of frames
  tag.length  #=> 7

  # Remove all comment frames
  tag.delete_if{ |frame| frame[:id] == :COMM }

  # Get info about APIC frame to see which fields are allowed
  ID3Lib::Info.frame(:APIC)
  #=> [ 2, :APIC, "Attached picture",
  #=>   [:textenc, :mimetype, :picturetype, :description, :data] ]

  # Add an attached picture frame
  cover = {
    :id          => :APIC,
    :mimetype    => 'image/jpeg',
    :picturetype => 3,
    :description => 'A pretty picture',
    :textenc     => 0,
    :data        => File.read('cover.jpg')
  }
  tag << cover

  # Last but not least, apply changes
  tag.update!


== Licence

This library has Ruby's licence:

http://www.ruby-lang.org/en/LICENSE.txt


== Author

Robin Stocker <robinstocker at rubyforge.org>

## 官网

- 主页: http://id3lib-ruby.rubyforge.org
- RubyGems: https://rubygems.org/gems/id3lib-ruby

## 历史版本号

- 0.6.0-x86-mswin32-60 (2010-05-16)
- 0.6.0 (2010-05-16)
- 0.5.0-mswin32 (2009-09-24)
- 0.4.1-mswin32 (2009-09-24)
- 0.4.0-mswin32 (2009-09-24)
- 0.3.1-mswin32 (2009-09-24)
- 0.3.0-mswin32 (2009-09-24)
- 0.2.1 (2009-07-25)
- 0.2.0 (2009-07-25)
- 0.1.0 (2009-07-25)
- 0.5.0 (2009-07-25)
- 0.4.1 (2009-07-25)
- 0.4.0 (2009-07-25)
- 0.3.1 (2009-07-25)
- 0.3.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/id3lib-ruby
- gem 安装: `gem install id3lib-ruby`
- Bundler: `gem "id3lib-ruby"`
- 最新版本: 0.6.0
- 最新版归档: https://rubygems.org/downloads/id3lib-ruby-0.6.0.gem
- 版本锁定: `gem "id3lib-ruby", "~> 0.6.0"`
- 中央仓库: https://rubygems.org/
