# kalman_filter

**Tag**: data

## 简介

Noisy sensor data, approximations in the equations that
    describe the system evolution, and external factors that are not accounted
    for all place limits on how well it is possible to determine the system's
    state. The Kalman filter deals effectively with the uncertainty due to
    noisy sensor data and to some extent also with random external factors.
    The Kalman filter produces an estimate of the state of the system as an
    average of the system's predicted state and of the new measurement using a
    weighted average. The purpose of the weights is that values with better
    (i.e., smaller) estimated uncertainty are "trusted" more. The weights
    are calculated from the covariance, a measure of the estimated uncertainty
    of the prediction of the system's state. The result of the weighted
    average is a new state estimate that lies between the predicted and
    measured state, and has a better estimated uncertainty than either alone.
    This process is repeated at every time step, with the new estimate and its
    covariance informing the prediction used in the following iteration. This
    means that the Kalman filter works recursively and requires only the last
    "best guess", rather than the entire history, of a system's state to
    calculate a new state.

## 官网

- 主页: https://github.com/jjviscomi/kalman-filter
- 文档: https://www.rubydoc.info/gems/kalman_filter/1.0.2
- 问题追踪: https://github.com/jjviscomi/kalman-filter/issues
- RubyGems: https://rubygems.org/gems/kalman_filter

## 历史版本号

- 1.0.2 (2020-08-19)
- 1.0.1 (2016-11-07)
- 1.0.0 (2016-11-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/kalman_filter
- gem 安装: `gem install kalman_filter`
- Bundler: `gem "kalman_filter"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/kalman_filter-1.0.2.gem
- 版本锁定: `gem "kalman_filter", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
