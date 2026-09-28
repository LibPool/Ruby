# corto

**Tag**: web, database, testing, networking, filesystem, data

## 简介

CORTO - your url shortner gem
-----------------------------

- Yet another url shortner?
	
	corto is a ruby gem that shorten a URL for you and store the result in a SQLite3 database.
	Why the world needs another url shortener? Well, true to be told I don't know the answer and I'm 
	pretty sure this code is far away from being revolutionary.
	
	However... corto is funniest!

- Usage
	
	Using corto as standalone utility is straightforward. In case you want to shorten an url you just 
	launch the program with the url as parameter.
	
		% bin/corto http://www.armoredcode.com
		% corto: http://www.armoredcode.com shrunk as ji5jnu
	
	Please note that you've to supply a valid URL, since internally it's parsed and rejected anything but
	HTTP and HTTPS verbs.
	
		% bin/corto funnystatementhere
		% corto: it seems funnystatementhere is not a valid url to shrink
	
	If you want to deflate a shrunk url, you have just to specify the '-d' flag this way.
		
		% bin/corto -d ji5jnu
		% corto: ji5jnu deflated is http://www.armoredcode.com

	Super easy, isn't it? Now, go ahead and shrink the web!
	
- API

	A simple corto shortening session start with class initialization, optionally telling which SQLite3 
	database to use and then mastering the parameter.
	
		require 'corto'
		
		...
		corto = Corto.new # we're now saying the gem we want to use it's internal database stored in db/corto.db
		s = corto.shrink('http://www.armoredcode.com')
	
		# s now stores the shrinked url that is already added to database if not present.
		# If you'll pass an invalid url to shrink(), nil will be returned instead
	
	Deflating a URL is super easy as well
	
		# The deflate process is quite straightforward as well
		
		d = corto.deflate(s)
		# d has now the deflated url or nil if that url was not found
	
	You can also count how many urls contained into db
		
		# If you want to know how many urls you have in your database, just call the count() method.
		puts 'Hey, I have stored ' + corto.count() + ' urls'
	
	And finally you can purge your db
		
		# Tired of your database and time for a massive clean has come? Let's purge the db.
		corto.purge
		
		# corto.count == 0 now
		 
	
- Note on Patches/Pull Requests

	* Fork the project.
	* Make your feature addition or bug fix.
	* Add tests for it. This is important so I don’t break it in a future version unintentionally.
	* Commit, do not mess with rakefile, version, or history. (if you want to have your own version, 
		that is fine but bump version in a commit by itself I can ignore when I pull)
	* Send me a pull request. Bonus points for topic branches.

- Copyright
	
	Copyright © 2011 Paolo Perego. See LICENSE for details.

## 官网

- 主页: http://github.com/thesp0nge/corto
- RubyGems: https://rubygems.org/gems/corto

## 历史版本号

- 0.99.0 (2011-03-25)
- 0.90.0 (2011-03-01)
- 0.80.2 (2011-02-11)
- 0.80.1 (2011-02-09)
- 0.80.0 (2011-02-09)
- 0.60.0 (2011-02-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/corto
- gem 安装: `gem install corto`
- Bundler: `gem "corto"`
- 最新版本: 0.99.0
- 最新版归档: https://rubygems.org/downloads/corto-0.99.0.gem
- 版本锁定: `gem "corto", "~> 0.99.0"`
- 中央仓库: https://rubygems.org/
