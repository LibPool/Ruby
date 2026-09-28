# school_year

**Tag**: library

## 简介

# School Year
    Simple logic for translating between academic year and grade for a student

    ## Sample Usage
    `SchoolYear.grade_to_graduation_year(grade, academic_year)` determines the graduation year for a student based on their grade and the academic year    `SchoolYear.grade_to_year(grade, graduation_year)` determines the calendar year from the student's grade based on the graduation year
    `SchoolYear.year_to_grade(year, graduation_year)` determines the student's grade from the calendar year based on the graduation year
    `SchoolYear.default_first_day_of_school(academic_year_or_date)` determines the first day of school (as September 1st) based on an integer representing the academic year (e.g., 1998), or a date (e.g., '1998-04-04'.to_date)
    `SchoolYear.default_last_day_of_school(academic_year_or_date)` determines the last day of school (as June 15th) based on an integer representing the academic year (e.g., 1998), or a date (e.g., '1998-04-04'.to_date)
    `SchoolYear.school_days_elapsed(date, first_attendace_day)` determines the approximate number of days elapsed from the first_attendance_day to the date. Both arguments can be blank: if date is blank, the approximate number of total days in the 1901 school year will be returned.

## 官网

- 主页: http://www.puzzlesandwich.com
- 文档: https://www.rubydoc.info/gems/school_year/0.2.0
- RubyGems: https://rubygems.org/gems/school_year

## 历史版本号

- 0.2.0 (2021-09-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/school_year
- gem 安装: `gem install school_year`
- Bundler: `gem "school_year"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/school_year-0.2.0.gem
- 版本锁定: `gem "school_year", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
