# promotion

**Tag**: web, database, serialization, devops, filesystem, data

## 简介

The Promotion tool is designed to make it easy and quick to deploy an application
		into production. Originally built for use with OpenBSD, it can be used on an *nix
		system by adjusting a few paths (in config.rb).

		To deploy or install an application you just need to copy a few files into place, right?
		Well, the folders need to be there first of course, oh and the permissions need to be set,
		and I guess we need the right users set up before file ownerships can be set correctly,
		which means we need groups before that ... ok, so there is more to it than copying a few files.

		There are also system-wide settings that may need to be modified to support an application,
		such as environment variables in /etc/profile, /etc/sudoers,
		startup scripts in /etc/rc.conf.local, and /var/cron/tabs/* cron jobs.
		Promotion does not modify these sensitive files, but it does say how to change them.

		Promotion handles all of this based on an XML deployment descriptor for each application,
		allowing rapid, reliable redeployment with a single line command (promote). It also manages database
		schema migration with the evolve/devolve commands.

## 官网

- 主页: http://rubygems.org/gems/promotion
- 文档: https://www.rubydoc.info/gems/promotion/2.1.3
- RubyGems: https://rubygems.org/gems/promotion

## 历史版本号

- 2.1.3 (2013-11-22)
- 2.1.2 (2013-11-14)
- 2.1.1 (2013-11-14)
- 2.1 (2013-11-01)
- 2.0 (2013-10-30)
- 1.4.7 (2013-10-18)
- 1.4.6 (2013-10-18)
- 1.4.5 (2013-09-20)
- 1.4.4 (2013-04-04)
- 1.4.3 (2013-01-08)
- 1.4.2 (2012-11-04)
- 1.4.1 (2012-10-03)
- 1.4.0 (2012-10-01)
- 1.3.8 (2012-09-30)
- 1.3.7 (2012-09-29)
- 1.3.6 (2012-09-29)
- 1.3.5 (2012-09-27)
- 1.3.4 (2012-09-27)
- 1.3.3 (2012-09-27)
- 1.3.2 (2012-09-27)
- 1.3.1 (2012-09-26)
- 1.3.0 (2012-09-26)
- 1.2.1 (2012-09-25)
- 1.2.0 (2012-09-20)
- 1.1.0 (2012-09-20)
- 1.0.9 (2012-09-19)
- 1.0.8 (2012-09-19)
- 1.0.7 (2012-09-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/promotion
- gem 安装: `gem install promotion`
- Bundler: `gem "promotion"`
- 最新版本: 2.1.3
- 最新版归档: https://rubygems.org/downloads/promotion-2.1.3.gem
- 版本锁定: `gem "promotion", "~> 2.1.3"`
- 中央仓库: https://rubygems.org/
