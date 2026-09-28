# ruby-saferpay

**Tag**: web, cli, database, testing, data

## 简介

The SCAI interface is used when the merchant wishes to keep the acquirer on her/his own website for the whole duration of the transaction (client payment details transits through *both* the merchant site and the saferpay database ) whereas VT implies a redirect to the saferpay site.  == FEATURES/PROBLEMS:  * supports both common credit cards and direct debit cards (&quot;Lastschrift&quot;) * support for VT style payments is incomplete  == SYNOPSIS:  Init (info from saferpay test account; they're the same for all test accounts): @pan        =  &quot;9451123100000004&quot;        #  Saferpay test PAN @accountid  =  &quot;99867-94913159&quot;          #  Saferpay test ACCOUNTID @exp        =  &quot;1107&quot;                    #  This will change for other test accounts I guess... Might just be three months ahead of Time.now @sfp  = Saferpay.new( @accountid, @pan, @exp )  Reserve: &lt;tt&gt;@sfp.reserve(30000, &quot;USD&quot;)&lt;/tt&gt;  Amounts are divided by 100. We're talking cents here, not dollars...  Capture last transaction: &lt;tt&gt;@sfp.capture&lt;/tt&gt;  Capture with a transacaton ID &quot;4hj34hj4hh34h4j3hj4h334&quot;: &lt;tt&gt;@sfp.capture(&quot;4hj34hj4hh34h4j3hj4h334&quot;)&lt;/tt&gt;  == REQUIREMENTS:

## 官网

- 文档: https://www.rubydoc.info/gems/ruby-saferpay/0.0.9
- RubyGems: https://rubygems.org/gems/ruby-saferpay

## 历史版本号

- 0.0.4 (2009-07-25)
- 0.0.3 (2009-07-25)
- 0.0.2 (2009-07-25)
- 0.0.9 (2009-07-25)
- 0.0.8 (2009-07-25)
- 0.0.7 (2009-07-25)
- 0.0.5 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/ruby-saferpay
- gem 安装: `gem install ruby-saferpay`
- Bundler: `gem "ruby-saferpay"`
- 最新版本: 0.0.9
- 最新版归档: https://rubygems.org/downloads/ruby-saferpay-0.0.9.gem
- 版本锁定: `gem "ruby-saferpay", "~> 0.0.9"`
- 中央仓库: https://rubygems.org/
