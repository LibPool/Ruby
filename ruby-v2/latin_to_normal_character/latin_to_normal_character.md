# latin_to_normal_character

**Tag**: library

## 简介

This will replace the Latin character inside a string to correspond to normal character example: à to a.

    Usage: 
    LatinToNormalCharacter.transform('ThÏs ís Â strìng wÌth Lãtîn úñîcÔdë.')
    and will return a string value of "ThIs is A string wIth Latin unicOde.

    List of supported latin characters:
    A: ['À', 'Á', 'Â', 'Ã', 'Ä', 'Å']
    a: ['à', 'á', 'â', 'ã', 'ä', 'å']
    B: ['Ɓ', 'Ƃ', 'Ƅ', 'ʙ']
    b: ['ƀ', 'ƃ', 'ƅ']
    C: ['Ç', 'Č', 'Ɔ', 'Ƈ']
    c: ['ç', 'č', 'ƈ']
    D: ['Ð', 'Ƌ', 'Ɗ']
    d: ['ð', 'ƌ', 'ƍ']
    E: ['È', 'É', 'Ê', 'Ë', 'Ĕ', 'Ǝ', 'Ɛ']
    e: ['è', 'é', 'ê', 'ë', 'ĕ', 'Ə', 'ʚ']
    F: ['Ƒ']
    f: ['ƒ']
    G: ['Ğ', 'Ģ', 'Ĝ', 'Ġ', 'Ɠ', 'ʛ']
    g: ['ğ', 'ģ', 'ĝ', 'ġ']
    H: ['Ĥ', 'Ħ', 'ʜ']
    h: ['ĥ', 'ħ', 'ʰ', 'ʯ', 'ʮ']
    I: ['Ì', 'Í', 'Î', 'Ï', 'Ĩ', 'Ī', 'Ĭ', 'Į', 'İ', 'Ɨ']
    i: ['ì', 'í', 'î', 'ï', 'ĩ', 'ī', 'ĭ', 'į', 'ı']
    J: ['Ĵ']
    j: ['ĵ', 'ʝ']
    K: ['Ķ', 'Ƙ']
    k: ['ķ', 'ĸ', 'ƙ', 'ʞ']
    L: ['Ĺ', 'Ļ', 'Ľ', 'Ŀ', 'Ł', 'ʟ']
    l: ['ĺ', 'ļ', 'ľ', 'ŀ', 'ł', 'ƚ']
    M: ['Ɯ']
    m: ['ɯ', 'ɰ', 'ɱ']
    N: ['Ñ', 'Ń', 'Ņ', 'Ň', 'Ŋ', 'Ɲ']
    n: ['ñ', 'ń', 'ņ', 'ň', 'ŋ', 'ŉ', 'ɲ', 'ɳ', 'ƞ', 'ɴ']
    O: ['Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ø', 'Ō', 'Ŏ', 'Ő', 'Ɵ', 'Ơ']
    o: ['ò', 'ó', 'ô', 'õ', 'ö', 'ø', 'ō', 'ŏ', 'ő', 'ơ', 'ɵ']
    P: ['Ƥ']
    p: ['ƥ']
    q: ['ʠ']
    R: ['Ŕ', 'Ŗ', 'Ř']
    r: ['ŕ', 'ŗ', 'ř', 'ɹ', 'ɺ', 'ɻ', 'ɼ', 'ɽ', 'ɾ', 'ɿ', 'ʀ', 'ʁ']
    S: ['Ŝ', 'Ş', 'Š', 'Ś']
    s: ['ŝ', 'ş', 'š', 'ś', 'ſ', 'ʂ']
    T: ['Ţ', 'Ť', 'Ŧ', 'Ƭ', 'Ʈ']
    t: ['ţ', 'ť', 'ŧ', 'ƭ', 'ƫ', 'ʇ', 'ʈ']
    U: ['Ù', 'Ú', 'Û', 'Ü', 'Ū', 'Ũ', 'Ŭ', 'Ů', 'Ű', 'Ų', 'Ư']
    u: ['ù', 'ú', 'û', 'ü', 'ū', 'ũ', 'ŭ', 'ů', 'ű', 'ų', 'ư', 'ʉ']
    V: ['Ʋ']
    v: ['ʋ', 'ʌ']
    W: ['Ŵ']
    w: ['ŵ', 'ʍ']
    Y: ['Ý', 'Ÿ', 'Ŷ', 'Ƴ']
    y: ['ý', 'ŷ', 'ƴ', 'ʎ', 'ʏ']
    Z: ['Ž', 'Ź', 'Ż', 'Ƶ']
    z: ['ž', 'ź', 'ż', 'ƶ', 'ʐ', 'ʑ']
    AE: ['Æ']
    ae: ['æ']
    IJ: ['Ĳ']
    ij: ['ĳ']
    OE: ['Œ']
    oe: ['œ', 'ɶ']
    th: ['Þ']
    SS: ['ß']
    YR: ['Ʀ']
    ESH: ['Ʃ']
    esh: ['ƪ']
    EZH: ['Ʒ', 'Ƹ']
    ezh: ['ƹ', 'ƺ']
    dz: ['ƻ']
    Q: ['Ƽ']
    q: ['ƽ']
    ts: ['ƾ']
    Wynn: ['ƿ']



    Updates:
      0.0.4 & 0.0.5
    - update the coverage of latin string support.
      0.0.6
    - fix issue on non string value.
    0.0.7
    - fix issue on non string value.

## 官网

- 源码仓库: https://github.com/mgc-robot/latin-to-normal-character
- RubyGems: https://rubygems.org/gems/latin_to_normal_character

## 历史版本号

- 0.0.7 (2020-03-24)
- 0.0.6 (2020-03-24)
- 0.0.5 (2020-03-20)
- 0.0.4 (2020-03-19)
- 0.0.3 (2020-03-19)
- 0.0.2 (2020-03-19)
- 0.0.1 (2020-03-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/latin_to_normal_character
- gem 安装: `gem install latin_to_normal_character`
- Bundler: `gem "latin_to_normal_character"`
- 最新版本: 0.0.7
- 最新版归档: https://rubygems.org/downloads/latin_to_normal_character-0.0.7.gem
- 版本锁定: `gem "latin_to_normal_character", "~> 0.0.7"`
- 中央仓库: https://rubygems.org/
