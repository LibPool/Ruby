# ebs_conductor

**Tag**: web, testing, networking, data

## 简介

= ebs_conductor

The EBS Conductor is a library for managing Amazon Elastic Block Storage volumes and snapshots.  It is designed to persist a specific set of data (a "lineage") between different compute instances.

EBS Conductor can be used on it's own, but it's most powerful when executed on an EC2 instance using Chef, and the ebs_conductor cookbook[https://github.com/rgeyer/cookbooks/tree/master/cookbooks/ebs_conductor]

== Examples

=== Attach a new 1GB blan volume in the lineage "foobar" to a linux box at /dev/sdb1

    ebs_conductor = Rgeyer::Gem::EbsConductor.new('...','...')
    ebs_conductor.attach_from_lineage('i-abcd1234', 'foobar', 1, '/dev/sdb1')

=== Attach a specific snapshot to a 1GB volume in the lineage "foobar" to a linux box at /devb/sdb1

    ebs_conductor = Rgeyer::Gem::EbsConductor.new('...','...')
    ebs_conductor.attach_from_lineage('i-abcd1234', 'foobar', 1, '/dev/sdb1' {:snapshot_id => 'snap-abcd1234'})

=== Snapshot the lineage "foobar", do not purge any old snapshots in the lineage

    ebs_conductor = Rgeyer::Gem::EbsConductor.new('...','...')
    ebs_conductor.snapshot_lineage('foobar')

=== Snapshot the lineage "foobar", and purge old snapshots so that only 7 remain

    ebs_conductor = Rgeyer::Gem::EbsConductor.new('...','...')
    ebs_conductor.snapshot_lineage('foobar', {:history_to_keep => 7})

=== Snapshot the lineage "foobar" from the specified volume_id
This is useful if you're trying to start a lineage from a "naked" instance, or if you are trying to create a new lineage from an existing one

    ebs_conductor = Rgeyer::Gem::EbsConductor.new('...','...')
    ebs_conductor.snapshot_lineage('foobar', {:history_to_keep => 7, :volume_id => 'vol-abcd1234'})

== List of To Do Items
* Support for stripes in a lineage

== Copyright

Copyright (c) 2011 Ryan Geyer. See LICENSE.txt for
further details.

## 官网

- 主页: http://github.com/rgeyer/ebs_conductor
- RubyGems: https://rubygems.org/gems/ebs_conductor

## 历史版本号

- 0.0.4 (2011-07-08)
- 0.0.3 (2011-06-23)
- 0.0.2 (2011-06-06)
- 0.0.1 (2011-06-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/ebs_conductor
- gem 安装: `gem install ebs_conductor`
- Bundler: `gem "ebs_conductor"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/ebs_conductor-0.0.4.gem
- 版本锁定: `gem "ebs_conductor", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
