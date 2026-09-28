# ssh_sig

**Tag**: web, cli, testing, security, networking, filesystem

## 简介

# SshSig - SSH signature verification in pure ruby

SshSig is a Ruby gem which can be used to verify signatures signed created by `ssh-keygen`.
This capability was [first added](https://github.com/openssh/openssh-portable/commit/2a9c9f7272c1e8665155118fe6536bebdafb6166) in OpenSSH 8.0
allows SSH keys to be used for GPG-like signing capabilities, [including signing git commits](https://github.com/git/git/pull/1041).

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'ssh_sig'
```

And then execute:

    $ bundle install

Or install it yourself as:

    $ gem install ssh_sig

## Usage

Version 1 of [the SSH signature format](https://github.com/openssh/openssh-portable/blob/b7ffbb17e37f59249c31f1ff59d6c5d80888f689/PROTOCOL.sshsig)
supports `ed25519` and `rsa` keys. It is recommended that you use `ed25519` over `rsa` where possible (`ssh-keygen -t ed25519`).

In order to verify a signature you need:

1. The public key of the sender
1. The signature file
1. The message to be verified.

```ruby
require 'ssh_sig'

armored_pubkey = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILXPkJPI4TMFWZP4xRBQjNeizUG99KuZCt9G23rX48kz"

blob = ::SshSig::Blob.from_armor(
  <<~EOF
  -----BEGIN SSH SIGNATURE-----
  U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAgtc+Qk8jhMwVZk/jFEFCM16LNQb
  30q5kK30bbetfjyTMAAAAEZmlsZQAAAAAAAAAGc2hhNTEyAAAAUwAAAAtzc2gtZWQyNTUx
  OQAAAECJITeYJIlEeydsCTh1DkfdhlDJFBa73ojfWe0MbrIzoJKd9THd9WeQrhygSRGsNG
  cU/stk3/919nykg67yG2gN
  -----END SSH SIGNATURE-----
  EOF
)

message = "This message was definitely sent by Brian Williams"

valid = ::SshSig::Verifier
  .from_armored_pubkey(armored_pubkey)
  .verify(blob, message)

if valid
  puts 'Signature is valid'
else
  puts 'Signature is not valid'
end
```

Signatures can be created using `ssh-keygen -Y sign -n file -f ~/.ssh/ed_25519 message.txt`
and will be outputted in `message.txt.sig`.

Public keys can be found in a variety of places, including:

- Your `~/.ssh/id_<alg>.pub` file
- `authorized_keys` files on servers
- `https://gitlab.com/<username>.keys`
- `https://github.com/<username>.keys`

The `SshSig::Verifier#from_gitlab` and `SshSig::Verifier#from_github` methods are provided
to automatically load public keys from the respective `<username>.keys` urls.

```ruby
require 'ssh_sig'

blob = ::SshSig::Blob.from_armor(
  <<~EOF
  -----BEGIN SSH SIGNATURE-----
  U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAgtc+Qk8jhMwVZk/jFEFCM16LNQb
  30q5kK30bbetfjyTMAAAAEZmlsZQAAAAAAAAAGc2hhNTEyAAAAUwAAAAtzc2gtZWQyNTUx
  OQAAAECJITeYJIlEeydsCTh1DkfdhlDJFBa73ojfWe0MbrIzoJKd9THd9WeQrhygSRGsNG
  cU/stk3/919nykg67yG2gN
  -----END SSH SIGNATURE-----
  EOF
)

message = 'This message was definitely sent by Brian Williams'

valid = ::SshSig::Verifier
  .from_gitlab('bwill')
  .verify(blob, message)

if valid
  puts 'Signature is valid'
else
  puts 'Signature is not valid'
end
```

## Is it safe to re-purpose SSH keys for signing?

Yes. The [SSH signature protocol](https://github.com/openssh/openssh-portable/blob/d575cf44895104e0fcb0629920fb645207218129/PROTOCOL.sshsig)
is designed to be resistant to cross-protocol attacks, where signatures created for one purpose (i.e. signing a git commit),
may be re-used for another purpose (i.e. authenticating to a server). It does this using the magic pre-amble (to differentiate
between messages signed by `ssh-keygen` and messages used for SSH authentication) and namespaces (to differentiate between
messages signed by `ssh-keygen` but used for different purposes). This causes identical messages to produce different signatures
for each different protocol.

## Development

After checking out the repo, run `bin/setup` to install dependencies. Then, run `rake spec` to run the tests. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and the created tag, and push the `.gem` file to [rubygems.org](https://rubygems.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/[USERNAME]/ssh_sig. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [code of conduct](https://github.com/[USERNAME]/ssh_sig/blob/main/CODE_OF_CONDUCT.md).

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## 官网

- 主页: https://gitlab.com/bwill/ssh_sig
- 更新日志: https://gitlab.com/bwill/ssh_sig/-/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/ssh_sig

## 历史版本号

- 0.1.1 (2021-12-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/ssh_sig
- gem 安装: `gem install ssh_sig`
- Bundler: `gem "ssh_sig"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/ssh_sig-0.1.1.gem
- 版本锁定: `gem "ssh_sig", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
