# Python Game Template

Este repositório apresenta uma estrutura simples e organizada para projetos de jogos desenvolvidos em Python.

A organização separa os arquivos do projeto por responsabilidade, facilitando a leitura, manutenção e evolução do código. A estrutura também ajuda a evitar que todo o jogo fique concentrado em um único arquivo.

## Estrutura do Projeto

```txt
python-game-template/
│
├── assets/
│   ├── images/
│   │   ├── player.png
│   │   ├── enemy.png
│   │   └── background.png
│   │
│   ├── sounds/
│   │   ├── jump.wav
│   │   └── collision.wav
│   │
│   └── music/
│       └── theme.mp3
│
├── classes/
│   ├── player.py
|   ├── coin.py
|   ├── text.py
│   ├── enemy.py
│   └── game_object.py
│
├── utils/
│   ├── helpers.py
│   └── collision.py
│
├── constants.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Explicação da Estrutura

### `assets/`

A pasta `assets` guarda todos os arquivos externos usados no jogo, como imagens, efeitos sonoros e músicas.

Separar esses arquivos do código deixa o projeto mais limpo e facilita alterações futuras. Por exemplo, é possível trocar uma imagem ou música sem precisar modificar a lógica principal do jogo.

A pasta pode ser dividida em três partes principais:

#### `assets/images/`

Guarda as imagens usadas no jogo.

Exemplos:

```txt
player.png
enemy.png
background.png
button_start.png
```

Essa pasta pode conter imagens de personagens, inimigos, cenários, botões, telas de menu, itens e obstáculos.

#### `assets/sounds/`

Guarda efeitos sonoros curtos.

Exemplos:

```txt
jump.wav
collision.wav
game_over.wav
collect_item.wav
```

Essa pasta pode conter sons de pulo, colisão, dano, vitória, derrota ou coleta de itens.

#### `assets/music/`

Guarda músicas de fundo.

Exemplos:

```txt
theme.mp3
menu_music.mp3
level_music.mp3
```

Essa pasta pode conter músicas para o menu, fases, tela final ou momentos específicos do jogo.

---

### `classes/`

A pasta `classes` guarda os arquivos que representam os principais objetos do jogo.

Cada arquivo deve conter uma classe relacionada ao seu nome. Isso ajuda a separar responsabilidades e evita que diferentes partes do jogo fiquem misturadas no mesmo lugar.

Exemplos:

```txt
player.py
enemy.py
coin.py
text.py
game_object.py
```

Possíveis classes do jogo:

* jogador;
* inimigo;
* personagem;
* item;
* obstáculo;
* projétil;
* objeto genérico do jogo.

Exemplo de classe:

```python
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        pass
```

A classe `Player`, por exemplo, pode concentrar informações e comportamentos relacionados ao jogador, como posição, velocidade, vida, movimentação e desenho na tela.

---

### `utils/`

A pasta `utils` guarda funções auxiliares do projeto.

Essas funções não pertencem diretamente a uma classe principal, mas ajudam em tarefas usadas em diferentes partes do jogo.

Exemplos:

```txt
helpers.py
collision.py
```

Possíveis usos da pasta `utils`:

* verificar colisões;
* carregar imagens;
* carregar sons;
* centralizar textos na tela;
* formatar pontuação;
* calcular distância entre objetos;
* reutilizar funções comuns.

Exemplo:

```python
def check_collision(object_a, object_b):
    return object_a.rect.colliderect(object_b.rect)
```

Separar funções auxiliares evita repetição de código e deixa os arquivos principais mais simples.

---

### `constants.py`

O arquivo `constants.py` guarda valores fixos usados em diferentes partes do projeto.

Exemplos:

```python
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

WINDOW_TITLE = "My Game"

IMAGES_PATH = "assets/images"
SOUNDS_PATH = "assets/sounds"
MUSIC_PATH = "assets/music"
```

Esse arquivo evita que números, textos e caminhos fiquem espalhados pelo código.

Por exemplo, em vez de repetir `800`, `600` ou `"assets/images"` em vários arquivos, esses valores ficam centralizados em um único lugar.

Isso facilita alterações futuras. Caso o tamanho da tela precise mudar, basta alterar em `constants.py`.

---

### `main.py`

O arquivo `main.py` é o ponto de entrada do projeto.

É por ele que o jogo começa a ser executado.

Normalmente, esse arquivo contém:

* inicialização do jogo;
* criação da janela;
* configuração inicial;
* loop principal;
* leitura de eventos;
* atualização dos objetos;
* desenho dos elementos na tela;
* encerramento do jogo.

Exemplo simples:

```python
def main():
    print("Game started!")


if __name__ == "__main__":
    main()
