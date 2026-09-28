# glslkit-webgl

**Tag**: web, template, tooling, filesystem

## 简介

Lets you write WebGL2 rendering code entirely in Ruby, running under ruby.wasm in the browser. Resolves uniform/attribute locations from a glslkit reflection manifest instead of calling getActiveUniform, and surfaces shader compile errors as Ruby exceptions pointing at the original file and line. REQUIRES a ruby.wasm runtime (the `js` gem) to run — it installs under a normal CRuby/JRuby/TruffleRuby, but raises a clear LoadError instead of working there. This gem is meant to be bundled into a ruby.wasm build (see README), not required from a regular Ruby process.

## 官网

- 主页: https://github.com/kyubey1228/glslkit
- 源码仓库: https://github.com/kyubey1228/glslkit/tree/main/webgl
- 更新日志: https://github.com/kyubey1228/glslkit/blob/main/webgl/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/glslkit-webgl

## 历史版本号

- 0.1.0 (2026-08-24)
- 0.1.0.pre (2026-08-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/glslkit-webgl
- gem 安装: `gem install glslkit-webgl`
- Bundler: `gem "glslkit-webgl"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/glslkit-webgl-0.1.0.gem
- 版本锁定: `gem "glslkit-webgl", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
