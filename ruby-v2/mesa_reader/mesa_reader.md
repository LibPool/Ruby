# mesa_reader

**Tag**: web, testing, networking, filesystem, data

## 简介

MesaReader is a ruby module that contains three classes, MesaData,
    MesaProfileIndex, and MesaLogDir. These classes are intended to read in
    three types of files or directories, MESA history/profile logs, MESA 
    profile indexes, and entire MESA LOGS directories, respectively. The
    resulting objects can then be maniuplated to return useful data in a ruby
    or tioga script.

    In addition to simple returning of data columns (the primary function of 
    the MesaData class), some basic searching features are built-in, allowing 
    you to search for profiles that correspond to something in the history, or
    for parts of history columns that depend on other history columns. All
    returned vectors have many built-in methods since they are DVectors from
    the DObjects module in Tioga, which is a requirement.

    For detailed instructions, see the readme on the github page at 

    https://github.com/wmwolf/MESA_Reader

## 官网

- 主页: https://wmwolf.github.io
- 文档: https://www.rubydoc.info/gems/mesa_reader/0.1.0
- RubyGems: https://rubygems.org/gems/mesa_reader

## 历史版本号

- 0.1.0 (2014-12-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/mesa_reader
- gem 安装: `gem install mesa_reader`
- Bundler: `gem "mesa_reader"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/mesa_reader-0.1.0.gem
- 版本锁定: `gem "mesa_reader", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
