# bjeanes-harsh

**Tag**: web, testing, tooling, filesystem

## 简介

"Harsh: Another Rails Syntax Highlighter," is just that - it highlights code in Rails, much like Radiograph or tm_syntax_highlighting. However, it does it well, _better_. Oh, and it also supports Haml, as well as ERb. And it comes with rake tasks.  Firstly, it allows block form: &lt;% harsh :theme =&gt; :dawn do %&gt; class Testing def initialize(str) puts str end end &lt;% end %&gt; as well as the form the other plugins offer, which is text as a parameter: &lt;% harsh %Q{ class Testing def initialize(str) puts str end end }, :theme =&gt; :dawn  For haml, harsh is implemented as a filter. First, add this to the bottom of your environment.rb: Harsh.enable_haml  Then, to use harsh in Haml: :harsh class Foo &lt; Bar end  However, haml's filters can't take options. So how on earth are we going to customize it to our heart's delight? Easily, my friend, fret not! Enter the BCL (Bootleg Configuration Line):  :harsh #!harsh theme = all_hallows_eve lines=true syntax=css h1 { float:left; clear:left; position:relative; }  It has to be the first line in the filter. You don't need the config line, though. Also, notice that you can have spaces between the arguments and the little = sign.  Harsh also offers rake tasks for what tm_syntax_highlighting provides in generators, and a :harsh as a stylesheet-includer to load all syntax-highlighting files, as such: &lt;%= stylesheet_include_tag :harsh %&gt;  The rake tasks for setting up your stylesheets are these: rake harsh:theme:list # lists available themes rake harsh:theme:install[twilight] # installs the twilight theme into /public/stylesheets/harsh/ rake harsh:theme:install THEME=twilight # also installs the twilight theme (for *csh shells) rake harsh:theme:uninstall[twilight] # removes the twilight theme rake harsh:theme:uninstall THEME=twilight # also uninstalls the twilight theme (for *csh shells)  While purely informative, you can find out the available syntaxes as follows: rake harsh:syntax:list

## 官网

- 主页: http://www.carboni.ca/
- 文档: https://www.rubydoc.info/gems/bjeanes-harsh/0.1.0
- RubyGems: https://rubygems.org/gems/bjeanes-harsh

## 历史版本号

- 0.1.0 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/bjeanes-harsh
- gem 安装: `gem install bjeanes-harsh`
- Bundler: `gem "bjeanes-harsh"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/bjeanes-harsh-0.1.0.gem
- 版本锁定: `gem "bjeanes-harsh", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
