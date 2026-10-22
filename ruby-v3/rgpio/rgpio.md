# rgpio

**Tag**: web

## 简介

Control a Raspberry Pi's hardware from Ruby. GPIO goes through libgpiod v2 — the Linux GPIO character device (uAPI v2) — rather than the deprecated sysfs interface. PWM is either the hardware peripheral through sysfs or timed in Ruby on any line; I2C and SPI are ioctl calls on /dev/i2c-N and /dev/spidev, needing no libgpiod at all. On top sits a gpiozero-style device layer: LED, Button, Motor, PWMLED, RGBLED, Servo, and drivers for the ADT7410 temperature sensor, ST7032 character LCD and MCP3208 ADC. Bound through the stdlib `fiddle`, which is built with the interpreter and so matches any Pi's architecture, unlike the precompiled `ffi` gem.

## 官网

- 主页: https://github.com/lumbermill/rgpio
- 更新日志: https://github.com/lumbermill/rgpio/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/lumbermill/rgpio/issues
- RubyGems: https://rubygems.org/gems/rgpio

## 历史版本号

- 0.1.0 (2026-09-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/rgpio
- gem 安装: `gem install rgpio`
- Bundler: `gem "rgpio"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/rgpio-0.1.0.gem
- 版本锁定: `gem "rgpio", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
