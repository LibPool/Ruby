# sangoro

**Tag**: web, cli, testing, networking, filesystem

## 简介

# Sangoro
A Ruby program to change the exif creation time stamp of JPEGs or PNGs.<br>


# Installation
To use the Sangoro tool you require:
<ul>
  <li> <a href="https://www.ruby-lang.org/en/downloads/"><code>ruby</code></a> (v>=2.3.3)
</ul>
as well as the following Ruby gems:  
<ul>
  <li><code>fastimage</code>
  <li><code>fileutils</code>
  <li><code>gtk3</code>
  <li><code>mini_exiftool</code></li>
</ul>  

On Mac you might need the exiftool installed. I recommend installing it using the Brew package manager:
```brew install exiftool```

Get the Sangoro tool by typing ```gem install sangoro``` in your command line. This will install the sangoro gem as well as the gems mentined above.
Now you can just run ```sangoro``` in your command line.

# Usage
1. Select a JPEG/PNG file by clicking on "Select image"
2. You will see the file name and the creation date & time on the right side, if available.
3. Now you can specify by how many hours, minutes and/or seconds you want the time stamp to move. You also need to choose whether to move the timestamp forward or back.
4. If you want to apply this change to all images in the folder, check the box below.
5. Click "Apply". 
6. You are done. The exif creation timestamp of the selected image(s) was adjusted as specified.

# Remarks  
If you have any remarks, bugs, questions etc. please tell me, I'd be happy to help.

## 官网

- 主页: https://github.com/BluePeony/sangoro
- 文档: https://www.rubydoc.info/gems/sangoro/1.0.2
- RubyGems: https://rubygems.org/gems/sangoro

## 历史版本号

- 1.0.2 (2023-05-17)
- 1.0.1 (2023-05-16)
- 1.0.0 (2023-03-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/sangoro
- gem 安装: `gem install sangoro`
- Bundler: `gem "sangoro"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/sangoro-1.0.2.gem
- 版本锁定: `gem "sangoro", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
