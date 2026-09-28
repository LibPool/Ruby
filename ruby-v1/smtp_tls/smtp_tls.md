# smtp_tls

**Tag**: web, testing, security, networking, data

## 简介

Provides SMTP STARTTLS support for Ruby 1.8.6 (built-in for 1.8.7+).  Simply
require 'smtp_tls' and use the Net::SMTP#enable_starttls method to talk to
servers that use STARTTLS.

  require 'net/smtp'
  begin
    require 'smtp_tls'
  rescue LoadError
  end

  smtp = Net::SMTP.new address, port
  smtp.enable_starttls
  smtp.start Socket.gethostname, user, password, authentication do |server|
    server.send_message message, from, to
  end

You can also test your SMTP connection settings using mail_smtp_tls:

  $ date | ruby -Ilib bin/mail_smtp_tls smtp.example.com submission \
    &quot;your username&quot; &quot;your password&quot; plain \
    from@example.com to@example.com
  Using SMTP_TLS 1.0.3
  -&gt; &quot;220 smtp.example.com ESMTP XXX\r\n&quot;
  &lt;- &quot;EHLO you.example.com\r\n&quot;
  -&gt; &quot;250-smtp.example.com at your service, [192.0.2.1]\r\n&quot;
  -&gt; &quot;250-SIZE 35651584\r\n&quot;
  -&gt; &quot;250-8BITMIME\r\n&quot;
  -&gt; &quot;250-STARTTLS\r\n&quot;
  -&gt; &quot;250-ENHANCEDSTATUSCODES\r\n&quot;
  -&gt; &quot;250 PIPELINING\r\n&quot;
  &lt;- &quot;STARTTLS\r\n&quot;
  -&gt; &quot;220 2.0.0 Ready to start TLS\r\n&quot;
  TLS connection started
  &lt;- &quot;EHLO you.example.com\r\n&quot;
  -&gt; &quot;250-smtp.example.com at your service, [192.0.2.1]\r\n&quot;
  -&gt; &quot;250-SIZE 35651584\r\n&quot;
  -&gt; &quot;250-8BITMIME\r\n&quot;
  -&gt; &quot;250-AUTH LOGIN PLAIN\r\n&quot;
  -&gt; &quot;250-ENHANCEDSTATUSCODES\r\n&quot;
  -&gt; &quot;250 PIPELINING\r\n&quot;
  &lt;- &quot;AUTH PLAIN BASE64_STUFF_HERE\r\n&quot;
  -&gt; &quot;235 2.7.0 Accepted\r\n&quot;
  &lt;- &quot;MAIL FROM:&lt;from@example.com&gt;\r\n&quot;
  -&gt; &quot;250 2.1.0 OK XXX\r\n&quot;
  &lt;- &quot;RCPT TO:&lt;to@example.com&gt;\r\n&quot;
  -&gt; &quot;250 2.1.5 OK XXX\r\n&quot;
  &lt;- &quot;DATA\r\n&quot;
  -&gt; &quot;354  Go ahead XXX\r\n&quot;
  writing message from String
  wrote 91 bytes
  -&gt; &quot;250 2.0.0 OK 1247028988 XXX\r\n&quot;
  &lt;- &quot;QUIT\r\n&quot;
  -&gt; &quot;221 2.0.0 closing connection XXX\r\n&quot;

This will connect to smtp.example.com using the submission port (port 587)
with a username and password of &quot;your username&quot; and &quot;your password&quot; and
authenticate using plain-text auth (the submission port always uses SSL) then
send the current date to to@example.com from from@example.com.

Debug output from the connection will be printed on stderr.

## 官网

- 主页: http://seattlerb.rubyforge.org/smtp_tls
- RubyGems: https://rubygems.org/gems/smtp_tls

## 历史版本号

- 1.0.1 (2009-08-06)
- 1.0 (2009-08-05)
- 1.0.2 (2009-08-05)
- 1.0.3 (2009-08-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/smtp_tls
- gem 安装: `gem install smtp_tls`
- Bundler: `gem "smtp_tls"`
- 最新版本: 1.0.3
- 最新版归档: https://rubygems.org/downloads/smtp_tls-1.0.3.gem
- 版本锁定: `gem "smtp_tls", "~> 1.0.3"`
- 中央仓库: https://rubygems.org/
