# rails_config_model_generator

**Tag**: web, testing, security, template, tooling, filesystem

## 简介

== DESCRIPTION: Creates a configuration controller and model that can be used to quickly create configuration table for your system so you can store system-wide variables that you'd like the user to be able to set.  This gem contains a generator to create a simple configuration model, migration, and interface for your application, complete with working tests.  == FEATURES  * Generates the controller, model, and the associated files.   * You can specify the model name and set the fields for the migrations via the generator.  == SYNOPSIS:  === Setup and overview Generate a new configuration system for your application by executing the generator from the root of your application.  ruby script\generate rails_config_model Configuration  You can also specify the model fields much like the scaffold_resource generator  ruby script/generate rails_config_model Configuration contact_email:string site_name:string welcome_message:text max_number_of_events:integer  Once installed, you modify the generated migration to include the fields you want to configure. There are a few defaults there to give you an idea.  The generator will create a controller mounted at /configuration so you can edit your configurations.  Modify this as needed to provide for security.  === The Edit form The application's edit form uses the *form* helper method to auto-generate the fields. This may not be optimal and you may wish to actually write your own view instead. See app/views/configuration/edit.rhtml for more details.  === Usage Configuration is simply a model for this table. It is designed to handle a single row of a table, and so additional rows cannot be created.  If you have a table that looks like this:  id contact_email site_name welcome_message max_number_of_events  You simply grab the row from the table  @configuration = Configuration.load  and then grab the values out.  email = @configuration.contact_email  Or save new values  @configuration = Configuration.load @configuration.welcome_message = &quot;This is the default message.&quot; @configuraiton.save

## 官网

- 主页: http://rconfig.rubyforge.org/
- RubyGems: https://rubygems.org/gems/rails_config_model_generator

## 历史版本号

- 1.2.2 (2009-07-25)
- 1.2.1 (2009-07-25)
- 1.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails_config_model_generator
- gem 安装: `gem install rails_config_model_generator`
- Bundler: `gem "rails_config_model_generator"`
- 最新版本: 1.2.2
- 最新版归档: https://rubygems.org/downloads/rails_config_model_generator-1.2.2.gem
- 版本锁定: `gem "rails_config_model_generator", "~> 1.2.2"`
- 中央仓库: https://rubygems.org/
