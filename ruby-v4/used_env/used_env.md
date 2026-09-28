# used_env

**Tag**: filesystem

## 简介

A gem to list all the environment variables used in a Ruby project.

Example usage:
  results = UsedEnv.find_env_variables

  results.each do |entry|
    puts "ENV_Variable: #{entry[:variable]} | File_path: #{entry[:file]} | Line: #{entry[:line]}"
  end
  ..........used_env..........used_env --valid............used_env --invalid.............

## 官网

- 文档: https://www.rubydoc.info/gems/used_env/0.0.15
- RubyGems: https://rubygems.org/gems/used_env

## 历史版本号

- 0.0.15 (2024-12-18)
- 0.0.4 (2024-12-10)
- 0.0.3 (2024-12-09)
- 0.0.2 (2024-12-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/used_env
- gem 安装: `gem install used_env`
- Bundler: `gem "used_env"`
- 最新版本: 0.0.15
- 最新版归档: https://rubygems.org/downloads/used_env-0.0.15.gem
- 版本锁定: `gem "used_env", "~> 0.0.15"`
- 中央仓库: https://rubygems.org/
