# pikuri-thunderbird

**Tag**: database, networking, tooling, filesystem, data

## 简介

pikuri-thunderbird lets a pikuri agent search and read the user's
*local* Thunderbird data — mail folders and cached calendars — by
reading Thunderbird's own on-disk profile. It never speaks
IMAP/POP3/SMTP itself and never egresses: search and read are both
inbound-only, so the v1 demo (+bin/pikuri-thunderbird+) breaks the
lethal trifecta by construction, exactly like +bin/pikuri-corpus+.

Mail search rides Thunderbird's Gloda index
(+global-messages-db.sqlite+) as a pre-decoded corpus: pikuri copies a
consistent snapshot, builds its own ephemeral FTS5 index over the
decoded columns, and serves ranked search + full-body reads with no
MIME parsing. Calendar reads come from the +calendar-data/*.sqlite+
stores (normalized columns, no ICS parser for the common case).

Any *outbound* action (compose a mail, create an event) is a v2
feature and is always a human-gated hand-off to Thunderbird's own UI —
pikuri writes nothing to Thunderbird's stores and sends nothing itself.
See +pikuri-thunderbird/DESIGN.md+ and +ideas/thunderbird.md+.

## 官网

- 主页: https://codeberg.org/mvysny/pikuri
- 源码仓库: https://codeberg.org/mvysny/pikuri/src/branch/master
- 更新日志: https://codeberg.org/mvysny/pikuri/src/branch/master/CHANGELOG.md
- 问题追踪: https://codeberg.org/mvysny/pikuri/issues
- RubyGems: https://rubygems.org/gems/pikuri-thunderbird

## 历史版本号

- 0.1.0 (2026-08-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/pikuri-thunderbird
- gem 安装: `gem install pikuri-thunderbird`
- Bundler: `gem "pikuri-thunderbird"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pikuri-thunderbird-0.1.0.gem
- 版本锁定: `gem "pikuri-thunderbird", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
