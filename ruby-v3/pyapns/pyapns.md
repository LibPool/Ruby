# pyapns

**Tag**: web, cli, testing, networking, filesystem

## 简介

:title: The Ruby API

:section: PYAPNS::Client
There's python in my ruby!

This is a class used to send notifications, provision applications and
retrieve feedback using the Apple Push Notification Service.

PYAPNS is a multi-application APS provider, meaning it is possible to send
notifications to any number of different applications from the same application
and same server. It is also possible to scale the client to any number
of processes and servers, simply balanced behind a simple web proxy.

It may seem like overkill for such a bare interface - after all, the 
APS service is rather simplistic. However, PYAPNS takes no shortcuts when it
comes to completeness/compliance with the APNS protocol and allows the
user many optimization and scaling vectors not possible with other libraries.
No bandwidth is wasted, connections are persistent and the server is
asynchronous therefore notifications are delivered immediately.

PYAPNS takes after the design of 3rd party push notification service that
charge a fee each time you push a notification, and charge extra for so-called
'premium' service which supposedly gives you quicker access to the APS servers.
However, PYAPNS is free, as in beer and offers more scaling opportunities without
the financial draw.

:section: Provisioning

To add your app to the PYAPNS server, it must be `provisioned` at least once.
Normally this is done once upon the start-up of your application, be it a web
service, desktop application or whatever... It must be done at least once
to the server you're connecting to. Multiple instances of PYAPNS will have
to have their applications provisioned individually. To provision an application
manually use the `PYAPNS::Client#provision` method.

    require 'pyapns'
    client = PYAPNS::Client.configure
    client.provision :app_id => 'cf', :cert => '/home/ss/cert.pem', :env => 'sandbox', :timeout => 15

This basically says "add an app reference named 'cf' to the server and start
a connection using the certification, and if it can't within 15 seconds, 
raise a `PYAPNS::TimeoutException`

That's all it takes to get started. Of course, this can be done automatically
by using PYAPNS::ClientConfiguration middleware. `PYAPNS::Client` is a singleton
class that is configured using the class method `PYAPNS::Client#configure`. It
is sensibly configured by default, but can be customized by specifying a hash
See the docs on `PYAPNS::ClientConfiguration` for a list of available configuration
parameters (some of these are important, and you can specify initial applications)
to be configured by default.

:section: Sending Notifications

Once your client is configured, and application provisioned (again, these
should be taken care of before you write notification code) you can begin
sending notifications to users. If you're wondering how to acquire a notification
token, you've come to the wrong place... I recommend using google. However,
if you want to send hundreds of millions of notifications to users, here's how
it's done, one at a time...

The `PYAPNS::Client#notify` is a sort of polymorphic method which can notify
any number of devices at a time. It's basic form is as follows:

    client.notify 'cf', 'long ass app token', {:aps=> {:alert => 'hello?'}}

However, as stated before, it is sort of polymorphic:

    client.notify 'cf', ['token', 'token2', 'token3'], [alert, alert2, alert3]

    client.notify :app_id => 'cf', :tokens => 'mah token', :notifications => alertHash

    client.notify 'cf', 'token', PYAPNS::Notification('hello tits!')

As you can see, the method accepts paralell arrays of tokens and notifications
meaning any number of notifications can be sent at once. Hashes will be automatically
converted to `PYAPNS::Notification` objects so they can be optimized for the wire
(nil values removed, etc...), and you can pass `PYAPNS::Notification` objects
directly if you wish.

:section: Retrieving Feedback

The APS service offers a feedback functionality that allows application servers
to retrieve a list of device tokens it deems to be no longer in use, and the
time it thinks they stopped being useful (the user uninstalled your app, better
luck next time...) Sounds pretty straight forward, and it is. Apple recommends
you do this at least once an hour. PYAPNS will return a list of 2-element lists
with the date and the token:

    feedbacks = client.feedback 'cf'

:section: Asynchronous Calls

PYAPNS::Client will, by default, perform no funny stuff and operate entirely
within the calling thread. This means that certain applications may hang when,
say, sending a notification, if only for a fraction of a second. Obviously 
not a desirable trait, all `provision`, `feedback` and `notify`
methods also take a block, which indicates to the method you want to call
PYAPNS asynchronously, and it will be done so handily in another thread, calling
back your block with a single argument when finished. Note that `notify` and `provision`
return absolutely nothing (nil, for you rub--wait you are ruby developers!).
It is probably wise to always use this form of operation so your calling thread
is never blocked (especially important in UI-driven apps and asynchronous servers)
Just pass a block to provision/notify/feedback like so:

    PYAPNS::Client.instance.feedback do |feedbacks|
      feedbacks.each { |f| trim_token f }
    end

:section: PYAPNS::ClientConfiguration
A middleware class to make `PYAPNS::Client` easy to use in web contexts

Automates configuration of the client in Rack environments
using a simple confiuration middleware. To use `PYAPNS::Client` in
Rack environments with the least code possible `use PYAPNS::ClientConfiguration`
(no, really, in some cases, that's all you need!) middleware with an optional
hash specifying the client variables. Options are as follows:

     use PYAPNS::ClientConfiguration(
          :host => 'http://localhost/' 
          :port => 7077,
          :initial => [{
              :app_id => 'myapp',
              :cert => '/home/myuser/apps/myapp/cert.pem',
              :env => 'sandbox',
              :timeout => 15
     }])

Where the configuration variables are defined:

    :host     String      the host where the server can be found
    :port     Number      the port to which the client should connect
    :initial  Array       OPTIONAL - an array of INITIAL hashes

    INITIAL HASHES:

    :app_id   String      the id used to send messages with this certification
                          can be a totally arbitrary value
    :cert     String      a path to the certification or the certification file
                          as a string
    :env      String      the environment to connect to apple with, always
                          either 'sandbox' or 'production'
    :timoeut  Number      The timeout for the server to use when connecting
                          to the apple servers

:section: PYAPNS::Notification
An APNS Notification

You can construct notification objects ahead of time by using this class.
However unnecessary, it allows you to programmatically generate a Notification
like so: 

    note = PYAPNS::Notification.new 'alert text', 9, 'flynn.caf', {:extra => 'guid'}

    -- or --
    note = PYAPNS::Notification.new 'alert text'

These can be passed to `PYAPNS::Client#notify` the same as hashes

## 官网

- 主页: http://pyapns.org
- RubyGems: https://rubygems.org/gems/pyapns

## 历史版本号

- 0.3.0 (2010-01-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/pyapns
- gem 安装: `gem install pyapns`
- Bundler: `gem "pyapns"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/pyapns-0.3.0.gem
- 版本锁定: `gem "pyapns", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
