# egduphsphonebookadapt

**Tag**: serialization

## 简介

The class gives you a search function, which takes a hash in form of {:first => first_name, :last => last_name} and returns an array of hashes corresponding to results.  you can send an options hash with :form => 'json' 
                    to get the results as JSON 

       example: Phonebook.new.search_results(:first => 'Bob', :last => 'Jones') will produce '[{:name=>Jones, Bob, :location=>HUP  Medicine  Department  of  3400  Spruce  St, :contact_info=>{Office=>(215) 5555-5555, Cell=>(215) 555-5555, email=>Bob.jones@uphs.upenn.edu}}]' 
                    
 this is an array, even if there is only one result. Can also call Phonebook.search_results(name_hash, options)

## 官网

- 文档: https://www.rubydoc.info/gems/egduphsphonebookadapt/0.0.8
- RubyGems: https://rubygems.org/gems/egduphsphonebookadapt

## 历史版本号

- 0.0.8 (2014-05-05)
- 0.0.6 (2014-04-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/egduphsphonebookadapt
- gem 安装: `gem install egduphsphonebookadapt`
- Bundler: `gem "egduphsphonebookadapt"`
- 最新版本: 0.0.8
- 最新版归档: https://rubygems.org/downloads/egduphsphonebookadapt-0.0.8.gem
- 版本锁定: `gem "egduphsphonebookadapt", "~> 0.0.8"`
- 中央仓库: https://rubygems.org/
