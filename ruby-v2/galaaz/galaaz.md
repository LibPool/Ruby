# galaaz

**Tag**: web, testing, security, networking, template, tooling, filesystem, data

## 简介

Galaaz is R-on-Rails: R scientists keep GNU R (CRAN / Bioconductor) for statistics and
graphics, and use Ruby—often Rails—to put that work on the web (HTTP, auth, jobs, HTML)
without rewriting analyses in another stack. Ruby developers also get full access to R
libraries through the same bridge.

Galaaz 2.0 talks to standard GNU R in a separate process. A bridge handles requests,
results, and typing so you can drive R from Ruby (calling R functions, loading packages,
and working with R objects). **JRuby** and **CRuby** are both supported for the same
NewBridge protocol (tested with JRuby 10.1.1.0 + Java 21, and CRuby 3.3).

Like RinRuby, rpy2, or reticulate, Galaaz is a cross-language bridge; unlike embedding a
second interpreter in one VM, using GNU R means compiled R packages and Bioconductor work
as usual. Large tables can optionally flow through Apache Arrow on the R side when you use
the helpers described in the project documentation.

You need JRuby or CRuby and a working GNU R installation in PATH for the bridge to run.
Build the native gatekeeper after install with: make -C ext/new_bridge all

## 官网

- 主页: https://github.com/rbotafogo/galaaz
- 文档: https://rbotafogo.github.io/galaaz/
- 更新日志: https://github.com/rbotafogo/galaaz/blob/galaaz2_0/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/galaaz

## 历史版本号

- 2.1.10 (2026-09-11)
- 2.1.10.pre.14 (2026-09-10)
- 2.1.10.pre.13 (2026-09-10)
- 2.1.10.pre.12 (2026-09-10)
- 2.1.10.pre.11 (2026-09-10)
- 2.1.10.pre.10 (2026-09-10)
- 2.1.10.pre.9 (2026-09-09)
- 2.1.10.pre.8 (2026-09-09)
- 2.1.10.pre.7 (2026-09-09)
- 2.1.10.pre.6 (2026-09-09)
- 2.1.10.pre.5 (2026-09-09)
- 2.1.10.pre.4 (2026-09-09)
- 2.1.10.pre.3 (2026-09-09)
- 2.1.10.pre.2 (2026-09-09)
- 2.1.10.pre.1 (2026-09-09)
- 2.1.9 (2026-09-09)
- 2.1.8 (2026-09-08)
- 2.1.7 (2026-09-08)
- 2.1.6 (2026-09-08)
- 2.1.5 (2026-09-08)
- 2.1.4 (2026-09-04)
- 2.1.3 (2026-09-04)
- 2.1.2 (2026-09-04)
- 2.1.1 (2026-09-04)
- 2.1.0 (2026-09-03)
- 2.0.0 (2026-08-17)
- 0.5.0 (2020-06-07)
- 0.4.10 (2019-05-07)
- 0.4.9 (2019-04-30)
- 0.4.8 (2019-04-22)
- 0.4.7 (2019-03-22)
- 0.4.6 (2019-02-21)
- 0.4.5 (2019-01-30)
- 0.4.2 (2018-11-21)
- 0.4.1 (2018-10-18)
- 0.4.0 (2018-10-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/galaaz
- gem 安装: `gem install galaaz`
- Bundler: `gem "galaaz"`
- 最新版本: 2.1.10
- 最新版归档: https://rubygems.org/downloads/galaaz-2.1.10.gem
- 版本锁定: `gem "galaaz", "~> 2.1.10"`
- 中央仓库: https://rubygems.org/