```

O `main.py` deve organizar o funcionamento geral do jogo, mas não deve concentrar toda a lógica do projeto.

Quando o código cresce, classes, funções auxiliares e constantes devem ser separadas em seus respectivos arquivos.

---

### `requirements.txt`

O arquivo `requirements.txt` lista as bibliotecas necessárias para executar o projeto.

Exemplo:

```txt
pygame
```

Para instalar as dependências, use:

```bash
pip install -r requirements.txt
```

Esse arquivo facilita a configuração do projeto em outro computador, pois todas as bibliotecas necessárias ficam registradas em um único lugar.

---

### `.gitignore`

O arquivo `.gitignore` informa ao Git quais arquivos e pastas não devem ser enviados para o repositório.

Exemplo:

```txt
__pycache__/
*.pyc
.venv/
.env
```

Isso evita enviar arquivos automáticos do Python, ambientes virtuais e configurações locais.

Arquivos como `__pycache__`, `.venv` e `.env` geralmente não devem ser versionados.

---

## Como Executar o Projeto

Primeiro, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Depois, execute o arquivo principal:

```bash
python main.py
```

Caso o projeto use uma biblioteca específica, como `pygame`, verifique se ela está listada no arquivo `requirements.txt`.

---

## Padrão de Nomes

Evite misturar padrões de nomeações. Defina um e o siga durante o desenvolvimento do projeto.

Essa prática evita problemas com importações e caminhos de arquivos.

---

## Sugestão de Organização dos Arquivos

### Para personagens

Arquivos relacionados a personagens devem ficar em `classes/`.

Exemplo:

```txt
classes/player.py
classes/enemy.py
```

### Para imagens

Arquivos de imagem devem ficar em `assets/images/`.

Exemplo:

```txt
assets/images/player.png
assets/images/background.png
```

### Para efeitos sonoros

Arquivos de som devem ficar em `assets/sounds/`.

Exemplo:

```txt
assets/sounds/jump.wav
assets/sounds/collision.wav
```

### Para músicas

Arquivos de música devem ficar em `assets/music/`.

Exemplo:

```txt
assets/music/theme.mp3
assets/music/menu_music.mp3
```

### Para funções auxiliares

Funções reutilizáveis devem ficar em `utils/`.

Exemplo:

```txt
utils/helpers.py
utils/collision.py
```

### Para valores fixos

Valores que não mudam durante a execução do jogo devem ficar em `constants.py`.
Isso facilita caso precise modificar esses valores.

Exemplo:

```python
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
```

---

## Boas Práticas

* Mantenha o `main.py` como ponto de entrada do projeto.
* Evite colocar toda a lógica do jogo dentro do `main.py`.
* Separe imagens, sons e músicas dentro da pasta `assets`.
* Use a pasta `classes` para organizar os principais objetos do jogo.
* Use a pasta `utils` para funções auxiliares.
* Use o arquivo `constants.py` para valores fixos.
* Use nomes claros e padronizados.
* Evite arquivos com espaços, acentos ou nomes muito genéricos.
* Atualize o `README.md` sempre que a estrutura do projeto mudar.

---

## Exemplo de `constants.py`

```python
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

WINDOW_TITLE = "My Game"

IMAGES_PATH = "assets/images"
SOUNDS_PATH = "assets/sounds"
MUSIC_PATH = "assets/music"

PLAYER_SPEED = 5
ENEMY_SPEED = 3
```

---

## Exemplo de `main.py`

```python
from constants import WINDOW_TITLE


def main():
    print(f"{WINDOW_TITLE} started!")


if __name__ == "__main__":
    main()
```

---

## Exemplo de Classe

Arquivo: `classes/player.py`

```python
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

---

## Exemplo de Função Auxiliar

Arquivo: `utils/helpers.py`

```python
def clamp(value, minimum, maximum):
    if value < minimum:
        return minimum

    if value > maximum:
        return maximum

    return value
```

A função acima limita um valor dentro de um intervalo mínimo e máximo.

---

## Objetivo da Estrutura

A estrutura do projeto foi definida para manter o código organizado e facilitar sua manutenção.

Separar arquivos por responsabilidade ajuda a:

* localizar partes do projeto com mais facilidade;
* reduzir repetição de código;
* evitar arquivos muito grandes;
* facilitar alterações futuras;
* melhorar a leitura do projeto;
* deixar o código mais próximo de projetos reais.

Mesmo em jogos simples, manter uma boa organização desde o início torna o desenvolvimento mais claro e evita confusão conforme o projeto cresce.

OBS.: Esse arquivo contém apenas sugestões. Você pode e deve modificar conforme as necessidades do seu projeto. Se trata apenas de uma base para vocês entenderem como funciona a estruturação.
