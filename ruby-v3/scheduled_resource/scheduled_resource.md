# scheduled_resource

**Tag**: web, cli, database, testing, serialization, networking, template, filesystem, data

## 简介

== README.md:
#ScheduledResource

This gem is for displaying how things are used
over time -- a schedule for a set of "resources".  You
can configure the elements of the schedule and there
are utilities and protocols to connect them:

 - Configuration (specification and management),
 - Query interfaces (a REST-like API and internal protocols to query the models), and
 - A basic Rails controller implementation.

We have a way to configure the schedule, internal
methods to generate the data, and a way to retrieve
data from the client.  However this gem is largely
view-framework agnostic.  We could use a variety of
client-side packages or even more traditional Rails
view templates to generate HTML.

In any case, to get a good feel in a display like
this we need some client-side code.  The gem includes
client-side modules to:

 - Manage &lt;b&gt;time and display geometries&lt;/b&gt; with "infinite" scroll along the time axis.
 - &lt;b&gt;Format display cells&lt;/b&gt; in ways specific to the resource models.
 - &lt;b&gt;Update text justification&lt;/b&gt; as the display is scrolled horizontally.


## Configuration

A **scheduled resource** is something that can be
used for one thing at a time.  So if "Rocky &amp; Bullwinkle"
is on channel 3 from 10am to 11am on Saturday, then
'channel 3' is the &lt;u&gt;resource&lt;/u&gt; and that showing of
the episode is a &lt;u&gt;resource-use&lt;/u&gt; block.  Resources 
and use-blocks are typically Rails models.  Each resource
and its use-blocks get one row in the display.  That
row has a label to the left with some timespan visible
on the rest of the row.

Something else you would expect see in a schedule
would be headers and labels -- perhaps one row with
the date and another row with the hour.  Headers and
labels also fit the model of resources and use-blocks.
Basic timezone-aware classes (ZTime*) for those are
included in this gem.


### Config File

The schedule configuration comes from
&lt;tt&gt;config/resource_schedule.yml&lt;/tt&gt; which has
three top-level sections:

- ResourceKinds:  A hash where the key is a Resource and the value is a UseBlock. (Both are class names),
- Resources:  A list where each item is a Resource Class followed by one or more resource ids, and
- visibleTime:  The visible timespan of the schedule in seconds.

The example file &lt;tt&gt;config/resource_schedule.yml&lt;/tt&gt;
(installed when you run &lt;tt&gt;schedulize&lt;/tt&gt;) should be
enough to display a two-row schedule with just the date
above and the hour below.  Of course you can monkey-patch
or subclass these classes for your own needs.


### The schedule API

The 'schedule' endpoint uses parameters &lt;tt&gt;t1&lt;/tt&gt; and
&lt;tt&gt;t2&lt;/tt&gt; to specify a time interval for the request.
A third parameter &lt;tt&gt;inc&lt;/tt&gt; allows an initial time
window to be expanded without repeating blocks that
span those boundaries.  The time parameters
_plus the configured resources_ define the data to be returned.


### More About Configuration Management

The &lt;b&gt;ScheduledResource&lt;/b&gt; class manages resource and
use-block class names, id's and labels for a schedule
according to the configuration file.
A ScheduledResource instance ties together:

 1. A resource class (eg TvStation),
 2. An id (a channel number in this example), and
 3. Strings and other assets that will go into the DOM.

The id is used to
  - select a resource _instance_ and
  - select instances of the _resource use block_ class (eg Program instances).

The id _could_ be a database id but more
often is something a little more suited to human use
in the configuration.  In any case it is used by model
class method
&lt;tt&gt;(resource_use_block_class).get_all_blocks()&lt;/tt&gt;
to select the right use-blocks for the resource.
A resource class name and id are are joined with
a '_' to form a tag that also serves as an id for the DOM.

Once the configuration yaml is loaded that data is
maintained in the session structure.  Of course having
a single configuration file limits the application's
usefulness.  A more general approach would be to
have a user model with login and configuration would
be associated with the user.


## Installation

Add this line to your application's Gemfile:

```ruby
gem 'scheduled_resource'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install scheduled_resource

Then from your application's root execute:

    $ schedulize .

This will install a few image placeholders, 
client-side modules and a stylesheet under 
&lt;tt&gt;vendor/assets&lt;/tt&gt;, an example configuration
in &lt;tt&gt;config/resource_schedule.yml&lt;/tt&gt; and
an example controller in
&lt;tt&gt;app/controllers/schedule_controller.rb&lt;/tt&gt;.

Also, if you use

    $ bundle show scheduled_resource

to locate the installed source you can browse
example classes &lt;tt&gt;lib/z_time_*.rb&lt;/tt&gt; and
the controller helper methods in
&lt;tt&gt;lib/scheduled_resource/helper.rb&lt;/tt&gt;


## Testing

This gem also provides for a basic test application
using angularjs to display a minimal but functional
schedule showing just the day and hour headers in
two different timezones (US Pacific and Eastern).
Proceed as follows, starting with a fresh Rails app:

    $ rails new test_sr

As above, add the gem to the Gemfile, then 

    $ cd test_sr
    $ bundle
    $ schedulize .

Add lines such as these to &lt;tt&gt;config/routes.rb&lt;/tt&gt;

    get "/schedule/index" =&gt; "schedule#index"
    get "/schedule"       =&gt; "schedule#schedule"

Copy / merge these files from the gem source into
the test app:

    $SR_SRC/app/views/layouts/application.html.erb
    $SR_SRC/app/views/schedule/index.html.erb
    $SR_SRC/app/assets/javascripts/{angular.js,script.js,controllers.js}

and add &lt;tt&gt;//= require angular&lt;/tt&gt; to application.js
just below the entries for &lt;tt&gt;jquery&lt;/tt&gt;.

After you run the server and browse to

    http://0.0.0.0:3000/schedule/index

you should see the four time-header rows specified
by the sample config file.


## More Examples

A better place to see the use of this gem is at
[tv4](https://github.com/emeyekayee/tv4).  Specifically,
models &lt;tt&gt;app/models/event.rb&lt;/tt&gt; and
&lt;tt&gt;app/models/station.rb&lt;/tt&gt; give better examples of
implementing the ScheduledResource protocol and adapting
to a db schema organized along somewhat different lines.




## Contributing

1. Fork it ( https://github.com/emeyekayee/scheduled_resource/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## 官网

- 主页: http://github.com/emeyekayee/scheduled_resource
- 文档: https://www.rubydoc.info/gems/scheduled_resource/0.0.3
- RubyGems: https://rubygems.org/gems/scheduled_resource

## 历史版本号

- 0.0.3 (2015-03-16)
- 0.0.2 (2015-03-13)
- 0.0.1 (2015-02-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/scheduled_resource
- gem 安装: `gem install scheduled_resource`
- Bundler: `gem "scheduled_resource"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/scheduled_resource-0.0.3.gem
- 版本锁定: `gem "scheduled_resource", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
