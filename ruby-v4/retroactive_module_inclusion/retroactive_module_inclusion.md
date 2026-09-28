# retroactive_module_inclusion

**Tag**: testing

## 简介

This gem circumvents the "dynamic module include" (aka "double inclusion")
problem, which is the fact that M.module_eval { include N } does not make
the methods of module N available to modules and classes which had included
module M beforehand, only to the ones that include it thereafter. This
behaviour hurts the least surprise principle, specially because if K is a
class, then K.class_eval { include M } *does* make all methods of M available
to all classes which had previously inherited it.

## 官网

- 主页: http://github.com/adrianomitre/retroactive_module_inclusion
- 问题追踪: http://github.com/adrianomitre/retroactive_module_inclusion/issues
- RubyGems: https://rubygems.org/gems/retroactive_module_inclusion

## 历史版本号

- 1.2.5 (2011-01-26)
- 1.2.4 (2011-01-24)
- 1.2.3 (2011-01-24)
- 1.2.2 (2011-01-24)
- 1.2.1 (2011-01-24)
- 1.2.0 (2011-01-24)
- 1.1.0 (2011-01-22)
- 1.0.3 (2011-01-21)
- 1.0.2 (2011-01-21)
- 1.0.1 (2011-01-20)
- 1.0.0 (2011-01-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/retroactive_module_inclusion
- gem 安装: `gem install retroactive_module_inclusion`
- Bundler: `gem "retroactive_module_inclusion"`
- 最新版本: 1.2.5
- 最新版归档: https://rubygems.org/downloads/retroactive_module_inclusion-1.2.5.gem
- 版本锁定: `gem "retroactive_module_inclusion", "~> 1.2.5"`
- 中央仓库: https://rubygems.org/
