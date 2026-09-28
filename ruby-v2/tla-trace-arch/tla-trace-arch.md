# tla-trace-arch

**Tag**: web, testing, networking, template, tooling, filesystem

## 简介

A set of [mustache] templates extending [tla-trace-filter] -tool
    to create a self extracting achieve for API traces generated, when
    model checking formal models created by [tla-Sbuilder] -tool.

    Also includes Ruby classes to extract test cases from archive
    extract.

    Use case:

    Formal models, built using [tla-sbuilder], and model checked using
    [TLA+tools]], can generate /API Traces/, which represent
    end-to-end scenarios executing across system services in the
    formal model. An API Trace is composed of steps, with each step
    giving 1) a (formal) system state before the API call, 2) the API
    call exercised together with (formal model) value bindings of
    request parameters, 3) API response returned, and 4) the (formal)
    system state after the API call.  A API Trace can be mapped to
    /Unit Tests/ on implementation with each Unit Test corresponding a
    step in the API Trace. After executing each of the individual Unit
    Tests, the aggregate result can be interpreted as an execution of
    a "virtual" System Test - considerably easier than managing the
    execution a System Test as a single unit.

    The purpose of =tla-trace-arch= GEM is create a self extracting
    archive, which can be safely distributed to system service
    developers for extracting API Trace Steps to create unit tests for
    the service being developed by the developer.
   

    Ref: 
    - https://github.com/jarjuk/tla-trace-filter
    - https://mustache.github.io/mustache.5.html
    - https://github.com/jarjuk/tla-sbuilder
    - http://research.microsoft.com/en-us/um/people/lamport/tla/tools.html

## 官网

- 文档: https://www.rubydoc.info/gems/tla-trace-arch/0.1.1
- RubyGems: https://rubygems.org/gems/tla-trace-arch

## 历史版本号

- 0.1.1 (2018-02-02)
- 0.1.0 (2018-01-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/tla-trace-arch
- gem 安装: `gem install tla-trace-arch`
- Bundler: `gem "tla-trace-arch"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/tla-trace-arch-0.1.1.gem
- 版本锁定: `gem "tla-trace-arch", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
