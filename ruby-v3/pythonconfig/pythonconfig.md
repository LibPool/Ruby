# pythonconfig

**Tag**: tooling, filesystem

## 简介

PythonConfig is a module with classes for parsing and writing Python configuration  files created by the ConfigParser classes in Python. These files are structured like this: [Section Name] key = value otherkey: othervalue  [Other Section] key: value3 otherkey = value4  Leading whitespace before values are trimmed, and the key must be the at the start of the line - no leading whitespace there. You can use : or = .  Multiline values are supported, as long as the second (or third, etc.) lines start with whitespace:  [Section] bigstring: This is a very long string, so I'm not sure I'll be able to fit it on one line, but as long as there is one space before each line, I'm ok. Tabs work too.  Also, this class supports interpolation: [Awards] output: Congratulations for winning %(prize)! prize: the lottery Will result in: config.sections[&quot;Awards&quot;][&quot;output&quot;] == &quot;Congratulations for winning the lottery!&quot;  You can also access the sections with the dot operator, but only with all-lowercase: [Awards] key:value [prizes] lottery=3.2 million  config.awards[&quot;key&quot;] #=&gt; &quot;value&quot; config.prizes[&quot;lottery&quot;] #=&gt; &quot;3.2 million&quot;   You can modify any values you want, though to add sections, you should use the add_section method. config.sections[&quot;prizes&quot;][&quot;lottery&quot;] = &quot;100 dollars&quot; # someone hit the jackpot config.add_section(&quot;Candies&quot;) config.candies[&quot;green&quot;] = &quot;tasty&quot; When you want to output a configuration, just call its +to_s+ method. File.open(&quot;output.ini&quot;,&quot;w&quot;) do |out| out.write config.to_s end

## 官网

- 主页: http://www.carboni.ca/
- RubyGems: https://rubygems.org/gems/pythonconfig

## 历史版本号

- 1.0.1 (2009-07-25)
- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/pythonconfig
- gem 安装: `gem install pythonconfig`
- Bundler: `gem "pythonconfig"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/pythonconfig-1.0.1.gem
- 版本锁定: `gem "pythonconfig", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
