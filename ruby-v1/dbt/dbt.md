# dbt

**Tag**: filesystem

## 简介

== DBT (Dependencies and deBugging Tool)

DBT is a tool that helps declare dependencies (+app.files_dependencies+) and
assists with debugging in a RubyMotion project. It looks for 'break',
'requires', and 'provides' commands (it does a *teensy* bit of code analyzing to
provide some defaults) to make your RubyMotion +Rakefile+ and +debugger_cmds+
files short and consistent.

To use, include this gem, and add +DBT.analyze(app)+ to your +Rakefile+ in the
&lt;tt&gt;Motion::Project::App.setup&lt;/tt&gt; block.  In your source code you can add DBT
commands and those will be translated into directives for
+app.files_dependencies+ and +debugger_cmds+.

Run +rake+ or &lt;tt&gt;rake debug=1&lt;/tt&gt;, and off you go!

## 官网

- 主页: https://github.com/colinta/dbt
- 文档: https://www.rubydoc.info/gems/dbt/1.2.0
- RubyGems: https://rubygems.org/gems/dbt

## 历史版本号

- 1.2.0 (2014-08-11)
- 1.1.5 (2014-06-02)
- 1.1.4 (2014-04-30)
- 1.1.3 (2014-04-30)
- 1.1.2 (2014-04-24)
- 1.1.1 (2014-04-18)
- 1.1.0 (2014-04-18)
- 1.0.7 (2014-03-29)
- 1.0.6 (2014-03-29)
- 1.0.5 (2014-03-29)
- 1.0.4 (2014-03-29)
- 1.0.3 (2014-03-29)
- 1.0.2 (2014-03-29)
- 1.0.1 (2014-03-29)
- 1.0.0 (2014-02-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/dbt
- gem 安装: `gem install dbt`
- Bundler: `gem "dbt"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/dbt-1.2.0.gem
- 版本锁定: `gem "dbt", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
