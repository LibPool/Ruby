# flickru

**Tag**: web, cli, testing, networking, filesystem, data

## 简介

Command-line tool that automatises photo/video uploads to Flickr.

Entering 'flickru <directory>' in your command line, any photos under 'directory' (and subdirs)
are uploaded to your Flickr account (interactively entered the first time you start flickru).

Photos are identified by case-insensitive extensions: GIF, JPEG, JPG, PNG, and TIFF.
Videos are identified by case-insensitive extensions: AVI, MPEG, and MPG.

flickru automatically sets the following Flickr metadata:
 (1) date taken: file last-modification time, unless JPEG/TIFF Exif metadatum
     'date_time_original' is found (Flickr understands it natively).
 (2) privacy policy: private, visible by friends & family, hidden for public
     searches
 (3) safety level: safe
 (4) permissions: friends & family can add comments to the photo and its notes;
     nobody can add notes and tags to the photo
 (5) description: for videos longer than 90s (Flickr's longest allowed duration)
     but shorter than 500MB (Flickr's maximum permisible size), it will contain
     an annotation about its large duration.
 (6) title: extracted from the parent directory name
 (7) geolocation & accuracy: extracted from the parent directory name, unless
     JPEG/TIFF Exif GPS metadata is found (Flickr understands them natively).

Before uploading photos, please, make sure that you have correctly named each
photos parent directory according to the name format 'TITLE[@LOCATION[#PRECISION]]',
where:
 (1) TITLE is the desired title for the photos stored in the directory. If no
     LOCATION is given, flickru tries to extract the location from Wikipedia
     page TITLE.
 (2) LOCATION is the location of the photos, specified as:
   (a) the Wikipedia page name (whitespaces allowed) of the location or
   (b) its coordinates LATITUDE,LONGITUDE
 (3) PRECISION is the Flickr geolocation precision. Flickru sets it to one of
     the following case insentitive literals: 'street', 'city', 'region',
     'country', 'world'.

Photos are classified into photosets. If the photoset does not exist, flickru
creates it. This photoset is named after its grandparent directory. The
photoset is arranged by 'date taken' (older first).

To see some examples on the directory structure recognised by flickru, please
explore the subdirectories under 'var/ts'.

GitHub  : http://github.com/jesuspv/flickru
RubyGems: http://rubygems.org/gems/flickru

## 官网

- 主页: http://github.com/jesuspv/flickru
- 文档: https://www.rubydoc.info/gems/flickru/0.6.5
- RubyGems: https://rubygems.org/gems/flickru

## 历史版本号

- 0.6.5 (2018-12-02)
- 0.6.4 (2018-12-02)
- 0.6.0 (2016-11-05)
- 0.5.1 (2016-10-17)
- 0.5.0 (2016-10-16)
- 0.4.4 (2016-10-15)
- 0.4.3 (2016-09-30)
- 0.4.2 (2016-09-30)
- 0.4.0 (2013-11-16)
- 0.3.0 (2013-08-30)
- 0.2.2 (2013-08-16)
- 0.2.1 (2013-08-16)
- 0.2.0 (2013-08-16)
- 0.1.2 (2013-05-14)
- 0.1.1 (2013-05-02)
- 0.1.0 (2012-01-15)
- 0.0.15 (2012-01-08)
- 0.0.14 (2012-01-08)
- 0.0.13 (2012-01-08)
- 0.0.12 (2012-01-08)
- 0.0.11 (2012-01-08)
- 0.0.10 (2012-01-07)
- 0.0.9 (2012-01-06)
- 0.0.8 (2012-01-03)
- 0.0.7 (2011-12-18)
- 0.0.6 (2011-12-18)
- 0.0.5 (2011-12-18)
- 0.0.4 (2011-12-18)
- 0.0.3 (2011-12-18)
- 0.0.2 (2011-12-18)
- 0.0.1 (2011-12-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/flickru
- gem 安装: `gem install flickru`
- Bundler: `gem "flickru"`
- 最新版本: 0.6.5
- 最新版归档: https://rubygems.org/downloads/flickru-0.6.5.gem
- 版本锁定: `gem "flickru", "~> 0.6.5"`
- 中央仓库: https://rubygems.org/
