# Proposta Inicial do Jogo



A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Meteor-Evasion



Exemplo:

> Corrida dos Obstáculos

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: João Victor Santos
- Nome 2: Thales
- Nome 3:
- Nome 4:

## 3. Tipo de jogo

Jogo de desviar de obstáculos (Estilo Arcade / Sobrevivência Espacial).

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

> Jogo de desviar de obstaculos

## 4. Descrição geral do jogo

Descrição:

*Meteor Evasion** é um jogo digital 2D focado em agilidade e sobrevivência. O jogador assume o controle de uma nave espacial localizada na parte inferior da tela e deve se movimentar horizontalmente para desviar de uma chuva de meteoros que caem continuamente do topo do cenário. À medida que o tempo passa, a velocidade de queda dos meteoros aumenta e a frequência de surgimento se intensifica, exigindo reflexos cada vez mais rápidos do jogador.

## 5. Objetivo do jogador


Objetivo:

O objetivo principal é sobreviver o maior tempo possível, esquivando-se dos meteoros para acumular a maior pontuação possível e registrar um novo recorde (*High Score*) no ranking do jogo.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1:
- Regra 2:
- Regra 3:
- Regra 4:
- Regra 5:

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:
Por se tratar de um jogo no estilo *endless* (infinito), não há uma condição de vitória definitiva ou um "fim do jogo por zerar". A vitória pessoal do jogador consiste em superar o recorde de pontuação previamente salvo no sistema.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:
A partida é encerrada imediatamente (tela de *Game Over*) quando o contador de vidas do jogador chega a zero (0).

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

Uma nave espacial com movimentação lateral restrita às bordas da tela.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

** Elementos que surgem em posições X aleatórias no topo da tela e se movem verticalmente para baixo.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

 Exibição em tempo real da pontuação atual, número de vidas restantes através de ícones ou texto, e o Recorde Atual (*High Score*).

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

 Exibição em tempo real da pontuação atual, número de vidas restantes através de ícones ou texto, e o Recorde Atual (*High Score*).

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando:**Mover para a Esquerda:** Tecla de Seta para a Esquerda (`LEFT ARROW`) ou Tecla `A`.
- Tecla/comando:**Mover para a Direita:** Tecla de Seta para a Direita (`RIGHT ARROW`) ou Tecla `D`.
- Tecla/comando:**Reiniciar o Jogo:** Tecla `R` (ativa apenas na tela de *Game Over*).
- Tecla/comando:**Sair do Jogo:** Tecla `ESC` ou clicando no botão fechar da janela.

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

### 11. Organização Inicial do Código
Para garantir a modularização e a clareza do projeto, o código será estruturado da seguinte forma:

* `main.py`: Arquivo central responsável por inicializar o Pygame, carregar as configurações iniciais e disparar a execução do jogo.
* `src/game.py`: Contém a classe ou função principal do loop do jogo (`game_loop`), gerenciando os estados (Menu, Jogando, Game Over) e a taxa de quadros (FPS).
* `src/config.py`: Centraliza todas as constantes do projeto, como as dimensões da janela (800x600), a paleta de cores (RGB), caminhos de arquivos e taxas de velocidade padrão.
* `src/elements.py`: Contém a lógica de atualização e renderização dos elementos visuais do jogo, como a movimentação da Nave e o surgimento/queda dos Meteoros.
* `src/mechanics.py`: Concentra as funções puramente lógicas do jogo, como o cálculo de colisão entre retângulos (`pygame.Rect`), controle do sistema de vidas e progressão de dificuldade a cada 10 segundos.
* `src/data.py`: Responsável exclusivamente pelas funções de persistência de dados, englobando a leitura e a escrita do recorde (*High Score*) no arquivo local.

## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

**Listas (List):** Utilizada para gerenciar dinamicamente todos os meteoros ativos na tela (adicionando novos objetos gerados e removendo os meteoros que ultrapassam o limite inferior do cenário para otimizar a memória).
* **Dicionários (Dict):** Utilizado para encapsular e organizar o estado do jogo e do jogador (ex: `status_jogador = {'vidas': 3, 'pontos': 0, 'velocidade': 5}`).
* **Tuplas (Tuple):** Utilizadas para valores imutáveis de configuração, como as dimensões da janela do jogo (ex: `RESOLUCAO = (800, 600)`) e cores em formato RGB.


> Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:


Dificuldade 1:esafiador, mas que não se torne impossível logo no início.
Dificuldade 2: ** Garantir a correta exclusão de objetos da lista de meteoros assim que eles saem da tela, evitando vazamentos de memória (*memory leaks*).
Dificuldade 3: **Configurar os testes unitários (`unittest` ou `pytest`) de forma isolada da biblioteca Pygame para validar estritamente a lógica matemática e de estados.
## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

O escopo mínimo  consiste em: uma janela Pygame funcional, movimentação fluida da nave, geração procedural e queda de meteoros, sistema de colisão preciso (usando `pygame.Rect`), controle de vidas e pontos na tela, tela de Game Over funcional com opção de reinício e salvamento estável do *High Score* em um arquivo local.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1:Sistema de Itens Coletáveis (Power-ups)**
  Fazer com que, além dos meteoros, caiam esporadicamente do topo da tela itens benéficos, como um "Coração" (para recuperar 1 vida perdida) ou um "Escudo Temporário" (que torna a nave invulnerável por 5 segundos). Isso enriquece a mecânica, exigindo que o jogador decida entre desviar ou arriscar para pegar o item.
- Melhoria 2:Sons e Efeitos Sonoros (Áudio)**
  Utilizar o módulo `pygame.mixer` para adicionar uma música de fundo em loop com temática espacial e efeitos sonoros simples de 8-bits: um som de "explosão" quando a nave for atingida, um som de "bip" ao marcar pontos e um som de "Game Over" ao final da partida.
- Melhoria 3:Implementar a funcionalidade de pausar o jogo ao pressionar a tecla `P` ou `SPACE`, congelando a descida dos meteoros e abrindo uma pequena sobreposição na tela. Adicionalmente, caso haja tempo para a parte visual, substituir os retângulos coloridos por sprites em formato de imagem (PNG) para a nave e os meteoros.
