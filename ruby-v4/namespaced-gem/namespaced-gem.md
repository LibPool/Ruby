# namespaced-gem

**Tag**: web, testing, networking

## 简介

🔌 A RubyGems plugin that allows gemspec dependencies to be declared as full
URIs pointing to namespaced gem sources such as gem.coop namespaces
(e.g. `https://beta.gem.coop/@myspace/my-gem`).

When installed, this gem patches both RubyGems' native resolver (`gem
install`) and Bundler's resolver (`bundle install`) to parse URI dependency
names, route them to the correct namespace source, and remap transitive deps
on the fly — so `gem install @kaspth/oaken` and `bundle install` with URI
deps in gemspecs both Just Work™.

See https://github.com/gem-coop/gem.coop/issues/12 for the original discussion.

## 官网

- 主页: https://gitlab.com/galtzo-floss/namespaced-gem
- 更新日志: https://gitlab.com/galtzo-floss/namespaced-gem/-/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/namespaced-gem

## 历史版本号

- 0.1.0.pre (2026-03-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/namespaced-gem
- gem 安装: `gem install namespaced-gem`
- Bundler: `gem "namespaced-gem"`
- 最新版本: 0.1.0.pre
- 最新版归档: https://rubygems.org/downloads/namespaced-gem-0.1.0.pre.gem
- 版本锁定: `gem "namespaced-gem", "~> 0.1.0.pre"`
- 中央仓库: https://rubygems.org/
