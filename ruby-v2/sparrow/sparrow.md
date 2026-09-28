# sparrow

**Tag**: web, cli, testing, networking, data

## 简介

# Sparrow is a really fast lightweight queue written in Ruby that speaks memcached.  # That means you can use Sparrow with any memcached client library (Ruby or otherwise).  #  # Basic tests shows that Sparrow processes messages at a rate of 850-900 per second.  # The load Sparrow can cope with increases exponentially as you add to the cluster.  # Sparrow also takes advantage of eventmachine, which uses a non-blocking io, offering great performance. #  # Sparrow is a in-memory queue but will persist the data to disk when receiving a term signal. #  # Sparrow comes with built in support for daemonization and clustering.  # Also included are example libraries and clients. For example: #  # require 'memcache' # m = MemCache.new('127.0.0.1:11212') # m['queue_name'] = '1' # Publish to queue # m['queue_name']       #=&gt; 1 Pull next msg from queue # m['queue_name']       #=&gt; nil # m.delete('queue_name) # Delete queue #  # # or using the included client: #  # class MyQueue &lt; MQ3::Queue #   def on_message #     logger.info &quot;Received msg with args: #{args.inspect}&quot; #   end # end #  # MyQueue.servers = [ #   MQ3::Protocols::Memcache.new({:host =&gt; '127.0.0.1', :port =&gt; 11212, :weight =&gt; 1}) # ] # MyQueue.publish('test msg') # MyQueue.run #  # Messages are deleted as soon as they're read and the order you add messages to the queue probably won't  # be the same order when they're removed. #  # Additional memcached commands that are supported are: # flush_all # Deletes all queues # version # quit # The memcached commands 'add', and 'replace' just call 'set'. #  # Call sparrow with --help for usage options #  # The daemonization won't work on Windows.  #  # Check out the code: # svn checkout http://sparrow.googlecode.com/svn/trunk/ sparrow #  # Sparrow was inspired by Twitter's Starling

## 官网

- 主页: http://code.google.com/p/sparrow
- RubyGems: https://rubygems.org/gems/sparrow

## 历史版本号

- 0.4.1 (2009-07-25)
- 0.4 (2009-07-25)
- 0.3.1 (2009-07-25)
- 0.3 (2009-07-25)
- 0.2 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/sparrow
- gem 安装: `gem install sparrow`
- Bundler: `gem "sparrow"`
- 最新版本: 0.4.1
- 最新版归档: https://rubygems.org/downloads/sparrow-0.4.1.gem
- 版本锁定: `gem "sparrow", "~> 0.4.1"`
- 中央仓库: https://rubygems.org/
