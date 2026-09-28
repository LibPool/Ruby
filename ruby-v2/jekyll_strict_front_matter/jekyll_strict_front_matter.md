# jekyll_strict_front_matter

**Tag**: web, cli, networking, template, tooling, filesystem

## 简介

By default, if a page or a post in a Jekyll site has a syntax error in the
    front matter, Jekyll logs an error, does not render anything for the given
    page, and continues. The result is a site without any content for the
    page with the syntax error.

    This can be confusing for people who build sites without looking at the CLI,
    such as those of us whose sites build in a CI. In these cases, we may wish
    for our build to fail if there are front matter syntax errors.
    [This PR](https://github.com/jekyll/jekyll/pull/5832/files) seeks to add a
    config option for that, but in the meantime this plugin exists to fill the
    gap. This plugin may also be used to add the option to sites using an older
    version of Jekyll.

## 官网

- 主页: http://rubygems.org/gems/jekyll-strict-front-matter
- 文档: https://www.rubydoc.info/gems/jekyll_strict_front_matter/0.1.1
- RubyGems: https://rubygems.org/gems/jekyll_strict_front_matter

## 历史版本号

- 0.1.1 (2017-04-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/jekyll_strict_front_matter
- gem 安装: `gem install jekyll_strict_front_matter`
- Bundler: `gem "jekyll_strict_front_matter"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/jekyll_strict_front_matter-0.1.1.gem
- 版本锁定: `gem "jekyll_strict_front_matter", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
