# spree_suppliers

**Tag**: template

## 简介

This gem (spree extension) provides support for multiple suppliers in one store. Products should be assigned to the supplier that they belong to, which allows you to select a supplier and view only their products. Suppliers can be associated with Taxons that allow the customer to search for suppliers by taxon. Orders are also broken up into supplier invoices (one for each different supplier in the order), which list only the products that were purchased from that supplier. A mailer is in place to send each supplier their unique invoice descrbing what products they have sold and to who. The spree order mailer has also been modified to show all of the supplier invoices to the customer, along with the standard spree order number and info. The checkout process is combined so the customer only makes one transaction - the transaction can then be divided up amongst the suppliers involved in the transaction, according to the supplier_invoices. There is also an option for the site administrator to charge a percentage fee on each transaction to suppliers (this is currently set to 0%, but can be changed).

## 官网

- 主页: http://github.com/johndavid400/spree_suppliers
- 源码仓库: https://github.com/johndavid400/spree_suppliers
- RubyGems: https://rubygems.org/gems/spree_suppliers

## 历史版本号

- 1.0.4 (2012-02-06)
- 1.0.3 (2012-02-06)
- 1.0.2 (2012-02-06)
- 1.0.1 (2012-02-06)
- 1.0.0 (2012-02-06)
- 0.1.0 (2012-02-06)
- 0.0.1 (2011-12-06)
- 0.60.3 (2011-12-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/spree_suppliers
- gem 安装: `gem install spree_suppliers`
- Bundler: `gem "spree_suppliers"`
- 最新版本: 1.0.4
- 最新版归档: https://rubygems.org/downloads/spree_suppliers-1.0.4.gem
- 版本锁定: `gem "spree_suppliers", "~> 1.0.4"`
- 中央仓库: https://rubygems.org/
