# conjugatefr

**Tag**: cli, template

## 简介

== ABOUT
A simple program and library to conjugate french verbs.
Parses responses to requests to an online reference site.

=== Executable
ConjugateFR comes with the executable binary +conjugatefr+.
To view information about it's supported arguments, run
 conjugatefr --help

=== Custom Renderers
To make a custom renderer, just type
 require conjugatefr/renderer
and then make a class that extends +Renderer+.
An example is as follows:

  require 'conjugatefr/renderer'
  class ExampleRenderer &lt; Renderer
    def pre
      puts "This goes before the words."
    end
    def word (name, words)
      print "#{name}:"
      words.each do |word|
        print " #{word}"
      end
    end
    def post
      puts "This goes after the words."
    end
    def description; "Renders an example format."; end
  end
  # Add to the Renderers list (For CLI and other programs that use it.)
  $renderers["Example"] = ExampleRenderer.new
To try this out, save it as +erend.rb+ and then run:
  conjugatefr -R ./erend.rb -r Example
It will produce the output:
  This goes before the words.
  someword: someconjugation etc etc
  ... (more words will be here)
  This goes after the words.

=== The Library
The library can be included with +require conjugatefr+. It includes the
+ConjugateFR+ class.

## 官网

- 主页: http://rubygems.org/gems/conjugatefr
- 文档: https://www.rubydoc.info/gems/conjugatefr/1.0.5
- RubyGems: https://rubygems.org/gems/conjugatefr

## 历史版本号

- 1.0.5 (2015-09-17)
- 1.0.4 (2015-09-17)
- 1.0.3 (2015-09-17)
- 1.0.2 (2015-09-17)
- 1.0.0 (2015-09-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/conjugatefr
- gem 安装: `gem install conjugatefr`
- Bundler: `gem "conjugatefr"`
- 最新版本: 1.0.5
- 最新版归档: https://rubygems.org/downloads/conjugatefr-1.0.5.gem
- 版本锁定: `gem "conjugatefr", "~> 1.0.5"`
- 中央仓库: https://rubygems.org/
