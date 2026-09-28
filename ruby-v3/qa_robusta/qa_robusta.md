# qa_robusta

**Tag**: web, cli, testing, serialization, networking, template, filesystem

## 简介

QA Robusta is an automation framework easing pain points away from automation test case writers. How is pain relieved?

* Elements, such as links, buttons, and other html objects are defined in one 
  location. This ensures over time the user won't have definitions spread out 
  throughout different layers of code requiring time consuming updates if the 
  application under test is modified.
* Well defined flows allows the user to have a common means for navigating and 
  controlling interactions with the application under test. This takes all logic 
  out of test classes and yields in higher more modular code re-use.
* When an application requiring testing has the elements and flows implemented 
  less code savy resources can easily add new test cases once trained on how to 
  access the flows and elements.
* When ever a link or button is clicked a screen shot is taken
* Results are available under site/results directory in html format. Report 
  includes the rdoc on a per test class method along with any screen shots taken.  
  Example report: https://cyberconnect.biz/opensource/demo_results.html
* Transparent remote Unix command execution leading to well defined interfaces 
  for common task. For example, one may have a class defined specifically for 
  RemoteUnixNetwork. This class would have methods such as, assign_ip, ifup, ifdown,
  etc. This class then would be able to perform these task on any remote Unix machine.
* Executes the same on Windows or Linux/Unix environments. Developers have the 
  freedom to develop on the platform of choice.
* Mechanize extension: Allows the user to define a web application's page elements in 
  a YAML format and provide navigation paths accessing the YAML structure to interact 
  with the web application. Users can also perform direct http.post or any other 
  mechanize functionality when defining state-full interfaces to hit a web application 
  without going through a browser.

## 官网

- 主页: https://cyberconnect.biz/opensource/qa_robusta.html
- RubyGems: https://rubygems.org/gems/qa_robusta

## 历史版本号

- 0.1.9 (2011-10-11)
- 0.1.8 (2011-10-06)
- 0.1.5 (2011-10-04)
- 0.1.4 (2011-10-04)
- 0.1.3 (2011-10-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/qa_robusta
- gem 安装: `gem install qa_robusta`
- Bundler: `gem "qa_robusta"`
- 最新版本: 0.1.9
- 最新版归档: https://rubygems.org/downloads/qa_robusta-0.1.9.gem
- 版本锁定: `gem "qa_robusta", "~> 0.1.9"`
- 中央仓库: https://rubygems.org/
