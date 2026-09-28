# pastiepacker

**Tag**: web, networking, filesystem

## 简介

Prepare to pack or unpack piles of files with the pastiepacker.  To pack a folder: pastiepacker To pack some files ending with &quot;txt&quot;: find * | grep &quot;txt$&quot; | pastiepacker - It outputs the url of the prepared pastie, so you can pipe it to xargs: - pastiepacker | xargs open  To unpack a packed pastie: pastiepacker http://pastie.caboo.se/175886 - This unpacks the files into a subfolder 175886/

## 官网

- 主页: http://pastiepacker.rubyforge.org
- RubyGems: https://rubygems.org/gems/pastiepacker

## 历史版本号

- 1.1.1 (2009-07-25)
- 1.1.0 (2009-07-25)
- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/pastiepacker
- gem 安装: `gem install pastiepacker`
- Bundler: `gem "pastiepacker"`
- 最新版本: 1.1.1
- 最新版归档: https://rubygems.org/downloads/pastiepacker-1.1.1.gem
- 版本锁定: `gem "pastiepacker", "~> 1.1.1"`
- 中央仓库: https://rubygems.org/
