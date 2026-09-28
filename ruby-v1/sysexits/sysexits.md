# sysexits

**Tag**: web, testing, tooling, devops, filesystem

## 简介

Have you ever wanted to call &lt;code&gt;exit()&lt;/code&gt; with an error condition, but
weren't sure what exit status to use? No? Maybe it's just me, then.

Anyway, I was reading manpages late one evening before retiring to bed in my
palatial estate in rural Oregon, and I stumbled across
&lt;code&gt;sysexits(3)&lt;/code&gt;. Much to my chagrin, I couldn't find a +sysexits+ for
Ruby! Well, for the other 2 people that actually care about
&lt;code&gt;style(9)&lt;/code&gt; as it applies to Ruby code, now there is one!

Sysexits is a *completely* *awesome* collection of human-readable constants for
the standard (BSDish) exit codes, used as arguments to +exit+ to
indicate a specific error condition to the parent process.

It's so fantastically fabulous that you'll want to fork it right away to avoid
being thought of as that guy that's still using Webrick for his blog. I mean,
&lt;code&gt;exit(1)&lt;/code&gt; is so passé! This is like the 14-point font of Systems
Programming.

Like the C header file from which this was derived (I mean forked, naturally),
error numbers begin at &lt;code&gt;Sysexits::EX__BASE&lt;/code&gt; (which is way more cool
than plain old +64+) to reduce the possibility of clashing with other exit
statuses that other programs may already return.

The codes are available in two forms: as constants which can be imported into
your own namespace via &lt;code&gt;include Sysexits&lt;/code&gt;, or as
&lt;code&gt;Sysexits::STATUS_CODES&lt;/code&gt;, a Hash keyed by Symbols derived from the
constant names.

Allow me to demonstrate. First, the old way:

    exit( 69 )

Whaaa...? Is that a euphemism? What's going on? See how unattractive and...
well, 1970 that is? We're not changing vaccuum tubes here, people, we're
&lt;em&gt;building a totally-awesome future in the Cloud™!&lt;/em&gt;

    include Sysexits
    exit EX_UNAVAILABLE

Okay, at least this is readable to people who have used &lt;code&gt;fork()&lt;/code&gt;
more than twice, but you could do so much better!

    include Sysexits
    exit :unavailable

Holy Toledo! It's like we're writing Ruby, but our own made-up dialect in
which variable++ is possible! Well, okay, it's not quite that cool. But it
does look more Rubyish. And no monkeys were patched in the filming of this
episode! All the simpletons still exiting with icky _numbers_ can still
continue blithely along, none the wiser.

## 官网

- 主页: https://bitbucket.org/ged/sysexits
- 文档: http://deveiate.org/code/sysexits
- 问题追踪: https://bitbucket.org/ged/sysexits/issues
- RubyGems: https://rubygems.org/gems/sysexits

## 历史版本号

- 1.2.0 (2014-08-08)
- 1.1.0 (2012-09-18)
- 1.0.2 (2010-12-23)
- 1.0.1 (2010-10-14)
- 1.0.0 (2010-06-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/sysexits
- gem 安装: `gem install sysexits`
- Bundler: `gem "sysexits"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/sysexits-1.2.0.gem
- 版本锁定: `gem "sysexits", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
