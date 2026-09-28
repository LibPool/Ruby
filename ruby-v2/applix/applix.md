# applix

**Tag**: tooling

## 简介

ApplixHash#from_argv builds hashes from ARGV like argument vectors
    according to following examples:

         '-f'                  --&gt; { :f      =&gt; true }
         '--flag'              --&gt; { :flag   =&gt; true }
         '--flag:false'        --&gt; { :flag   =&gt; false }
         '--flag=false'        --&gt; { :flag   =&gt; 'false' }
         '--option=value'      --&gt; { :option =&gt; "value" }
         '--int=1'             --&gt; { :int    =&gt; "1" }
         '--float=2.3'         --&gt; { :float  =&gt; "2.3" }
         '--float:2.3'         --&gt; { :float  =&gt; 2.3 }
         '--txt="foo bar"'     --&gt; { :txt    =&gt; "foo bar" }
         '--txt:'"foo bar"''   --&gt; { :txt    =&gt; "foo bar" }
         '--txt:%w{foo bar}'   --&gt; { :txt    =&gt; ["foo", "bar"] }
         '--now:Time.now'      --&gt; { :now    =&gt; #&lt;Date: 3588595/2,0,2299161&gt; }

     remaining arguments(non flag/options) are inserted as [:arguments,
     args], eg:
         Hash.from_argv %w(--foo --bar=loo 123 now)
     becomes
         { :foo =&gt; true, :bar =&gt; 'loo', :arguments =&gt; ["123", "now"] }

## 官网

- 主页: http://github.com/crux/applix
- 文档: https://www.rubydoc.info/gems/applix/0.4.14
- RubyGems: https://rubygems.org/gems/applix

## 历史版本号

- 0.4.14 (2015-01-16)
- 0.4.13 (2015-01-08)
- 0.4.12 (2015-01-08)
- 0.4.11 (2013-07-23)
- 0.4.10 (2012-05-29)
- 0.4.9 (2012-04-26)
- 0.4.8 (2012-03-27)
- 0.4.7 (2012-03-27)
- 0.4.6 (2012-03-26)
- 0.4.5 (2012-03-26)
- 0.4.4 (2012-03-20)
- 0.4.3 (2012-03-20)
- 0.4.2 (2012-03-20)
- 0.3.8 (2011-08-28)
- 0.3.7 (2011-08-22)
- 0.3.6 (2011-08-17)
- 0.3.5 (2011-08-16)
- 0.3.4 (2011-08-16)
- 0.3.0 (2011-08-14)
- 0.2.2 (2011-02-07)
- 0.2.1 (2009-11-25)
- 0.2.0 (2009-11-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/applix
- gem 安装: `gem install applix`
- Bundler: `gem "applix"`
- 最新版本: 0.4.14
- 最新版归档: https://rubygems.org/downloads/applix-0.4.14.gem
- 版本锁定: `gem "applix", "~> 0.4.14"`
- 中央仓库: https://rubygems.org/
