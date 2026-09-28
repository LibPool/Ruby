# studio_game_alec

**Tag**: cli, testing, tooling, filesystem, data

## 简介

# StudioGame (Alec)

Jogo de terminal em Ruby com **jogadores, dados, tesouros e variações de jogadores** (Clumsy e Berserk), empacotado como gem.

> Nome do gem (exemplo): `studio_game_alec`

---

## 🚀 Instalação e execução

### Rodando direto do código-fonte
No diretório do projeto:

```bash
ruby bin/studio_game
```

Se você não passar um arquivo de jogadores via CLI, o script usa o `players.csv` que fica em `bin/` por padrão.

Também funciona passando um CSV na linha de comando:

```bash
ruby bin/studio_game my_favorite_players.csv
```

### Como gem (local)
Empacote e instale localmente:

```bash
gem build studio_game.gemspec
gem install studio_game_alec-<versao>.gem
```

Depois rode:

```bash
studio_game
```

> No Windows, o executável será resolvido pelo RubyGems. Se preferir, rode: `ruby bin/studio_game`.

---

## 📁 Estrutura do projeto

```
games/
├─ bin/
│  ├─ studio_game          # script principal (tem shebang)
│  └─ players.csv          # CSV padrão (nome,vida)
├─ lib/
│  └─ studio_game/
│     ├─ auditable.rb
│     ├─ berserk_player.rb
│     ├─ clumsy_player.rb
│     ├─ die.rb
│     ├─ game.rb
│     ├─ game_turn.rb
│     ├─ loaded_die.rb
│     ├─ playable.rb
│     ├─ player.rb
│     └─ treasure_trove.rb
├─ spec/
│  └─ studio_game/         # specs RSpec
├─ LICENSE
├─ README.md
└─ studio_game.gemspec
```

- **Namespace:** todo o código vive dentro do módulo `StudioGame` para evitar colisões.
- **bin/studio_game:** script CLI com shebang (`#!/usr/bin/env ruby`). Faz _fallback_ do `$LOAD_PATH` para `lib` quando usado fora da gem.
- **lib/studio_game/**: código da biblioteca (classes/módulos).
- **spec/**: testes RSpec.

---

## 🧩 Conceitos principais

- **Player** (`player.rb`): representa um jogador com `name`, `health`, coleta tesouros e calcula `score` (= `health` + `points`). Inclui o mixin **Playable**.
- **Playable** (`playable.rb`): mixin com `w00t`, `blam` e `strong?` (altera/consulta `health` via getters/setters).
- **TreasureTrove** (`treasure_trove.rb`): define `Treasure = Struct.new(:name,:points)` e a constante `TREASURES`; possui `.random`.
- **Die/LoadedDie** (`die.rb`, `loaded_die.rb`): rolam valores (o carregado favorece 1,1,2,5,6,6). Ambos incluem **Auditable**.
- **Auditable** (`auditable.rb`): imprime “Rolled a X (DieClass)” após cada rolagem.
- **Game** (`game.rb`): agrega jogadores, carrega CSV, executa rodadas, soma pontos e salva _high scores_.
- **GameTurn** (`game_turn.rb`): executa a lógica de um turno para um jogador (rola dado, aplica `blam/w00t/skip` e concede tesouro).
- **ClumsyPlayer / BerserkPlayer**: variações de `Player` que modificam comportamento de `w00t` e de coleta de tesouros.

---

## 🧪 Testes

Rode todos os testes:

```bash
rspec
```

Principais coisas testadas:
- Ordenação de jogadores por `score` (usa `<=>` em `Player`).
- Cálculo de `points` e `score` (soma de tesouros + vida).
- Efeitos de `w00t`/`blam` e força (`strong?`).
- Lógica de turno com _stubs_ de dado (`allow_any_instance_of(LoadedDie).to receive(:roll).and_return(n)`).
- Comportamentos de `ClumsyPlayer` e `BerserkPlayer`.

---

## 📦 CSVs e caminhos

- `bin/studio_game` resolve o CSV padrão assim:

```ruby
default_player_file = File.join(File.dirname(__FILE__), 'players.csv')
game.load_players(ARGV.shift || default_player_file)
```

- Você pode passar um arquivo `.csv` via CLI como primeiro argumento.

Formato do CSV:
```
Moe,100
Larry,60
Curly,125
```

---

## 🧾 High Scores

Após sair do loop, o jogo grava `high_score.txt` com as entradas ordenadas. Cada linha é formatada por `Game#high_score_entry`:

```
<nome com padding de pontos> <score>
```

---

## 🛠️ Dicas de desenvolvimento

- Use `require 'studio_game/arquivo'` quando a gem estiver instalada.
- No script binário, o `begin/rescue LoadError` faz _fallback_ para `$LOAD_PATH` local, útil fora da gem.
- Para debugar I/O em testes, o spec redireciona `STDOUT` (`$stdout = StringIO.new`).

---

## 📚 Licença

MIT – veja o arquivo `LICENSE`.

## 官网

- 文档: https://www.rubydoc.info/gems/studio_game_alec/1.0.1
- RubyGems: https://rubygems.org/gems/studio_game_alec

## 历史版本号

- 1.0.1 (2025-11-10)
- 1.0.0 (2025-11-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/studio_game_alec
- gem 安装: `gem install studio_game_alec`
- Bundler: `gem "studio_game_alec"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/studio_game_alec-1.0.1.gem
- 版本锁定: `gem "studio_game_alec", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
