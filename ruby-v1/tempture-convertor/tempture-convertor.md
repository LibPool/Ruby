# tempture-convertor

**Tag**: testing

## 简介

# Temperature Convertor

convert temperature from fehrenheit or kelvin to celsius


## Detail

The "Temperature" class stores and controls the value and convert function

**Constructor**

> ` def initialize(temperature, mode) `

The initialization process retrieve temperature user input and specific Temperature Mode and store temperature in celsius form.<br>
[param] temperature: float --> the temperature value<br>
[param] mode: TemperatureMode --> the temperature unit (Fahrenheit, Celsius or Kelvin)<br>
Note the TemperatureMode is an enumerate that holds value of TemperatureMode::Celsius, TemperatureMode::Fahrenheit or TemperatureMode::Kelvin. The implementation is:<br>

```ruby
module TemperatureMode
  Celsius = 1
  Fahrenheit = 2
  Kelvin = 4
end
```

**method**

> ` def toFahrenheit() `

Convert the temperature to Fahrenheit<br>
[return] temperature in Fahrenheit, type in float<br>

> ` def toKelvin() `

Convert the temperature to Kelvin<br>
[return] temperature in Kelvin, type in float<br>

**Property**

> ` this.temperature `

temperature in Celsius, type in float

## Get Start

Use following script for testing

```ruby
temp = Temperature.new(-24, 1)

puts temp.toString
puts "Current temperature is #{'%.2f' % temp.toFahrenheit} °F"
puts "Current temperature is #{'%.2f' % temp.toKelvin} K"
```

## 官网

- 主页: https://github.com/Ayano-Keiko
- 文档: https://www.rubydoc.info/gems/tempture-convertor/0.1.1
- RubyGems: https://rubygems.org/gems/tempture-convertor

## 历史版本号

- 0.1.1 (2026-03-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/tempture-convertor
- gem 安装: `gem install tempture-convertor`
- Bundler: `gem "tempture-convertor"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/tempture-convertor-0.1.1.gem
- 版本锁定: `gem "tempture-convertor", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
