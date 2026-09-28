# netshade-sql_valued_columns

**Tag**: web, database, testing, security, networking, template, data

## 简介

= sql_valued_columns  SqlValuedColumns is an ActiveRecord plugin that will let you have specific SQL statements executed on INSERT / UPDATE.  It will call the SQL function you provide, passing the arguments specified in the call to sql_column.  See the documentation for SqlValuedColumns::ClassMethods#sql_column for more  information regarding usage, including passing Strings and Proc objects as arguments to your SQL function.  Example:  You have a model with two columns, one named "another_column" and  the other named "size_of_another_column".  Whenever you insert data into  "another_column", you want to have size_of_another_column have the result of the SQL function LENGTH inserted into it.  class MyModel &lt; ActiveRecord::Base sql_column :size_of_another_column, "LENGTH", :another_column end  Example 2:  You have a model with three columns, position, latitude and longitude. Latitude and longitude are values expressed as angles, and position is a special datatype for your database that represents the X/Y/Z projection of that particular latitude and longitude (example: http://www.postgresql.org/docs/8.3/static/earthdistance.html )  When you insert data with latitude and longitude, you want to automatically call a function in your database to transform the latitude and longitude into the appropriate represenation.  class MyModel &lt; ActiveRecord::Base sql_column :position, "ll_to_earth", :latitude, :longitude end  Example 3:  You are an insane criminal who has somehow learned SQL.  You would like to  make anyone who runs your code to suffer database punishing queries and odd security and data formatting issues that will make them rue the day they ever learned of computers.  class MyModel &lt; ActiveRecord::Base sql_column :a_column, "(SELECT count(id) FROM large_list_of_things)", :raw =&gt; true sql_column :another_column, '(SELECT count(other_id) FROM other_large_list_of_things WHERE some_column = \'#{some_model_method}\')', :raw =&gt; true end   == Notes  No tests yet, am lazy.  == Copyright  Copyright (c) 2009 Chris Zelenak. See LICENSE for details.

## 官网

- 主页: http://github.com/netshade/sql_valued_columns
- 文档: https://www.rubydoc.info/gems/netshade-sql_valued_columns/0.0.4
- RubyGems: https://rubygems.org/gems/netshade-sql_valued_columns

## 历史版本号

- 0.0.2 (2014-08-10)
- 0.0.3 (2014-08-10)
- 0.0.4 (2014-08-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/netshade-sql_valued_columns
- gem 安装: `gem install netshade-sql_valued_columns`
- Bundler: `gem "netshade-sql_valued_columns"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/netshade-sql_valued_columns-0.0.4.gem
- 版本锁定: `gem "netshade-sql_valued_columns", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
