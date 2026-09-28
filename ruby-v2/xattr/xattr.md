# xattr

**Tag**: filesystem, data

## 简介

= xattr  == DESCRIPTION  Xattr provides the xattr (setxattr, getxattr, removexattr, listxattr) functions in a nice object-oriented wrapper. Ruby/DL is used so no compilation of modules is necessary.  Extended attributes extend the basic attributes associated with files and directories in the file system. They are stored as name:data pairs associated with file system objects (files, directories, symlinks, etc).  == SYNOPSIS  Using the library:  require &quot;xattr&quot;  xattr = Xattr.new(&quot;/path/to/file&quot;) xattr.list # =&gt; [...] xattr.get(&quot;...&quot;) xattr.set(&quot;...&quot;, &quot;...&quot;) xattr.remove(&quot;...&quot;)  Using the provided command-line tool:  $ xattr README.txt com.macromates.caret $ xattr README.txt com.macromates.caret  {column = 9; line = 26; } $ xattr README.txt com.macromates.caret &quot;{column = 0; line = 0; }&quot; {column = 0; line = 0; } $ xattr README.txt -com.macromates.caret {column = 0; line = 0; } $ xattr README.txt $   == REQUIREMENTS  * Mac OS X 10.4 (for now...)  == INSTALL  Using rubygems:  $ sudo gem install xattr  Using setup.rb:  $ sudo ruby setup.rb

## 官网

- 主页: http://rubyforge.org/projects/xattr
- RubyGems: https://rubygems.org/gems/xattr

## 历史版本号

- 0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/xattr
- gem 安装: `gem install xattr`
- Bundler: `gem "xattr"`
- 最新版本: 0.1
- 最新版归档: https://rubygems.org/downloads/xattr-0.1.gem
- 版本锁定: `gem "xattr", "~> 0.1"`
- 中央仓库: https://rubygems.org/
