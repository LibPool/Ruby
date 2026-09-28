# ontomde-core

**Tag**: web, testing, networking, template, tooling

## 简介

ontoMDE-core is basically a library for loading a RDFS model in ruby memory and process it to do something usefull such as generating Java or C++ code.  ontoMDE-core is used by ontoMDE-uml2 which adds UML2 meta-model definitions and some helper methods. ontoMDE-uml2 is in turn used by ontoMDE-uml2-java which adds methods and rules to generate java5 code.  But ontoMDE-core is *not* *UML* *specific* and can be used with *any* RDF[http://en.wikipedia.org/wiki/Resource_Description_Framework] / RDFS[http://en.wikipedia.org/wiki/RDF_Schema] model such as those created with Protege_2000[http://protege.stanford.edu]. This opens to ontoMDE-core users the ability to generate code from custom DSL[http://en.wikipedia.org/wiki/Domain_Specific_Language] models, or join different models.  This gem bundles, ontomde-inspector which is a web server for browsing a model and a meta-model inside a running ontomde generator. Inspector is available as an independant script but may also be run from generator (such as ontomde-java with option --inspector or --inspectorAfterLoad ) to provide a view of model before or after generation.

## 官网

- 主页: http://ontomde.rubyforge.org
- RubyGems: https://rubygems.org/gems/ontomde-core

## 历史版本号

- 2.0.0 (2009-07-25)
- 1.0.6 (2009-07-25)
- 1.0.4 (2009-07-25)
- 1.0.2 (2009-07-25)
- 2.0.5 (2009-07-25)
- 2.0.4 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/ontomde-core
- gem 安装: `gem install ontomde-core`
- Bundler: `gem "ontomde-core"`
- 最新版本: 2.0.5
- 最新版归档: https://rubygems.org/downloads/ontomde-core-2.0.5.gem
- 版本锁定: `gem "ontomde-core", "~> 2.0.5"`
- 中央仓库: https://rubygems.org/
