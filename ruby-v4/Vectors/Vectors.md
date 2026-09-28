# Vectors

**Tag**: library

## 简介

A Ruby gem for vector and matrix operations. Provides methods to calculate:
  - Matrix determinant:

   Determinant(matrix)

   input: matrix - Array of arrays size of nxn
   output: res[Int] - simple Integer

  - Scalar product of vectors

  scalar_prod(a, b)

  input: a[Array], b[Array]- vectors a and b
  output: res[Int] - simple Integer as a result of scalar prod

  - Cross product for 3D vectors

    cross_prod(a, b)

    input: a[Array], b[Array] - vectors a and b with dimension n = 3;
    output: res[Array] - vector with the size = 3 (its dimension) as a result of cross prod

  - Help function

    help()

    output: String with info about gem funcs
  
  Includes comprehensive error handling and input validation. Designed for educational use and basic linear algebra computations.

  Ruby-гем для операций с векторами и матрицами. Предоставляет методы для вычисления:
  - Определителя матрицы

    Determinant(matrix)

    input: matrix - матрица (массив массивов) размера nxn
    output: res[Int] - целое число

  - Скалярного произведения векторов

    scalar_prod(a, b)

    input: a[Array], b[Array] - векторы (массивы) a и b
    output: res[Int] - целое число как результат скалярного произведения

  - Векторного произведения для 3D векторов

    cross_prod(a, b)

    input: a[Array], b[Array] - векторы (массивы) a и b размером n = 3;
    output: res[Array] - вектор (массив) с размером = 3 (его размерность) как результат векторного произведения векторов

  - Функция "помощь"

    help()

    output: Строка с информацией про математические методы гема

  Включает обработку ошибок и валидацию входных данных. Разработан для образовательных целей и базовых вычислений линейной алгебры.

## 官网

- 文档: https://www.rubydoc.info/gems/Vectors/0.2.0
- RubyGems: https://rubygems.org/gems/Vectors

## 历史版本号

- 0.2.0 (2025-05-17)
- 0.1.0 (2025-04-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/Vectors
- gem 安装: `gem install Vectors`
- Bundler: `gem "Vectors"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/Vectors-0.2.0.gem
- 版本锁定: `gem "Vectors", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
