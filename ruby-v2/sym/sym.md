# sym

**Tag**: web, cli, security, networking, devops, filesystem, data

## 简介

Sym is a ruby library (gem) that offers both the command line interface 
 (CLI) and a set of rich Ruby APIs, which make it rather trivial to add 
 encryption and decryption of sensitive data to your development or deployment 
 workflow.
 
 For additional security the private key itself can be encrypted with a 
 user-generated password. For decryption using the key the password can be 
 input into STDIN, or be defined by an ENV variable, or an OS-X Keychain Entry. 
 
 Unlike many other existing encryption tools, Sym focuses on getting out of 
 your way by offering a streamlined interface with password caching (if 
 MemCached is installed and running locally) in hopes to make encryption of 
 application secrets nearly completely transparent to the developers. 
 
 Sym uses symmetric 256-bit key encryption with the AES-256-CBC cipher, 
 same cipher as used by the US Government. 
 
 For password-protecting the key Sym uses AES-128-CBC cipher. The resulting 
 data is zlib-compressed and base64-encoded. The keys are also base64 encoded 
 for easy copying/pasting/etc.
 
 Sym accomplishes encryption transparency by combining several convenient features:
  
   1. Sym can read the private key from multiple source types, such as pathname, 
      an environment variable name, a keychain entry, or CLI argument. You simply 
      pass either of these to the -k flag — one flag that works for all source types.
  
   2. By utilizing OS-X Keychain on a Mac, Sym offers truly secure way of 
      storing the key on a local machine, much more secure then storing it on a file system,
  
   3. By using a local password cache (activated with -c) via an in-memory provider 
      such as memcached, sym invocations take advantage of password cache, and 
      only ask for a password once per a configurable time period, 
 
   4. By using SYM_ARGS environment variable, where common flags can be saved. This 
      is activated with sym -A,
  
   5. By reading the key from the default key source file ~/.sym.key which 
      requires no flags at all,
  
   6. By utilizing the --negate option to quickly encrypt a regular file, or decrypt 
      an encrypted file with extension .enc
  
   7. By implementing the -t (edit) mode, that opens an encrypted file in your $EDITOR, 
      and replaces the encrypted version upon save & exit, optionally creating a backup.
  
   8. By offering the Sym::MagicFile ruby API to easily read encrypted files into memory.

Please refer the module documentation available here:
https://www.rubydoc.info/gems/sym

## 官网

- 主页: https://github.com/kigster/sym
- 文档: https://www.rubydoc.info/gems/sym/3.0.2
- RubyGems: https://rubygems.org/gems/sym

## 历史版本号

- 3.0.2 (2022-09-23)
- 3.0.1 (2021-02-12)
- 3.0.0 (2020-08-15)
- 2.10.0 (2020-08-14)
- 2.8.5 (2018-10-13)
- 2.8.4 (2018-04-13)
- 2.8.2 (2018-01-10)
- 2.8.1 (2018-01-07)
- 2.8.0 (2018-01-06)
- 2.7.0 (2017-06-23)
- 2.6.3 (2017-03-13)
- 2.6.2 (2017-03-12)
- 2.6.1 (2017-03-12)
- 2.6.0 (2017-03-12)
- 2.5.3 (2017-03-11)
- 2.5.1 (2017-03-07)
- 2.5.0 (2017-03-05)
- 2.4.3 (2017-03-01)
- 2.3.0 (2017-02-25)
- 2.2.1 (2017-02-15)
- 2.2.0 (2017-02-14)
- 2.1.2 (2017-02-11)
- 2.1.1 (2017-02-05)
- 2.1.0 (2017-01-24)
- 2.0.3 (2017-01-22)
- 2.0.2 (2017-01-21)
- 2.0.1 (2017-01-20)
- 2.0.0 (2016-11-11)
- 0.1.0 (2016-11-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/sym
- gem 安装: `gem install sym`
- Bundler: `gem "sym"`
- 最新版本: 3.0.2
- 最新版归档: https://rubygems.org/downloads/sym-3.0.2.gem
- 版本锁定: `gem "sym", "~> 3.0.2"`
- 中央仓库: https://rubygems.org/
