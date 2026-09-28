# crowdfund_alec

**Tag**: web, cli, testing, data

## 简介

# Crowdfund (Alec)

Ferramenta de linha de comando e biblioteca Ruby para simular um programa de **arrecadação de fundos** com rodadas, promessas (pledges) e diferentes tipos de projetos (básico, com *matching*, e *grant*).

## Instalação

```bash
gem install crowdfund_alec
```

Ou rode a partir do código-fonte:

```bash
ruby bin/crowdfund
```

## Como funciona

- Você carrega projetos via CSV (nome, fundos_iniciais, meta).
- Em cada rodada, um dado é rolado para **adicionar** (+25) ou **remover** (–15) fundos do projeto.
- Em paralelo, o projeto recebe **pledges** aleatórios: bronze ($50), silver ($75), gold ($100).
- Projetos podem ter comportamento especial:
  - **MatchingProject**: quando chega a 50% da meta, cada `add_fund` passa a dobrar (+50).
  - **GrantProject**: nunca perde fundos em `remove_fund`.
- Ao sair, o relatório salva os **subfinanciados** em `needmoremoney.txt` e imprime estatísticas.

## Uso (CLI)

```bash
# (1) CSV padrão (bin/projects.csv)
ruby bin/crowdfund

# (2) Informando um CSV customizado
ruby bin/crowdfund caminho/para/projetos.csv
```

Durante a execução:
- Digite um número para a quantidade de rodadas.
- Digite `q` ou `e` para sair e ver o relatório final.

### Formato do CSV

```
NomeDoProjeto,fundos_iniciais,meta
BuyaBoat,5,10000
TraveltoVictoriaIsland,5,3000
GetaPuppy,5,300
```

## Saída esperada

- Resumo por rodada dos fundos e pledges recebidos.
- Arquivo `needmoremoney.txt` contendo:
  - Título do relatório.
  - Projetos totalmente financiados.
  - Projetos subfinanciados ordenados por **quanto falta**.
  - Snapshot CSV de todos os projetos.

## API (uso como biblioteca)

Requerendo as classes principais:

```ruby
require 'crowdfund/project'
require 'crowdfund/fund_request'
```

Criando projetos e executando rodadas:

```ruby
project = Project.new("My App", 500, 2000)
funding = FundRequest.new("Startup do Alec")
funding.add_project(project)
funding.request_funding(5)
funding.print_results
```

### Classes principais

- `Project`
  - Atributos: `name`, `fund_amount`, `target_fund_amount`
  - Métodos: `add_fund`, `remove_fund`, `funds_needed`, `funded?`, `received_pledge`, `pledges`, `total_funds`, `each_received_pledge`, `to_csv`, `status`
- `FundRequest`
  - Gerencia lista de projetos, executa rodadas, imprime e salva relatórios.
- `MatchingProject < Project`
  - Dobra `add_fund` quando `halfway_funded?` (>= 50% da meta).
- `GrantProject < Project`
  - Sobrescreve `remove_fund` para nunca diminuir fundos.
- `Pledgesmod`
  - Constante `PLEDGES` e `.random` para escolher bronze/silver/gold.
- `FundingRound`
  - Regras de uma rodada: rola `Die`, aplica `add/remove`, atribui pledge.
- `Fundable` (mixin)
  - Implementa `add_fund`, `remove_fund`, `funds_needed`, `funded?`.
- `Die`
  - D6 simples com `roll`.

## Testes

Rodar todos os testes:

```bash
rspec
```

Principais cenários cobertos:
- Regras de `add_fund`/`remove_fund`.
- Comportamento de `MatchingProject` e `GrantProject`.
- Integração de `FundingRound` e `Pledgesmod`.
- Geração do relatório em `FundRequest`.

## Licença

MIT — consulte o arquivo `LICENSE`.

## 官网

- 文档: https://www.rubydoc.info/gems/crowdfund_alec/1.0.1
- RubyGems: https://rubygems.org/gems/crowdfund_alec

## 历史版本号

- 1.0.1 (2025-11-10)
- 1.0.0 (2025-11-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/crowdfund_alec
- gem 安装: `gem install crowdfund_alec`
- Bundler: `gem "crowdfund_alec"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/crowdfund_alec-1.0.1.gem
- 版本锁定: `gem "crowdfund_alec", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
