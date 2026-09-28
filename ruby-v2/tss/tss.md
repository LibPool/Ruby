# tss

**Tag**: web, testing, networking, template

## 简介

Threshold Secret Sharing (TSS) provides a way to generate N shares
    from a value, so that any M of those shares can be used to
    reconstruct the original value, but any M-1 shares provide no
    information about that value. This method can provide shared access
    control on key material and other secrets that must be strongly
    protected.

    This gem implements a Threshold Secret Sharing method based on
    polynomial interpolation in GF(256) and a format for the storage and
    transmission of shares.

    This implementation follows the specification in the document:

    http://tools.ietf.org/html/draft-mcgrew-tss-03

## 官网

- 主页: https://github.com/grempe/tss-rb
- 文档: https://www.rubydoc.info/gems/tss/0.5.0
- RubyGems: https://rubygems.org/gems/tss

## 历史版本号

- 0.5.0 (2017-01-29)
- 0.4.2 (2016-10-13)
- 0.4.1 (2016-09-29)
- 0.4.0 (2016-09-25)
- 0.3.0 (2016-09-24)
- 0.2.0 (2016-09-23)
- 0.1.1 (2016-04-14)
- 0.1.0 (2016-04-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/tss
- gem 安装: `gem install tss`
- Bundler: `gem "tss"`
- 最新版本: 0.5.0
- 最新版归档: https://rubygems.org/downloads/tss-0.5.0.gem
- 版本锁定: `gem "tss", "~> 0.5.0"`
- 中央仓库: https://rubygems.org/
