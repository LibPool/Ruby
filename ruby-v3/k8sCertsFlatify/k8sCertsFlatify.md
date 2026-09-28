# k8sCertsFlatify

**Tag**: devops, filesystem

## 简介

A script which extracts 1 or multiple tls/ssl certificates from a kubernetes cluster to PWD.
NOTE: Will not check the TLS certificate of the connecting kubernetes cluster as of the current time.
Switch --kubeconfig/-c <kubernetes kubeconfig file>. If not present default to ~/.kube/config
switch --namespaces/-n -- Namespace to dump certificates in. If not present, will dump certificates of all namespaces.
--context/-k -- The context to use in the kubeconfig file.
--dumpdir/-d -- Dump certificates to this directory instead of PWD
Will dump certificates in PWD in a directory with the name as the DNS to which the certificate belongs.

## 官网

- 文档: https://www.rubydoc.info/gems/k8sCertsFlatify/0.1.3
- RubyGems: https://rubygems.org/gems/k8sCertsFlatify

## 历史版本号

- 0.1.3-universal-linux (2025-02-11)
- 0.1.2-universal-linux (2025-01-30)
- 0.1.1-universal-linux (2024-11-06)
- 0.1.0-universal-linux (2024-11-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/k8sCertsFlatify
- gem 安装: `gem install k8sCertsFlatify`
- Bundler: `gem "k8sCertsFlatify"`
- 最新版本: 0.1.3
- 最新版归档: https://rubygems.org/downloads/k8sCertsFlatify-0.1.3.gem
- 版本锁定: `gem "k8sCertsFlatify", "~> 0.1.3"`
- 中央仓库: https://rubygems.org/
