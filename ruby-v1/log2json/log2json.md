# log2json

**Tag**: web, cli, database, testing, security, serialization, networking, template, tooling, filesystem

## 简介

Log2json lets you read, filter and send logs as JSON objects via Unix pipes.
It is inspired by Logstash, and is meant to be compatible with it at the JSON
event/record level so that it can easily work with Kibana. 

Reading logs is done via a shell script(eg, `tail`) running in its own process.
You then configure(see the `syslog2json` or the `nginxlog2json` script for
examples) and run your filters in Ruby using the `Log2Json` module and its
contained helper classes.

`Log2Json` reads from stdin the logs(one log record per line), parses the log
lines into JSON records, and then serializes and writes the records to stdout,
which then can be piped to another process for processing or sending it to
somewhere else.

Currently, Log2json ships with a `tail-log` script that can be run as the input
process. It's the same as using the Linux `tail` utility with the `-v -F`
options except that it also tracks the positions(as the numbers of lines read
from the beginning of the files) in a few files in the file system so that if the
input process is interrupted, it can continue reading from where it left off
next time if the files had been followed. This feature is similar to the sincedb
feature in Logstash's file input.

Note: If you don't need the tracking feature(ie, you are fine with always
tailling from the end of file with `-v -F -n0`), then you can just use the `tail`
utility that comes with your Linux distribution.(Or more specifically, the
`tail` from the GNU coreutils). Other versions of the `tail` utility may also
work, but are not tested. The input protocol expected by Log2json is very
simple and documented in the source code.

** The `tail-log` script uses a patched version of `tail` from the GNU coreutils
package. A binary of the `tail` utility compiled for Ubuntu 12.04 LTS is
included with the Log2json gem. If the binary doesn't work for your
distribution, then you'll need to get GNU coreutils-8.13, apply the patch(it
can be found in the src/ directory of the installed gem), and then replace
the bin/tail binary in the directory of the installed gem with your version
of the binary. ** 

P.S. If you know of a way to configure and compile ONLY the tail program in
coreutils, please let me know! The reason I'm not building tail post gem
installation is that it takes too long to configure &amp;&amp; make because that
actually builds every utilties in coreutils.


For shipping logs to Redis, there's the `lines2redis` script that can be used as
the output process in the pipe. For shipping logs from Redis to ElasticSearch,
Log2json provides a `redis2es` script.

Finally here's an example of Log2json in action:

From a client machine:

  tail-log /var/log/{sys,mail}log /var/log/{kern,auth}.log | syslog2json |
        queue=jsonlogs \
        flush_size=20 \
        flush_interval=30 \
        lines2redis host.to.redis.server 6379 0  # use redis DB 0


On the Redis server:

  redis_queue=jsonlogs redis2es host.to.es.server


Resources that help writing log2json filters:

  - look at log2json.rb source and example filters
  - http://grokdebug.herokuapp.com/
  - http://www.ruby-doc.org/stdlib-1.9.3/libdoc/date/rdoc/DateTime.html#method-i-strftime

## 官网

- 文档: https://www.rubydoc.info/gems/log2json/0.1.26
- RubyGems: https://rubygems.org/gems/log2json

## 历史版本号

- 0.1.26 (2014-07-11)
- 0.1.25 (2014-07-11)
- 0.1.24 (2014-06-23)
- 0.1.23 (2014-03-03)
- 0.1.22 (2013-11-15)
- 0.1.21 (2013-11-07)
- 0.1.20 (2013-11-06)
- 0.1.19 (2013-10-30)
- 0.1.18 (2013-10-30)
- 0.1.17 (2013-10-29)
- 0.1.16 (2013-10-29)
- 0.1.15 (2013-10-28)
- 0.1.14 (2013-10-25)
- 0.1.13 (2013-10-22)
- 0.1.12 (2013-10-21)
- 0.1.11 (2013-10-15)
- 0.1.10 (2013-10-11)
- 0.1.9 (2013-10-01)
- 0.1.8 (2013-09-17)
- 0.1.7 (2013-09-17)
- 0.1.6 (2013-09-17)
- 0.1.5 (2013-09-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/log2json
- gem 安装: `gem install log2json`
- Bundler: `gem "log2json"`
- 最新版本: 0.1.26
- 最新版归档: https://rubygems.org/downloads/log2json-0.1.26.gem
- 版本锁定: `gem "log2json", "~> 0.1.26"`
- 中央仓库: https://rubygems.org/
