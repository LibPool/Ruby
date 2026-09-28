# devise_revokable

**Tag**: web, testing, security, networking, template

## 简介

== Devise::Revokable

A module for Devise[http://github.com/plataformatec/devise]

This gem was created by "borrowing" heavily from Devise::Invitable[http://github.com/scambra/devise_invitable]

It exists to extend Devise to provide the basis for what is essentially the reverse of the standard
<tt>confirmable</tt> module.  Where <tt>confirmable</tt> sends an email and awaits a response, 
before confirming a new registration, <tt>revokable</tt> allows immediate access and sends an
email which provides a link to "revoke" the account if it was created fraudulently.

This is useful if you want to lower the barrier to entry to creating accounts, and clearly, if
account security isn't a concern.

Note that tests are non-existent.  Use freely but at your own risk.

=== Configuring

It works like normal Devise modules.  Add the <tt>:revokable</tt> module to the declaration.

  # in user.rb
  devise :revokable # plus other devise modules

If the user who received the revocation email follows the provided link and confirms revocation, the account will
effectively be "revoked" and inactive, unable to log in.

Additionally, you may want to override <tt>#revoke!</tt> to perfom additional revocation on the account, e.g. deleting
posts made, resetting personal information, etc.  The super method yields to a block for this purpose.

  # in user.rb
  def revoke!
    super do
      self.some_method_that_resets_me!
    end
  end

That's about the extent of it.  As with typical devise modules you can override the mailers and views with your own.
Additionally you can define the module accessor <tt>@@mailer</tt> on the module with a proc to handle your mail if you need to.
This proc is yielded two arguments, the method name (e.g. :revocation_instructions), and the affected resource.


  # in config/initializers/devise_revokable.rb
  require 'devise_revokable'
  require 'my_mailer'

  DeviseRevokable.mailer = proc {|method_name, resource| MyMailer.send(:method_name, resource) }

## 官网

- 主页: https://github.com/e9digital/devise_revokable
- RubyGems: https://rubygems.org/gems/devise_revokable

## 历史版本号

- 0.0.3 (2011-03-22)
- 0.0.2 (2011-03-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/devise_revokable
- gem 安装: `gem install devise_revokable`
- Bundler: `gem "devise_revokable"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/devise_revokable-0.0.3.gem
- 版本锁定: `gem "devise_revokable", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
