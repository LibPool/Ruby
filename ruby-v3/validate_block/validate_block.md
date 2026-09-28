# validate_block

**Tag**: testing

## 简介

This gem allows similar ActiveRecord validates_* commands to be grouped together in blocks and pruned of repeated parameters.

How often have you had a block of validation commands in an ActiveRecord object that are repeated, especially :id or :unless options?  Does this look familiar?

  validates_presence_of  :hair, :hair_color, :unless => :bald?
  validates_length_of    :hair, :within => 3..15, :unless => :bald?
  validates_inclusion_of :hair_color, :in => HAIR_COLORS, :unless => bald?

Instead, this gem will allow you to replace the above code with:

  validate_block :unless => :bald? do
    presence_of  :hair, :hair_color
    length_of    :hair, :within => 3..15
    inclusion_of :hair_color, :in => HAIR_COLORS
  end

..which is a great way to DRY your :hair, don't you think?

Basically, this gem 1) removes the requirement to have 'validates_' on the front of the commands and 2) passes the options on the validate_block command to each validation command inside the block.

The syntax of the validation commands remains the same.  Keeping the 'validates_*' prefix on the commands inside the block _will_ work but it is not required.

## 官网

- 主页: http://github.com/xunker/validate_block
- RubyGems: https://rubygems.org/gems/validate_block

## 历史版本号

- 0.2.0 (2010-09-13)
- 0.1.0 (2010-08-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/validate_block
- gem 安装: `gem install validate_block`
- Bundler: `gem "validate_block"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/validate_block-0.2.0.gem
- 版本锁定: `gem "validate_block", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
