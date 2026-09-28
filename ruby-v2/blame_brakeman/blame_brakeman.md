# blame_brakeman

**Tag**: security, serialization

## 简介

'git blame' added Brakeman JSON warnings. We have all the information at brakeman security warnings. 
                      But, Don't have a blame option for which developer done the vulnerabilities.Below is example.
                      
        {
         ....
        'blame': 'xxxxxxxxxxxxx (developer_name 2019-07-17 20:59:12 +0530 4226)  params.require(:users).permit!
'
         ...
        }

## 官网

- 主页: https://rubygems.org/gems/blame_brakeman
- 源码仓库: https://github.com/honestveera/blame_brakeman

## 历史版本号

- 0.0.3 (2019-12-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/blame_brakeman
- gem 安装: `gem install blame_brakeman`
- Bundler: `gem "blame_brakeman"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/blame_brakeman-0.0.3.gem
- 版本锁定: `gem "blame_brakeman", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
