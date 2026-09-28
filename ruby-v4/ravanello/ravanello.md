# ravanello

**Tag**: cli, database, testing, filesystem

## 简介

Ravanello is the cli for analyze keys in redis and size of it's values.

    Example of usage:
    ```bash
      gem install ravanello
      ravanello --version
      REDIS_URL="redis://localhost/db" ravanello analyze --rules rules.yml
    ```

    The rules files specifies the structure of the redis keys (splitted by :)
    and should looks like this:
    ```yml
    rules:
      resque:
        - 'delayed'
        - 'resque-retry'
        - 'timestamps'
        - 'lock'
        - 'meta'
    ```

    After analyzing you will get the report in console:
    ```
    Q-ty  Size  Key (sample)
    4     24    * (hello)
    1     6     denormalized:companies:* (denormalized:companies:99585213)
    ```

## 官网

- 主页: https://github.com/dsalahutdinov/ravanello
- 文档: https://www.rubydoc.info/gems/ravanello/0.1.1
- RubyGems: https://rubygems.org/gems/ravanello

## 历史版本号

- 0.1.1 (2017-12-11)
- 0.1.0 (2017-12-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/ravanello
- gem 安装: `gem install ravanello`
- Bundler: `gem "ravanello"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/ravanello-0.1.1.gem
- 版本锁定: `gem "ravanello", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
