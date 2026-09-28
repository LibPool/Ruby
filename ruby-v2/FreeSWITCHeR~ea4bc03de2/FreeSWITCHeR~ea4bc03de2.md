# FreeSWITCHeR

**Tag**: web, security, networking

## 简介

========================================================= FreeSWITCHeR Copyright (c) 2009 The Rubyists (Jayson Vaughn, Tj Vanderpoel, Michael Fellinger, Kevin Berry)  Distributed under the terms of the MIT License. ==========================================================  About ----- *** STILL UNDER HEAVY DEVELOPMENT ***  A ruby library for interacting with the &quot;FreeSWITCH&quot; (http://www.freeswitch.org) opensource telephony platform  *** STILL UNDER HEAVY DEVELOPMENT ***  Requirements ------------ - ruby (&gt;= 1.8) - eventmachine (If you wish to use Outbound and Inbound listener)  Usage -----  Example of originating a new call in 'irb' using FSR::CommandSocket#originate:  irb(main):001:0&gt; require 'fsr' =&gt; true  irb(main):002:0&gt; FSR.load_all_commands =&gt; [:sofia, :originate]  irb(main):003:0&gt; sock = FSR::CommandSocket.new =&gt; #&lt;FSR::CommandSocket:0xb7a89104 @server=&quot;127.0.0.1&quot;, @socket=#&lt;TCPSocket:0xb7a8908c&gt;, @port=&quot;8021&quot;, @auth=&quot;ClueCon&quot;&gt;  irb(main):007:0&gt; sock.originate(:target =&gt; 'sofia/gateway/carlos/8179395222', :endpoint =&gt; FSR::App::Bridge.new(&quot;user/bougyman&quot;)).run =&gt; {&quot;Job-UUID&quot;=&gt;&quot;732075a4-7dd5-4258-b124-6284a82a5ae7&quot;, &quot;body&quot;=&gt;&quot;&quot;, &quot;Content-Type&quot;=&gt;&quot;command/reply&quot;, &quot;Reply-Text&quot;=&gt;&quot;+OK Job-UUID: 732075a4-7dd5-4258-b124-6284a82a5ae7&quot;}   Example of creating an Outbound Eventsocket listener:  #!/usr/bin/env ruby  require 'fsr' require &quot;fsr/listener/outbound&quot;  class OesDemo &lt; FSR::Listener::Outbound  def session_initiated(session) number = session.headers[:caller_caller_id_number] # Grab the inbound caller id FSR::Log.info &quot;*** Answering incoming call from #{number}&quot; answer # Answer the call set &quot;hangup_after_bridge=true&quot; # Set a variable speak 'Hello, This is your phone switch.  Have a great day' # use mod_flite to speak hangup # Hangup the call end  end  FSR.start_oes!(OesDemo, :port =&gt; 1888, :host =&gt; &quot;localhost&quot;)    Example of creating an Inbound Eventsocket listener:  #!/usr/bin/env ruby  require 'fsr' require &quot;fsr/listener/inbound&quot;  class IesDemo &lt; FSR::Listener::Inbound  def on_event(event) pp event.headers pp event.content[:event_name] end  end  FSR.start_ies!(IesDemo, :host =&gt; &quot;localhost&quot;, :port =&gt; 8021)    Support ------- Home page at http://code.rubyists.com/projects/fs #rubyists on FreeNode

## 官网

- 主页: http://code.rubyists.com/projects/fs
- RubyGems: https://rubygems.org/gems/FreeSWITCHeR

## 历史版本号

- 0.0.8 (2009-08-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/FreeSWITCHeR
- gem 安装: `gem install FreeSWITCHeR`
- Bundler: `gem "FreeSWITCHeR"`
- 最新版本: 0.0.8
- 最新版归档: https://rubygems.org/downloads/FreeSWITCHeR-0.0.8.gem
- 版本锁定: `gem "FreeSWITCHeR", "~> 0.0.8"`
- 中央仓库: https://rubygems.org/
