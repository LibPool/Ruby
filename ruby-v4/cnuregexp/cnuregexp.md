# cnuregexp

**Tag**: serialization, filesystem, data

## 简介

cnuregexp allows tags to be placed inside a regex which function as labels for the matches. The matches within the MatchData object can then be accessed like a hash with the tag name  as the key. cnuregexp also provides a greedy match which will return an array of all matches rather than just the first match.  cnuregexp can also extract various data from an xml tag with the Regexp.xml_tag method. It uses Regexps to get the tag name, the attributes and their values, the tag content, and any other relevant data from an xml string.  Lastly, cnuregexp allows commonly used regular expressions to be stored in a config file(lib/cnuregexp_config.yml) and accessed with Regexp.regular_expression_name notation eg. Regexp.ssn, Regexp.email_address. cnuregexp comes preloaded with a few common regular expressions which are located in lib/cnuregexp_config.yml.

## 官网

- 主页: http://opensource.cashnetusa.com
- RubyGems: https://rubygems.org/gems/cnuregexp

## 历史版本号

- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/cnuregexp
- gem 安装: `gem install cnuregexp`
- Bundler: `gem "cnuregexp"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/cnuregexp-1.0.0.gem
- 版本锁定: `gem "cnuregexp", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
