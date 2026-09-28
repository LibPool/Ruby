# stb_image_ffi

**Tag**: data

## 简介

Very naive bindings for stb_image.h. Implements only stbi_set_flip_vertically_on_load and stb_load since these are the 2 functions I need to load an image as a texture in OpenGL.

The reason I made this instead of using stb-image is because stb-image didn't implement stbi_set_flip_vertically_on_load, as far as I can tell, which is useful/necessary when wanting to load image data in a format immediately consumable by OpenGL (see Example in README).

## 官网

- 主页: https://github.com/boatrite/stb_image_ffi
- 文档: https://www.rubydoc.info/gems/stb_image_ffi/1.0.2
- RubyGems: https://rubygems.org/gems/stb_image_ffi

## 历史版本号

- 1.0.2 (2019-10-03)
- 1.0.1 (2019-10-02)
- 1.0.0 (2019-10-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/stb_image_ffi
- gem 安装: `gem install stb_image_ffi`
- Bundler: `gem "stb_image_ffi"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/stb_image_ffi-1.0.2.gem
- 版本锁定: `gem "stb_image_ffi", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
