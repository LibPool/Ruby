# words_to_image

**Tag**: web, cli, filesystem

## 简介

command line application that

    * accepts a list of search keywords as arguments
    * queries the Flickr API for the top-rated image for each keyword
    * downloads the results
    * crops them rectangularly
    * assembles a collage grid from ten images and
    * writes the result to a user-supplied filename

    If given less than ten keywords, or if any keyword fails to
    result in a match, retrieve random words from a dictionary
    source such as `/usr/share/dict/words`. Repeat as necessary
    until you have gathered ten images.

## 官网

- 文档: https://www.rubydoc.info/gems/words_to_image/0.0.3
- RubyGems: https://rubygems.org/gems/words_to_image

## 历史版本号

- 0.0.3 (2016-02-29)
- 0.0.2 (2016-02-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/words_to_image
- gem 安装: `gem install words_to_image`
- Bundler: `gem "words_to_image"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/words_to_image-0.0.3.gem
- 版本锁定: `gem "words_to_image", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
