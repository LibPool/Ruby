# RedcapAPI

**Tag**: web, testing, serialization, data

## 简介

This gem is still under active development. Please contact me directly with any  questions or suggestions. 
    
  To start:

  r = RedcapAPI.new(token, url) # your institution has it's own url, and each project has it's own token

  r.get(optional record_id) # returns all records in JSON format or a specific record if specified
  
  r.get_fields # returns all fields for that instrument
  
  r.post(data) # this will either update an old record or create a new one. the data should be in form of array of hashes or as a hash (for one item).  dates are accepted in Date class or in strftime('%F') format. 
  for example
    data = {name: 'this is a test', field_2: Date.today}
    r.post(data) # creates a new object using the fields above. field names must match those in the existing project
    "{\"count\": 1}" --&gt; indicates the object posted. 
  
  to update an existing record:
  data = {record_id: 3, name: 'this is a test to update', field_2: Date.today}
  r.post(data) # this will update the record with record_id 3. if record_id 3 does not exist it will create an entry with that record id

## 官网

- 文档: https://www.rubydoc.info/gems/RedcapAPI/0.0.6
- RubyGems: https://rubygems.org/gems/RedcapAPI

## 历史版本号

- 0.0.6a (2015-06-18)
- 0.0.6 (2015-06-18)
- 0.0.5b (2014-07-13)
- 0.0.5a (2014-07-13)
- 0.0.5 (2014-07-13)
- 0.0.4 (2014-07-13)
- 0.0.3 (2014-07-13)
- 0.0.2 (2014-07-13)
- 0.0.1 (2014-07-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/RedcapAPI
- gem 安装: `gem install RedcapAPI`
- Bundler: `gem "RedcapAPI"`
- 最新版本: 0.0.6
- 最新版归档: https://rubygems.org/downloads/RedcapAPI-0.0.6.gem
- 版本锁定: `gem "RedcapAPI", "~> 0.0.6"`
- 中央仓库: https://rubygems.org/
