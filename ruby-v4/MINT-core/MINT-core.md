# MINT-core

**Tag**: web, cli, testing, security, networking, tooling

## 简介

Multimodal systems realizing a combination of speech, gesture and graphical-driven interaction are getting part of our everyday life.

Examples are in-car assistance systems or recent game consoles. Future interaction will be embedded into smart environments offering the user to choose and to combine a heterogeneous set of interaction devices and modalities based on his preferences realizing an ubiquitous and multimodal access.

This framework enables the modeling and execution of multimodal interaction interfaces for the web based on ruby and implements a server-sided synchronisation of all connected modes and media. Currenlty the framework considers gestures, head movements, multi touch and the mouse as principle input modes. The priciple output media is a web application based on a rails frontend as well as sound support based on the SDL libraries.

Building this framework is an ongoing effort and it has to be pointed out that it serves to demonstrate scientific research results and is not targeted to we applied to serve productive systems as they are several limitations that need to be solved (maybe with your help?) like for instance multi-user support and authentification.  

The MINT core gem contains all basic AUI and CUI models as well as the basic infrastructure to create interactors and mappings. For presenting the user interface on a specific platform a "frontend framework" is required. For the first MINT version (2010) we used Rails 2.3 (See http://github.com/sfeu/MINT-rails). The current version uses nodeJS and socketstream as the frontend framework (See http://github.com/sfeu/MINT-platform). The MINT-platform project contains installation instructions.

There is still no further documentation for the framework, but a lot of articles about the concepts and theories of our approach have already been published and can be accessed from our project site http://www.multi-access.de .

## 官网

- 主页: http://www.multi-access.de
- RubyGems: https://rubygems.org/gems/MINT-core

## 历史版本号

- 2.0.0 (2012-11-21)
- 1.0.1 (2011-11-09)
- 1.0.0 (2011-11-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/MINT-core
- gem 安装: `gem install MINT-core`
- Bundler: `gem "MINT-core"`
- 最新版本: 2.0.0
- 最新版归档: https://rubygems.org/downloads/MINT-core-2.0.0.gem
- 版本锁定: `gem "MINT-core", "~> 2.0.0"`
- 中央仓库: https://rubygems.org/
