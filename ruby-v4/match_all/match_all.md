# match_all

**Tag**: testing, data

## 简介

Ruby String's native #match method will only return the first instance of a
pattern match. This gem provides the #match_all method, returns all instances
of a pattern match in a String as an array.

EXAMPLES:
# Given the test string:
string = "My cat is asleep on the couch. Now the cat is playing."

# #match only returns the first match:

string.match(/cat/)
=> #<MatchData "cat">

# However, I've found I often want to match _all_ instances of the pattern, and
# then e.g. iterate through them and do something with them. #match_all does that:

string.match_all(/cat/)
=> [
     [0] #<MatchData "cat">,
     [1] #<MatchData "cat">
   ]

This is especially useful if, e.g. you want to interrogate the matches to find
out their starting/ending indexes within the string, etc

## 官网

- 主页: https://github.com/jeffdlange/match_all
- 更新日志: https://github.com/jeffdlange/match_all/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/match_all

## 历史版本号

- 0.1.2 (2022-11-15)
- 0.1.1 (2022-11-11)
- 0.1.0 (2022-11-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/match_all
- gem 安装: `gem install match_all`
- Bundler: `gem "match_all"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/match_all-0.1.2.gem
- 版本锁定: `gem "match_all", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
