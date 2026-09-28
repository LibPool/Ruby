# still_active

**Tag**: cli, testing, serialization, filesystem

## 简介

Analyses your Gemfile.lock for dependency health across the full transitive graph: whether each gem is actively maintained (last activity on GitHub, GitLab, or Codeberg/Forgejo, plus release recency), outdated versions, archived repos, OpenSSF Scorecard scores, known vulnerabilities (deps.dev and OSV, merged with ruby-advisory-db, flagging advisories with no fix and pins that sit below the fix), poison-pill compatibility ceilings, and libyear drift. Ruby version freshness with EOL detection. The same maintenance lens travels cross-ecosystem: point --sbom at a CycloneDX SBOM to assess npm, PyPI, Cargo, Go, Maven, and NuGet packages via deps.dev and ecosyste.ms. Handles rubygems, git, path, GitHub Packages, and JFrog Artifactory sources. Outputs coloured terminal tables, markdown, JSON (with a versioned, contract-tested schema), SARIF for GitHub code scanning, and a CycloneDX SBOM. CI quality gates (--fail-if-critical / -warning / -vulnerable / -outdated / -poison / -language-ceiling) with granular, committed suppression via .still_active.yml. Complements bundle outdated, bundler-audit, and libyear-bundler by adding the maintenance signal they don't, and folds their version, CVE, and libyear checks into one report.

## 官网

- 主页: https://github.com/SeanLF/still_active
- 文档: https://github.com/SeanLF/still_active#readme
- 更新日志: https://github.com/SeanLF/still_active/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/SeanLF/still_active/issues
- RubyGems: https://rubygems.org/gems/still_active

## 历史版本号

- 3.2.0 (2026-09-25)
- 3.1.0 (2026-09-07)
- 3.0.0 (2026-08-21)
- 3.0.0.rc6 (2026-07-31)
- 3.0.0.rc5 (2026-07-29)
- 3.0.0.rc4 (2026-07-13)
- 3.0.0.rc3 (2026-07-13)
- 3.0.0.rc2 (2026-07-09)
- 3.0.0.rc1 (2026-07-05)
- 2.0.0 (2026-06-14)
- 1.6.0 (2026-06-08)
- 1.5.0 (2026-05-23)
- 1.4.2 (2026-05-22)
- 1.4.1 (2026-05-22)
- 1.4.0 (2026-05-22)
- 1.3.0 (2026-04-08)
- 1.2.1 (2026-02-20)
- 1.2.0 (2026-02-20)
- 1.1.0 (2026-02-20)
- 1.0.1 (2026-02-19)
- 1.0.0 (2026-02-19)
- 0.5.0 (2023-05-21)
- 0.4.1 (2022-02-01)
- 0.4.0 (2021-11-11)
- 0.3.0 (2021-11-11)
- 0.2.0 (2021-11-11)
- 0.1.1 (2021-11-07)
- 0.1.0 (2021-11-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/still_active
- gem 安装: `gem install still_active`
- Bundler: `gem "still_active"`
- 最新版本: 3.2.0
- 最新版归档: https://rubygems.org/downloads/still_active-3.2.0.gem
- 版本锁定: `gem "still_active", "~> 3.2.0"`
- 中央仓库: https://rubygems.org/
