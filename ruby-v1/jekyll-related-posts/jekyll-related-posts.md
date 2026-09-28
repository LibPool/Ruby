# jekyll-related-posts

**Tag**: template

## 简介

Proper related posts plugin for Jekyll - uses document correlation matrix on TF-IDF (optionally with Latent Semantic Indexing).

Each document is tokenized and stemmed, every word found is treated as keyword for analysis (except for some stop words).

TF-IDF matrix for the whole site is calculated (including extra provided weights), then if given accuraccy is lower than 1.0, LSI algorithm is used to compute new simplified vector space. Document correlation matrix is created using dot product of the matrix and its transpose.

For each of the post' related documents are inserted into priority queue (sorted by score from document correlation matrix), assuming the score is greater than minimal required score. Selected few bests related posts are retrieven from the queue.

Liquid template for each post is rendered and &lt;related-posts /&gt; is replaced with the outcomes of algorithm.

## 官网

- 主页: https://github.com/alfanick/jekyll-related-posts
- 文档: https://www.rubydoc.info/gems/jekyll-related-posts/0.1.2
- RubyGems: https://rubygems.org/gems/jekyll-related-posts

## 历史版本号

- 0.1.2 (2016-10-23)
- 0.1.1 (2015-11-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/jekyll-related-posts
- gem 安装: `gem install jekyll-related-posts`
- Bundler: `gem "jekyll-related-posts"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/jekyll-related-posts-0.1.2.gem
- 版本锁定: `gem "jekyll-related-posts", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
