# pintoscheck

**Tag**: web, cli, testing, serialization, networking, template, filesystem

## 简介

== PintosCheck -- Auto Pintos Checker to Save the Day ==

== Functionalities ==
The functionality of this simple script is to download pintos homework assignments from the mail inbox and then run through all the desired tests and finally generate reports in plain text or html formats, all automatically.

== Requirements For Running PintosCheck ==
Since all the scripts are written in ruby, PintosCheck require ruby installed on the system. I use ruby 1.8.7 for development, but ruby 1.9.* versions are expected to function as well. However, ruby 1.8.6 and lower versions are not supported. For information of downloading and installing ruby, see http://www.ruby-lang.org/en/downloads/.
In addition to ruby itself, RubyGems 1.3.* is also required because it hosts the installation source for this project and almost all other ruby projects as well. To download or update RubyGems, please go to http://gemcutter.org/pages/download for more information.

== Installation ==
Once you have all the requirements on your system, it's really easy to install PintosCheck. In the UNIX shell or Windows command line environment, type the following command(sudo if needed):
  gem install pintoscheck --include-dependencies
Go grab a cup of coffee, and PintosCheck will automatically download and install itself onto the system.
To check the installation, type 'ptschk --version', and if something like 'PintosCheck 0.1.0' pops up then you're green to go!

== Finally, how do I check my students' pintos homework? ==
This project ships with a 'ptschk' command tool. This tool needs a task configuration file to actually do everything. The configuration file is in YAML format, which is basically a recursive key-value pair representation. If you're using PintosCheck for the first time, there's a very nice command line option to generate the skeleton for you. Just run 'ptschk init my_first_task.config' and a file named 'my_first_task.config' will be generated for you. Inside this file there is a set of the minimal options for the task to run properly, and you just have to fill in what you need. After you set up your configuration file, run 'ptschk run my_first_task.config' and the tasks will kick off immediately, and after a while the report will be generated. A detailed configuration options for advanced task setup will be available in production release of this project.

## 官网

- 主页: http://github.com/ChrisKXu/pintoscheck
- RubyGems: https://rubygems.org/gems/pintoscheck

## 历史版本号

- 0.1.0beta (2010-05-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/pintoscheck
- gem 安装: `gem install pintoscheck`
- Bundler: `gem "pintoscheck"`
- 最新版本: 0.1.0beta
- 最新版归档: https://rubygems.org/downloads/pintoscheck-0.1.0beta.gem
- 版本锁定: `gem "pintoscheck", "~> 0.1.0beta"`
- 中央仓库: https://rubygems.org/
