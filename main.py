import pygame
import sys
import random
from src.config import * # Importa tudo que criamos no config.py

# --- FUNÇÕES DO JOGO ---

def mover_jogador(teclas, retangulo_jogador):
    """Atualiza a posição do jogador com base nas setas do teclado."""
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        retangulo_jogador.x -= VELOCIDADE_NAVE
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        retangulo_jogador.x += VELOCIDADE_NAVE
        
    # Impedir que a nave saia da tela
    if retangulo_jogador.left < 0:
        retangulo_jogador.left = 0
    if retangulo_jogador.right > LARGURA_TELA:
        retangulo_jogador.right = LARGURA_TELA

def atualizar_meteoro(retangulo_meteoro):
    """Faz o meteoro cair e reaparecer no topo quando sai da tela."""
    retangulo_meteoro.y += VELOCIDADE_METEORO
    
    # Se o meteoro sair por baixo da tela, volta pro topo em posição aleatória
    if retangulo_meteoro.top > ALTURA_TELA:
        retangulo_meteoro.y = -TAMANHO_METEORO
        retangulo_meteoro.x = random.randint(0, LARGURA_TELA - TAMANHO_METEORO)

# --- FUNÇÃO PRINCIPAL ---

def main():
    # 1. Inicializa o Pygame
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Meteor Evasion - Protótipo")
    relogio = pygame.time.Clock()

    # 2. Criação dos Elementos (Retângulos)
    # A nave começa no meio da tela, na parte de baixo
    jogador_rect = pygame.Rect(LARGURA_TELA // 2, ALTURA_TELA - 50, LARGURA_NAVE, ALTURA_NAVE)
    
    # O meteoro começa no topo, em uma posição aleatória
    meteoro_rect = pygame.Rect(random.randint(0, LARGURA_TELA - TAMANHO_METEORO), -50, TAMANHO_METEORO, TAMANHO_METEORO)

    # 3. Loop Principal do Jogo
    rodando = True
    while rodando:
        # A. Tratamento de Eventos (Ex: fechar a janela)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # B. Lógica do Jogo e Movimentação
        teclas_pressionadas = pygame.key.get_pressed()
        mover_jogador(teclas_pressionadas, jogador_rect)
        atualizar_meteoro(meteoro_rect)

        # C. Renderização (Desenhar na tela)
        tela.fill(PRETO) # Limpa a tela com fundo preto a cada frame
        
        # Desenha a Nave (Azul) e o Meteoro (Vermelho)
        pygame.draw.rect(tela, AZUL, jogador_rect)
        pygame.draw.rect(tela, VERMELHO, meteoro_rect)

        # D. Atualiza a tela e controla o FPS
        pygame.display.flip()
        relogio.tick(FPS)

    # Encerra o Pygame corretamente ao sair do loop
    pygame.quit()
    sys.exit()

# Executa o jogo
if __name__ == "__main__":
    main()

