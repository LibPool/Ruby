# right_aws

**Tag**: web, testing, serialization, networking, devops, filesystem, data

## 简介

== DESCRIPTION:

The RightScale AWS gems have been designed to provide a robust, fast, and secure interface to Amazon EC2, EBS, S3, SQS, SDB, and CloudFront.
These gems have been used in production by RightScale since late 2006 and are being maintained to track enhancements made by Amazon.
The RightScale AWS gems comprise:

- RightAws::Ec2 -- interface to Amazon EC2 (Elastic Compute Cloud) and the
  associated EBS (Elastic Block Store)
- RightAws::S3 and RightAws::S3Interface -- interface to Amazon S3 (Simple Storage Service)
- RightAws::Sqs and RightAws::SqsInterface -- interface to first-generation Amazon SQS (Simple Queue Service) (API version 2007-05-01)
- RightAws::SqsGen2 and RightAws::SqsGen2Interface -- interface to second-generation Amazon SQS (Simple Queue Service) (API version 2008-01-01)
- RightAws::SdbInterface and RightAws::ActiveSdb -- interface to Amazon SDB (SimpleDB)
- RightAws::AcfInterface -- interface to Amazon CloudFront, a content distribution service

== FEATURES:

- Full programmmatic access to EC2, EBS, S3, SQS, SDB, and CloudFront.
- Complete error handling: all operations check for errors and report complete
  error information by raising an AwsError.
- Persistent HTTP connections with robust network-level retry layer using
  RightHttpConnection).  This includes socket timeouts and retries.
- Robust HTTP-level retry layer.  Certain (user-adjustable) HTTP errors returned
  by Amazon's services are classified as temporary errors.
  These errors are automaticallly retried using exponentially increasing intervals.
  The number of retries is user-configurable.
- Fast REXML-based parsing of responses (as fast as a pure Ruby solution allows).
- Uses libxml (if available) for faster response parsing.
- Support for large S3 list operations.  Buckets and key subfolders containing
  many (> 1000) keys are listed in entirety.  Operations based on list (like
  bucket clear) work on arbitrary numbers of keys.
- Support for streaming GETs from S3, and streaming PUTs to S3 if the data source is a file.
- Support for single-threaded usage, multithreaded usage, as well as usage with multiple
  AWS accounts.
- Support for both first- and second-generation SQS (API versions 2007-05-01
  and 2008-01-01).  These versions of SQS are not compatible.
- Support for signature versions 0 and 1 on SQS, SDB, and EC2.
- Interoperability with any cloud running Eucalyptus (http://eucalyptus.cs.ucsb.edu)
- Test suite (requires AWS account to do "live" testing).

## 官网

- 文档: https://www.rubydoc.info/gems/right_aws/3.1.0
- RubyGems: https://rubygems.org/gems/right_aws

## 历史版本号

- 3.1.0 (2013-06-13)
- 3.0.5 (2013-03-05)
- 3.0.4 (2012-04-10)
- 3.0.3 (2012-03-08)
- 3.0.0 (2011-11-15)
- 2.1.0 (2011-03-29)
- 2.0.0 (2010-04-28)
- 1.10.0 (2009-07-25)
- 1.7.1 (2009-07-25)
- 1.7.0 (2009-07-25)
- 1.6.2 (2009-07-25)
- 1.6.1 (2009-07-25)
- 1.6.0 (2009-07-25)
- 1.5.0 (2009-07-25)
- 1.4.3 (2009-07-25)
- 1.4.2 (2009-07-25)
- 1.3.0 (2009-07-25)
- 1.2.0 (2009-07-25)
- 1.1.0 (2009-07-25)
- 1.9.0 (2009-07-25)
- 1.8.1 (2009-07-25)
- 1.8.0 (2009-07-25)
- 1.7.3 (2009-07-25)
- 1.7.2 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/right_aws
- gem 安装: `gem install right_aws`
- Bundler: `gem "right_aws"`
- 最新版本: 3.1.0
- 最新版归档: https://rubygems.org/downloads/right_aws-3.1.0.gem
- 版本锁定: `gem "right_aws", "~> 3.1.0"`
- 中央仓库: https://rubygems.org/
