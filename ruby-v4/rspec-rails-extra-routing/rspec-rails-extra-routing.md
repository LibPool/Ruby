# rspec-rails-extra-routing

**Tag**: web, testing

## 简介

Extension to rspec-rails that allows some shortcuts in routing tests.

With it, this:

  describe "users routes" do

    describe "GET /" do

      it{{:get => '/'}.should route_to "users#index"}

    end



    describe "POST /" do

      it{{:post => '/'}.should be_routable}

    end

  end



can be written like this:



  describe "users routes" do

    get('/').should route_to "users#index"

    post('/').should be_routable

  end

## 官网

- 主页: http://github.com/HugoLnx/rspec-rails-extra-routing
- RubyGems: https://rubygems.org/gems/rspec-rails-extra-routing

## 历史版本号

- 0.1.0 (2011-04-05)
- 0.0.6 (2011-04-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/rspec-rails-extra-routing
- gem 安装: `gem install rspec-rails-extra-routing`
- Bundler: `gem "rspec-rails-extra-routing"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/rspec-rails-extra-routing-0.1.0.gem
- 版本锁定: `gem "rspec-rails-extra-routing", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
