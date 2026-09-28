# moumar-wmainfo-rb

**Tag**: web, security, networking, filesystem, data

## 简介

:: wmainfo-rb ::
Author: Darren Kirby
mailto:bulliver@badcomputer.org
License: Ruby

 = Quick API docs =

  == Initializing ==

  require 'wmainfo'
  foo = WmaInfo.new("someSong.wma")
     ... or ...
  foo = WmaInfo.new("someVideo.wmv", :encoding=>"UTF-16LE") 
  (default encoding is ASCII)
     ... or ...
   foo = WmaInfo.new("someVideo.wmv", :debug=>1)

  == Public attributes ==

  @drm          :: 'true' if DRM present else 'false'
  @tags         :: dict of strings (id3 like data)
  @info         :: dict of variable types (non-id3 like data)
  @ext_info     :: dict of variable types (non-id3 like data) from ASF_Extended_Content_Description_Object
  @headerObject :: dict of arrays (name, GUID, size and offset of ASF objects)
  @stream       :: dict of variable types (stream properties data)

  == Public methods ==

  print_objects   :: pretty-print header objects
  hasdrm?         :: returns True if file has DRM
  hastag?('str')  :: returns True if @tags['str'] exists
  print_tags      :: pretty-print @tags dict
  hasinfo?('str') :: returns True if @info['str'] exists
  print_info      :: pretty-print @info dict
  print_stream    :: pretty-print @stream dict

  For more/different documentation see http://badcomputer.org/unix/code/wmainfo/

  == Thanks/Contributors == 

   Ilmari Heikkinen sent in a fix for uninitialized '@ext_info'.
   Guillaume Pierronnet sent in a patch which improves character encoding handling.

## 官网

- 主页: http://badcomputer.org/unix/code/wmainfo/
- RubyGems: https://rubygems.org/gems/moumar-wmainfo-rb

## 历史版本号

- 0.8 (2012-12-08)
- 0.7 (2012-04-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/moumar-wmainfo-rb
- gem 安装: `gem install moumar-wmainfo-rb`
- Bundler: `gem "moumar-wmainfo-rb"`
- 最新版本: 0.8
- 最新版归档: https://rubygems.org/downloads/moumar-wmainfo-rb-0.8.gem
- 版本锁定: `gem "moumar-wmainfo-rb", "~> 0.8"`
- 中央仓库: https://rubygems.org/
