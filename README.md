Meteor Evasion
Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório contém o jogo desenvolvido como avaliação final, aplicando conceitos de lógica de programação, estruturas de dados, manipulação de arquivos e modularização.

Integrantes do grupo
João Victor Santos

Thales

Estrutura do projeto
main.py: ponto de entrada da aplicação.

src/: código-fonte principal do jogo (loop, regras, físicas e dados).

assets/: imagens (imagens/) e sons (sons/) utilizados no jogo.

data/ ou raiz: arquivos persistentes (como o recorde.txt).

tests/: testes unitários de validação da lógica e arquivos.

docs/: documentação do projeto, incluindo a proposta inicial.

Descrição do jogo
Meteor Evasion é um jogo arcade 2D de sobrevivência espacial. O jogador controla uma nave que se movimenta na parte inferior da tela e deve desviar de uma chuva constante de meteoros que caem do espaço. À medida que o jogador sobrevive e acumula pontos, a velocidade de queda dos meteoros aumenta, tornando o jogo progressivamente mais difícil. O jogo também conta com um sistema de pontuação máxima (High Score) salva em arquivo.

Objetivo do jogador
O objetivo é sobreviver o maior tempo possível, esquivando-se dos meteoros para acumular pontos e tentar quebrar o recorde histórico salvo no jogo.

Regras do jogo
O jogador inicia a partida com 3 vidas.

A cada meteoro que sai da tela com sucesso (sem bater na nave), o jogador ganha 1 ponto.

A cada 10 pontos acumulados, a velocidade dos meteoros aumenta (aumento de dificuldade).

Colidir com um meteoro reduz a quantidade de vidas em 1.

A partida termina (Game Over) quando o jogador perde todas as vidas.

Se a pontuação final for maior que o recorde atual, o novo recorde é salvo automaticamente.

Controles
Seta para a Esquerda ou Tecla A: Mover a nave para a esquerda.

Seta para a Direita ou Tecla D: Mover a nave para a direita.

Tecla R: Reiniciar a partida (ativo apenas na tela de Game Over).

ESC ou Botão Fechar: Sair do jogo.

Como executar o projeto
1. Clonar o repositório e rodar
Abra o terminal e execute os seguintes comandos:

Bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
Como executar os testes
Para validar a integridade da lógica de gravação e leitura de recordes, execute:

Bash
python -m pytest
# ou, se o seu arquivo se chamar test_logica.py:
python test_logica.py