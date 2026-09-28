# vincenty

**Tag**: web, testing, networking, template

## 简介

* Vincenty wrote an algorithm for calculating the bearing and distance between two coordinates on the earth
  and an algorithm for finding a second coordinate, given a starting coordinate, bearing and destination.
  The algorithms model the earth as an ellipsoid, using the WGS-84 model. This is the common GPS model for
  mapping to latitudes and longitudes.

  This is a Ruby implementation of Vincenty's algorithms, and the Vincenty class includes two methods for 
  modeling the earth as a sphere. These were added as a reference for testing the Vincenty algorithm, but
  could be used on their own. 

  The package also makes use of several other classes that may be useful in their own Right. These include
  class Angle, class Latitude (subclass of Angle), class Longitude (subclass of Angle), 
  class TrackAndBearing and class coordinate (which class Vincenty is a subclass)

  Angle requires extensions to Numeric and String to provide to_radians (to_r) and to_degrees (to_d). String also includes a to_decimal_degrees(), which converts most string forms of Latitude and Longitude to decimal form. These extensions are included in the package in core_extensions.rb. Float has also been extended to change round to have an optional argument specifying the number of decimal places to round to. This is fully compatible with the Float.round, as the default is to round to 0 decimal places.

*  The Vincenty code is based on the wikipedia presentation of the Vincenty algorithm http://en.wikipedia.org/wiki/Vincenty%27s_formulae .
*  The algorithm was modified to include changes I found at http://www.movable-type.co.uk/scripts/latlong-vincenty-direct.html.
*  I also altered the formulae to correctly return the bearing for angles greater than 180. 
  
* Vincenty's original publication

** T Vincenty, "Direct and Inverse Solutions of Geodesics on the Ellipsoid with application of nested equations", Survey Review, vol XXII no 176, 1975 http://www.ngs.noaa.gov/PUBS_LIB/inverse.pdf

## 官网

- 主页: http://rbur004.github.io/vincenty/
- 源码仓库: https://github.com/rbur004/vincenty
- 文档: http://rbur004.github.com/vincenty/
- RubyGems: https://rubygems.org/gems/vincenty

## 历史版本号

- 1.0.12 (2022-03-06)
- 1.0.11 (2021-10-14)
- 1.0.10 (2021-10-09)
- 1.0.9 (2021-10-09)
- 1.0.8 (2016-12-03)
- 1.0.7 (2015-05-18)
- 1.0.6 (2014-08-23)
- 1.0.4 (2013-01-12)
- 1.0.3 (2009-12-31)
- 1.0.2 (2009-07-25)
- 1.0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/vincenty
- gem 安装: `gem install vincenty`
- Bundler: `gem "vincenty"`
- 最新版本: 1.0.12
- 最新版归档: https://rubygems.org/downloads/vincenty-1.0.12.gem
- 版本锁定: `gem "vincenty", "~> 1.0.12"`
- 中央仓库: https://rubygems.org/
