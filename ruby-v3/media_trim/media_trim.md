# media_trim

**Tag**: testing, template, filesystem

## 简介

Trim an audio or video file using ffmpeg

- Works with all formats supported by ffmpeg, including mp3, mp4, mkv, and many more.
- Seeks to the nearest frame positions by re-encoding the media.
- Reduces file size procduced by OBS Studio by over 80 percent.
- Can be used as a Ruby gem.
- Installs the 'trim' command.

When run as a command, output files are named by adding a 'trim.' prefix to the media file name, e.g. 'dir/trim.file.ext'.
By default, the trim command does not overwrite pre-existing output files.
When trimming is complete, the trim command displays the trimmed file, unless the -q option is specified

Command-line Usage:
  trim [OPTIONS] dir/file.ext start [[to|for] end]

- The start and end timecodes have the format [HH:[MM:]]SS[.XXX]
  Note that decimal seconds may be specified, bug frames may not;
  this is consistent with how ffmpeg parses timecodes.
- end defaults to end of the audio/video file

OPTIONS are:
  -d Enable debug output.
  -f Overwrite output file if present.
  -h Display help information.
  -v Verbose output.
  -V Do not @view the trimmed file when complete.

Examples:
  # Crop dir/file.mp4 from 15.0 seconds to the end of the video, save to demo/trim.demo.mp4:
  trim demo/demo.mp4 15

  # Crop dir/file.mkv from 3 minutes, 25 seconds to 9 minutes, 35 seconds, save to demo/trim.demo.mp4:
  trim demo/demo.mp4 3:25 9:35

  # Same as the previous example, using optional 'to' syntax:
  trim demo/demo.mp4 3:25 to 9:35

  # Save as the previous example, but specify the duration instead of the end time by using the for keyword:
  trim demo/demo.mp4 3:25 for 6:10

## 官网

- 主页: https://www.mslinn.com/av_studio/425-trimming-media.html
- 源码仓库: https://github.com/mslinn/media_trim
- 更新日志: https://github.com/mslinn/media_trim/CHANGELOG.md
- 问题追踪: https://github.com/mslinn/media_trim/issues
- RubyGems: https://rubygems.org/gems/media_trim

## 历史版本号

- 0.2.2 (2026-08-24)
- 0.2.1 (2026-07-21)
- 0.2.0 (2023-11-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/media_trim
- gem 安装: `gem install media_trim`
- Bundler: `gem "media_trim"`
- 最新版本: 0.2.2
- 最新版归档: https://rubygems.org/downloads/media_trim-0.2.2.gem
- 版本锁定: `gem "media_trim", "~> 0.2.2"`
- 中央仓库: https://rubygems.org/
