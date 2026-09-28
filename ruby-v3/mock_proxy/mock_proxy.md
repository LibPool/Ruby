# mock_proxy

**Tag**: cli, testing

## 简介

Remember when RSpec had stub_chain? They removed it for good reasons but sometimes you just need it.
  Well, here it is, a proxy object. It doesn't actually mock anything for you (the name is just catchy) so you need to do that.
  But that actually comes with a lot of benefits:
  1) It's compatable with any testing framework
  2) You can use it for purposes other than testing, e.g. prototyping, code stubs
  3) Flexibility in how you use it without overloading the number of methods you have to remember

  Here's an example usage:
  let(:model_proxy) do
    MockProxy.new(email_client: {
      create_email: {
        receive: proc {}
      }
    })
  end
  before { allow(Model).to receive(:new).and_return model_proxy }
  it 'should call receive' do
    proc = MockProxy.get(model_proxy, 'email_client.create_email.receive')
    expect(proc).to receive(:call)
    run_system_under_test
    MockProxy.update(mock_proxy, 'email_client.create_email.validate!') { true }
    MockProxy.observe(mock_proxy, 'email_client.create_email.send') do |to|
      expect(to).to eq 'stop@emailing.me'
    end
    run_system_under_test2
  end

  As you can see, the proc - which ends the proxy by calling the proc - can be used for anything. You can spy on the
  call count and arguments, mock methods, or just stub out code you don't want executed. Because it doesn't make any
  assumptions, it becomes very flexible. Simple, yet powerful, it's uses are infinite. Enjoy

## 官网

- 主页: https://github.com/matrinox/MockProxy
- 文档: https://www.rubydoc.info/gems/mock_proxy/0.4.6
- RubyGems: https://rubygems.org/gems/mock_proxy

## 历史版本号

- 0.4.6 (2016-08-15)
- 0.4.1 (2016-08-12)
- 0.4.0 (2016-08-12)
- 0.3.0 (2016-02-19)
- 0.2.3 (2016-02-19)
- 0.2.2 (2016-02-19)
- 0.2.1 (2016-02-19)
- 0.2.0 (2016-02-19)
- 0.1.3 (2016-02-19)
- 0.1.2 (2016-02-19)
- 0.1.1 (2016-02-19)
- 0.1.0 (2016-02-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/mock_proxy
- gem 安装: `gem install mock_proxy`
- Bundler: `gem "mock_proxy"`
- 最新版本: 0.4.6
- 最新版归档: https://rubygems.org/downloads/mock_proxy-0.4.6.gem
- 版本锁定: `gem "mock_proxy", "~> 0.4.6"`
- 中央仓库: https://rubygems.org/
