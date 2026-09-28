# konto_check_ruby

**Tag**: filesystem, data

## 简介

konto_check_ruby is a plain Ruby port (no C extension) of Michael Plugge's
C library konto_check. It validates German bank account numbers with all
check digit methods of the Deutsche Bundesbank (00 to E4), generates and
validates IBANs including the Bundesbank IBAN rules, and looks up bank
data (name, BIC, place, ...). It reads the LUT files of the original
library as well as the bank code files (Bankleitzahlendatei) published by
the Deutsche Bundesbank and can generate LUT files itself. The modules
KontoCheck and KontoCheckRaw are compatible with the original konto_check gem.

## 官网

- 主页: https://github.com/provideal/konto_check_ruby
- 更新日志: https://github.com/provideal/konto_check_ruby/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/provideal/konto_check_ruby/issues
- RubyGems: https://rubygems.org/gems/konto_check_ruby

## 历史版本号

- 1.0.0 (2026-09-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/konto_check_ruby
- gem 安装: `gem install konto_check_ruby`
- Bundler: `gem "konto_check_ruby"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/konto_check_ruby-1.0.0.gem
- 版本锁定: `gem "konto_check_ruby", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
