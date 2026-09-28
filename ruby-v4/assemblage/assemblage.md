# assemblage

**Tag**: web, testing

## 简介

Assemblage is a continuous integration toolkit. It's intended to provide you
with a minimal infrastructure for distributing and performing automated tasks
for one or more version control repositories. It makes as few assumptions as
possible as to what those things might be.

It's still just a personal project, but if you want to use it I'm happy to
answer questions and entertain suggestions, especially in the form of
patches/PRs.

Assemblage has three primary parts: the **Assembly Server**, **Assembly
Workers**, and **Repositories**.

&lt;dl&gt;
  &lt;dt&gt;Assembly Server&lt;/dt&gt;
  &lt;dd&gt;Aggregates and distributes events from &lt;em&gt;repositories&lt;/em&gt; to
  &lt;em&gt;workers&lt;/em&gt; via one or more "assemblies".&lt;/dd&gt;

  &lt;dt&gt;Assembly Workers&lt;/dt&gt;
  &lt;dd&gt;Listens for events published by the &lt;em&gt;assembly server&lt;/em&gt;, checks out
  a &lt;em&gt;repository&lt;/em&gt;, and runs an assembly script in that repository.&lt;/dd&gt;

  &lt;dt&gt;Repository&lt;/dt&gt;
  &lt;dd&gt;A distributed version control repository. Assemblage currently supports
  Mercurial and Git.&lt;/dd&gt;
&lt;/dl&gt;

## 官网

- 主页: https://assembla.ge/
- 文档: https://www.rubydoc.info/gems/assemblage/0.1.pre20180313184155
- RubyGems: https://rubygems.org/gems/assemblage

## 历史版本号

- 0.1.pre20180313184155 (2018-03-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/assemblage
- gem 安装: `gem install assemblage`
- Bundler: `gem "assemblage"`
- 最新版本: 0.1.pre20180313184155
- 最新版归档: https://rubygems.org/downloads/assemblage-0.1.pre20180313184155.gem
- 版本锁定: `gem "assemblage", "~> 0.1.pre20180313184155"`
- 中央仓库: https://rubygems.org/
