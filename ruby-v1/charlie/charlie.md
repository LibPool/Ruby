# charlie

**Tag**: web, cli, testing, networking, template

## 简介

== DESCRIPTION: Charlie is a library for genetic algorithms (GA) and genetic programming (GP).  == FEATURES: - Quickly develop GAs by combining several parts (genotype, selection, crossover, mutation) provided by the library. - Sensible defaults are provided with any genotype, so often you only need to define a fitness function. - Easily replace any of the parts by your own code. - Test different strategies in GA, and generate reports comparing them.  Example report: http://charlie.rubyforge.org/example_report.html  == INSTALL: * sudo gem install charlie  == EXAMPLES: This example solves a TSP problem (also quiz #142): N=5 CITIES = (0...N).map{|i| (0...N).map{|j| [i,j] } }.inject{|a,b|a+b} class TSP &lt; PermutationGenotype(CITIES.size) def fitness d=0 (genes + [genes[0]]).each_cons(2){|a,b|  a,b=CITIES[a],CITIES[b] d += Math.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 )  } -d # lower distance -&gt; higher fitness. end use EdgeRecombinationCrossover, InversionMutator end Population.new(TSP,20).evolve_on_console(50)  This example finds a polynomial which approximates cos(x) class Cos &lt; TreeGenotype([proc{3*rand-1.5},:x], [:-@], [:+,:*,:-]) def fitness -[0,0.33,0.66,1].map{|x| (eval_genes(:x=&gt;x) - Math.cos(x)).abs }.max end use TournamentSelection(4) end Population.new(Cos).evolve_on_console(500)

## 官网

- 主页: http://charlie.rubyforge.org
- RubyGems: https://rubygems.org/gems/charlie

## 历史版本号

- 0.7.1 (2009-07-25)
- 0.7.0 (2009-07-25)
- 0.6.0 (2009-07-25)
- 0.5.0 (2009-07-25)
- 0.8.1 (2009-07-25)
- 0.8.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/charlie
- gem 安装: `gem install charlie`
- Bundler: `gem "charlie"`
- 最新版本: 0.8.1
- 最新版归档: https://rubygems.org/downloads/charlie-0.8.1.gem
- 版本锁定: `gem "charlie", "~> 0.8.1"`
- 中央仓库: https://rubygems.org/
