# circuit_breaker

**Tag**: testing

## 简介

CircuitBreaker is a relatively simple Ruby mixin that will wrap
 a call to a given service in a circuit breaker pattern.

 The circuit starts off "closed" meaning that all calls will go through.
 However, consecutive failures are recorded and after a threshold is reached,
 the circuit will "trip", setting the circuit into an "open" state.

 In an "open" state, every call to the service will fail by raising
 CircuitBrokenException.

 The circuit will remain in an "open" state until the failure timeout has
 elapsed.

 After the failure_timeout has elapsed, the circuit will go into
 a "half open" state and the call will go through.  A failure will
 immediately pop the circuit open again, and a success will close the
 circuit and reset the failure count.

     require 'circuit_breaker'
     class TestService

       include CircuitBreaker

       def call_remote_service() ...

       circuit_method :call_remote_service

       # Optional
       circuit_handler do |handler|
         handler.logger = Logger.new(STDOUT)
         handler.failure_threshold = 5
         handler.failure_timeout = 5
       end

       # Optional
       circuit_handler_class MyCustomCircuitHandler
     end

## 官网

- 主页: http://github.com/wsargent/circuit_breaker
- 文档: https://www.rubydoc.info/gems/circuit_breaker/1.1.2
- RubyGems: https://rubygems.org/gems/circuit_breaker

## 历史版本号

- 1.1.2 (2016-01-11)
- 1.1.1 (2014-03-06)
- 1.1.0 (2013-04-19)
- 1.0.1 (2012-01-05)
- 1.0.0 (2009-08-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/circuit_breaker
- gem 安装: `gem install circuit_breaker`
- Bundler: `gem "circuit_breaker"`
- 最新版本: 1.1.2
- 最新版归档: https://rubygems.org/downloads/circuit_breaker-1.1.2.gem
- 版本锁定: `gem "circuit_breaker", "~> 1.1.2"`
- 中央仓库: https://rubygems.org/
