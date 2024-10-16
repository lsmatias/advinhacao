# Jogo de Adivinhação de Números
Bem-vindo ao Jogo de Adivinhação de Números, um jogo interativo em que o jogador tenta adivinhar um número secreto escolhido aleatoriamente pela máquina. A cada tentativa, o jogador recebe uma dica indicando se o número escolhido é maior ou menor do que o palpite. É um jogo divertido e desafiador para testar sua habilidade de adivinhar!

## Índice
* [Visão Geral](https://github.com/lsmatias/advinhacao/blob/main/README.md#visão-geral) 
* [Funcionalidades](https://github.com/lsmatias/advinhacao/blob/main/README.md#funcionalidades)
* [Pré-requisitos](https://github.com/lsmatias/advinhacao/blob/main/README.md#pré-requisitos)
* [Como Jogar](https://github.com/lsmatias/advinhacao/blob/main/README.md#como-jogar)
* [Instalação](https://github.com/lsmatias/advinhacao/blob/main/README.md#instalação)
* [Regras do Jogo](https://github.com/lsmatias/advinhacao/blob/main/README.md#regras-do-jogo)
* [Exemplo de Uso](https://github.com/lsmatias/advinhacao/blob/main/README.md#exemplo-de-uso)
* [Melhorias Futuras](https://github.com/lsmatias/advinhacao/blob/main/README.md#melhoriasfuturas)
* [Contribuição](https://github.com/lsmatias/advinhacao/blob/main/README.md#contribuição)

## Visão Geral
O Jogo de Adivinhação de Números é uma aplicação simples em Python, onde o usuário tenta adivinhar um número aleatório escolhido pela máquina dentro de um intervalo predefinido. O objetivo é adivinhar o número antes que todas as chances se esgotem.

# Funcionalidades
Dicas para ajudar o jogador, indicando se o número é maior ou menor do que o palpite.
Sistema de contagem de tentativas, mostrando quantas chances restam.
Níveis de dificuldade: fácil, médio e difícil.
Mensagens motivacionais que incentivam o jogador durante o jogo.
Opção para reiniciar o jogo após o término.

# Pré-requisitos
Para executar o jogo, você precisará do Python instalado no seu sistema. Recomenda-se a versão 3.6 ou superior.

## Como Jogar

Clone este repositório ou baixe o código fonte.
Execute o arquivo advinhacao.py em seu ambiente de desenvolvimento.
Escolha o nível de dificuldade.
Tente adivinhar o número com base nas dicas fornecidas após cada tentativa.
Você tem um número limitado de chances para acertar. Boa sorte!

Clone este repositório ou baixe o código fonte.
Execute o arquivo jogo_adivinha.py em seu ambiente de desenvolvimento.
Escolha o nível de dificuldade.
Tente adivinhar o número com base nas dicas fornecidas após cada tentativa.
Você tem um número limitado de chances para acertar. Boa sorte!

# Instalação
Siga estas instruções para instalar e configurar o jogo no seu ambiente local:

1- Clone o repositório:
```
git clone https://github.com/seu-usuario/jogo-adivinhacao.git
```
2-Navegue até o diretório do projeto:
```
cd jogo-adivinhacao
```

3- Execute o jogo:
```
python advinhacao.py
```

# Regras do Jogo
O jogo escolhe aleatoriamente um número dentro de um intervalo específico, dependendo do nível de dificuldade.
Você precisa adivinhar o número em um número limitado de tentativas:
Fácil: Intervalo de 0 a 50, com 15 chances.
Médio: Intervalo de 0 a 100, com 10 chances.
Difícil: Intervalo de 0 a 200, com 5 chances.
A cada palpite, o jogo informa se o número secreto é maior ou menor que o chute.
Se todas as chances se esgotarem antes do acerto, o jogo termina e o número secreto é revelado.

# Exemplo de Uso

```
#### Iniciando Jogo ####
Escolha o nível de dificuldade (fácil, médio, difícil): médio
Chute um número entre 0 e 100: 45

Você errou!!! Dica: É um número maior.
Você ainda possui 9 chances.

Chute um número entre 0 e 100: 60

Você errou!!! Dica: É um número menor.
Você ainda possui 8 chances.

Parabéns, você venceu! O número era 58 e você ainda tinha 7 chances.
#### Fim do Jogo ####
```

# Melhorias Futuras

Aqui estão algumas sugestões para melhorias:
Modo Multiplayer: Permitir que dois ou mais jogadores joguem alternadamente, competindo para ver quem acerta primeiro.
Pontuação: Implementar um sistema de pontuação baseado no número de tentativas restantes.
Interface Gráfica: Criar uma versão com interface gráfica utilizando bibliotecas como tkinter ou pygame.
Estatísticas: Mostrar o histórico de vitórias e derrotas do jogador.

# Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um "issue" ou enviar um "pull request" para melhorar este projeto.
