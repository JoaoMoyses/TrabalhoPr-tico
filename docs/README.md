# Documentacao

# 🚀 Meteor Evasion

**Projeto Final da Disciplina de Algoritmos - PUC Minas**

## 📖 Sobre o Jogo
**Meteor Evasion** é um jogo arcade 2D de sobrevivência espacial desenvolvido inteiramente em Python utilizando a biblioteca Pygame. No controle de uma nave espacial, o jogador deve demonstrar reflexos rápidos para desviar de uma chuva constante de meteoros. 

O jogo foi projetado para ser infinito (*endless runner*), focando em acumular a maior pontuação possível. À medida que o jogador sobrevive, o nível de dificuldade aumenta automaticamente, exigindo ainda mais agilidade.

## ✨ Funcionalidades Implementadas
* **Movimentação Fluida:** Controle da nave respeitando os limites da tela.
* **Dificuldade Progressiva:** A velocidade de queda dos meteoros aumenta a cada 10 pontos conquistados.
* **Fundo Estrelado Animado (Parallax):** Geração procedural de estrelas em diferentes velocidades, criando uma sensação de profundidade no espaço.
* **Sistema de Vidas e Pontuação:** O jogador inicia com 3 vidas. Cada meteoro evitado concede 1 ponto.
* **Persistência de Dados (High Score):** O recorde máximo do jogador é salvo automaticamente em um arquivo local (`recorde.txt`) e carregado nas próximas partidas.
* **Sistema de Assets Inteligente (Fallback):** O jogo tenta carregar imagens customizadas (`.png`) da pasta `assets`. Caso não as encontre, adapta-se automaticamente para desenhar formas geométricas, garantindo que o jogo nunca quebre.
* **Menu de Game Over Interativo:** Exibição da pontuação final, recorde histórico e a opção de reiniciar a partida instantaneamente sem fechar a janela.
* **Testes Unitários:** Validação da lógica de leitura e escrita de arquivos independente da interface gráfica.

## 🎮 Controles
* **Seta para a Esquerda / Tecla A:** Move a nave para a esquerda.
* **Seta para a Direita / Tecla D:** Move a nave para a direita.
* **Tecla R:** Reinicia a partida (Apenas na tela de *Game Over*).

## ⚙️ Como Executar o Jogo

1. Certifique-se de ter o **Python 3.x** instalado em sua máquina.
2. Clone este repositório ou baixe os arquivos.
3. Abra o terminal na pasta principal do projeto e instale as dependências:
   ```bash
   pip install -r requirements.txt

## Arquivos

-

## Sugestoes de uso


