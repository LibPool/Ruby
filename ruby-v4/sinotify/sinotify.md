# sinotify

**Tag**: web, networking, filesystem

## 简介

ALPHA Alert -- just uploaded initial release. 

Linux inotify is a means to receive events describing file system activity (create, modify, delete, close, etc). 

Sinotify was derived from aredridel's package (http://raa.ruby-lang.org/project/ruby-inotify/), with the addition of
Paul Boon's tweak for making the event_check thread more polite (see
http://www.mindbucket.com/2009/02/24/ruby-daemons-verifying-good-behavior/)

In sinotify, the classes Sinotify::PrimNotifier and Sinotify::PrimEvent provide a low level wrapper to inotify, with
the ability to establish 'watches' and then listen for inotify events using one of inotify's synchronous event loops,
and providing access to the events' masks (see 'man inotify' for details). Sinotify::PrimEvent class adds a little semantic sugar
to the event in to the form of 'etypes', which are just ruby symbols that describe the event mask. If the event has a
raw mask of (DELETE_SELF & IS_DIR), then the etypes array would be [:delete_self, :is_dir]. 

In addition to the 'straight' wrapper in inotify, sinotify provides an asynchronous implementation of the 'observer
pattern' for notification. In other words, Sinotify::Notifier listens in the background for inotify events, adapting
them into instances of Sinotify::Event as they come in and immediately placing them in a concurrent queue, from which
they are 'announced' to 'subscribers' of the event.  [Sinotify uses the 'cosell' implementation of the Announcements
event notification framework, hence the terminology 'subscribe' and 'announce' rather then 'listen' and 'trigger' used
in the standard event observer pattern. See the 'cosell' package on github for details.]

A variety of 'knobs' are provided for controlling the behavior of the notifier: whether a watch should apply to a
single directory or should recurse into subdirectores, how fast it should broadcast queued events, etc (see
Sinotify::Notifier, and the example in the synopsis section below). An event 'spy' can also be setup to log all
Sinotify::PrimEvents and Sinotify::Events.

Sinotify::Event simplifies inotify's muddled event model, sending events only for those files/directories that have
changed. That's not to say you can't setup a notifier that recurses into subdirectories, just that any individual
event will apply to a single file, and not to its children. Also, event types are identified using words (in the form
of ruby :symbols) instead of inotify's event masks. See Sinotify::Event for more explanation. 

The README for inotify:

  http://www.kernel.org/pub/linux/kernel/people/rml/inotify/README

Selected quotes from the README for inotify:

  * "Rumor is that the 'd' in 'dnotify' does not stand for 'directory' but for 'suck.'"

  * "The 'i' in inotify does not stand for 'suck' but for 'inode' -- the logical
    choice since inotify is inode-based."

(The 's' in 'sinotify' does in fact stand for 'suck.')

## 官网

- 主页: http://tab-a.slot-z.net
- RubyGems: https://rubygems.org/gems/sinotify

## 历史版本号

- 0.0.2 (2009-10-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/sinotify
- gem 安装: `gem install sinotify`
- Bundler: `gem "sinotify"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/sinotify-0.0.2.gem
- 版本锁定: `gem "sinotify", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
