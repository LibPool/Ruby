# betterobject

**Tag**: tooling

## 简介

This gem installs several class methods to Object which in turn generates both class and instance methods but only when you are ready.
In order to prevent name pollution, you have the ability to manage the generators to pick alternate names if you prefer.
After scouring the RubyGems site, some of the better Class upgrades are included here as well as some of my own.
The gem creates the backbone upon which future upgrades should be forthcoming.
As a teaser, some of the generators presently include: obj.local_methods, obj.inherited_methods, obj.replaced_methods, obj.in?, COBJ.comes_from?, COBJ.derives_from?, obj.find_def.
There are currently 20 generators and counting.
Calling Object.better_install_all will install all of the generators.
You can also generate a subset by calling Object.better_install(:generator_name).
The generator names are also the method names which can be renamed by calling Object.better_rename(old_name, new_name);

## 官网

- 文档: https://www.rubydoc.info/gems/betterobject/1.2.0
- RubyGems: https://rubygems.org/gems/betterobject

## 历史版本号

- 1.2.0 (2018-01-12)
- 1.1.0 (2018-01-04)
- 1.0.0 (2018-01-01)
- 0.1.0 (2017-12-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/betterobject
- gem 安装: `gem install betterobject`
- Bundler: `gem "betterobject"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/betterobject-1.2.0.gem
- 版本锁定: `gem "betterobject", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
