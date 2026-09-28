# footman

**Tag**: testing, tooling, filesystem

## 简介

# Footman

This gem is still growing.

## Installation
Depends upon having reprepro tool installed (if debian based) or createrepo installed (if red hat based).
Ruby 1.9.+ is required to use this gem.

'createrepo' (rpm) tool does not require any pre-setup to the repository or watched directory.
- - -
'reprepro' (deb) tool requires pre-setup.
The repository directory for deb files must contain:
<pre><code>
conf/
conf/distributions
conf/options
conf/override.precise
</pre></code>

options file is empty, but needed to make reprepro happy

distributions file will contain:
<pre><code>Origin: Tyler
Label: Tyler's Personal Debs
Codename: precise
Architectures: i386 amd64 source lpia
Components: main
Description: Tylers Personal Debian Repository
DebOverride: override.precise
DscOverride: override.precise

Origin: Tyler
Label: Tyler's Personal Debs
Codename: lenny
Architectures: i386 amd64 source lpia
Components: main
Description: Tylers Personal Debian Repository
DebOverride: override.lenny
DscOverride: override.lenny
</code></pre>
Note that the code name is for each distribution repository you support.
for each distribtuion repository you support there must be an override file.

override file can be left empty, footman will fill it out when a new package is added.

The watched directory must have sub directorys named after each of the distribution repositories
you support. For example my watched directory at /path/ will have two subdirectories:
<pre><code>/path/lenny/
/path/precise/</code></pre>
Packages must be dropped into the subdirectory that corrosponds with the distribution they were
built on.
- - -

Add this line to your application's Gemfile:

    gem 'footman'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install footman

Or locally:

    $ gem build footman.gemspec
    $ gem install footman --local

## Usage

footman path/to/watch path/to/repo

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## 官网

- 主页: https://github.com/Pagoda/footman
- RubyGems: https://rubygems.org/gems/footman

## 历史版本号

- 0.0.2 (2013-01-15)
- 0.0.1 (2013-01-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/footman
- gem 安装: `gem install footman`
- Bundler: `gem "footman"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/footman-0.0.2.gem
- 版本锁定: `gem "footman", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
