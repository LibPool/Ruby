# wxjsapi

**Tag**: web

## 简介

所有需要使用JS-SDK的页面必须先注入配置信息，否则将无法调用（同一个url仅需调用一次，对于变化url的SPA的web app可在每次url变化时进行调用,目前Android微信客户端不支持pushState的H5新特性，所以使用pushState来实现web app的页面会导致签名失败，此问题会在Android6.2中修复）。wx.config({
      debug: true, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
      appId: '', // 必填，公众号的唯一标识
      timestamp: , // 必填，生成签名的时间戳
      nonceStr: '', // 必填，生成签名的随机串
      signature: '',// 必填，签名，见附录1
      jsApiList: [] // 必填，需要使用的JS接口列表，所有JS接口列表见附录2
  });

## 官网

- 主页: https://github.com/VitalYoung/wxjsapi-config
- 文档: https://www.rubydoc.info/gems/wxjsapi/0.1.3
- RubyGems: https://rubygems.org/gems/wxjsapi

## 历史版本号

- 0.1.3 (2016-04-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/wxjsapi
- gem 安装: `gem install wxjsapi`
- Bundler: `gem "wxjsapi"`
- 最新版本: 0.1.3
- 最新版归档: https://rubygems.org/downloads/wxjsapi-0.1.3.gem
- 版本锁定: `gem "wxjsapi", "~> 0.1.3"`
- 中央仓库: https://rubygems.org/
