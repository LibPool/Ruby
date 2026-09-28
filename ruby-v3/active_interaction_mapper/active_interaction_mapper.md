# active_interaction_mapper

**Tag**: web, filesystem

## 简介

This gem allows the tracking of ActiveInteractions interactions.

                        This is done by tracking the .execute methode that is overridden in each class inheriting from ActiveInteraction.

                        To be able to trace function calls, I used Ruby's TracePoint class and to draw the graphs I used the 'ruby-graphviz' gem.

                        Note that you need to install GraphViz in your environment and have its path in your path environment variable to be able to draw graphs.

## 官网

- 主页: https://github.com/charbel-elhajj/active_interaction_mapper
- RubyGems: https://rubygems.org/gems/active_interaction_mapper

## 历史版本号

- 0.1.2 (2021-05-11)
- 0.1.1 (2021-05-10)
- 0.1.0 (2021-05-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/active_interaction_mapper
- gem 安装: `gem install active_interaction_mapper`
- Bundler: `gem "active_interaction_mapper"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/active_interaction_mapper-0.1.2.gem
- 版本锁定: `gem "active_interaction_mapper", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
