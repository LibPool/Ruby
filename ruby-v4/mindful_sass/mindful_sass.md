# mindful_sass

**Tag**: testing, filesystem

## 简介

<p>Sass or the much better approach of scss is really helpful and a big silver bullet for my css structuring in 
    ruby projects.</p>
    
 \   <p>Standard sass command works for whole directories or single files only. In general it gets the jobs we want done, 
    but in practical usage i think the sass command tool is a little bit unconvinient. A common scenario for me is, 
 \   that you have whole bunch of sass files, which you want to compile to a single compressed output file.
    But if you have splitted your sass files in component based modules and you want to watch the complete folder you 
    have to care for dependency handling in each file, because each file will be compiled for its own.</p>
 \   
    <pre># compiling a complete folder with scss
    ~ $ sass css/scss:css/compiled</pre>
 \   
    <p>So converting the whole folder is not what i want, because i don\'t want to import for example my color.sass config file
    in each module again. Compiling a single file seems to be the better solution, and it works in general, as expected,
    but the devil is in the detail. </p>
    
    <pre># compiling a single file where the other files are imported.
    ~ $ sass css/scss/main.scss:css/compiled/main.css</pre>
 \   
    <p>If we change a file with impact to our main.sass file, the --watch handle will not get it, because it observes only
    the timestamp of the given main.sass.</p>
    
    <p>Here is it, where mindful_sass tries to help out. You use it according to the single file variant of 
    sass, but it tries to observe the whole folder the given sass file is placed. If a timestamp of file in the sass folder
    or its children changes it will compile the specified main.sass again.</p>

 \   <p>This gem is not aimed to replace anything in the sass universe. It is only a wrapper to avoid the described unconvinience, 
    and i hope that it gets useless as fast as possible, because the sass development gets this feature done for themselves.</p>

 \   <p>Thanks anyway to the sass developer team.</p>

## 官网

- 文档: https://www.rubydoc.info/gems/mindful_sass/0.0.3
- RubyGems: https://rubygems.org/gems/mindful_sass

## 历史版本号

- 0.0.3 (2011-08-01)
- 0.0.2 (2011-08-01)
- 0.0.1 (2011-08-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/mindful_sass
- gem 安装: `gem install mindful_sass`
- Bundler: `gem "mindful_sass"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/mindful_sass-0.0.3.gem
- 版本锁定: `gem "mindful_sass", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
