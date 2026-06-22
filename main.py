import pygame
import sys
import random
import os
from src.config import *
from src.dados import carregar_recorde, salvar_recorde

def main():
    pygame.init()
    pygame.mixer.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Meteor Evasion - Premium")
    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 36)
    fonte_grande = pygame.font.SysFont(None, 60)

    # --- TRUQUE PROFISSIONAL: CAMINHO ABSOLUTO ---
    # Isso garante que o Python ache a pasta assets não importa de onde você rode o código
    DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
    caminho_imagens = os.path.join(DIRETORIO_ATUAL, "assets", "imagens")
    caminho_sons = os.path.join(DIRETORIO_ATUAL, "assets", "sons")
    
    try:
        img_nave = pygame.image.load(os.path.join(caminho_imagens, "nave.png"))
        img_nave = pygame.transform.scale(img_nave, (LARGURA_NAVE, ALTURA_NAVE))
    except Exception as e:
        print(f"Erro ao carregar nave: {e}")
        img_nave = None

    try:
        img_meteoro = pygame.image.load(os.path.join(caminho_imagens, "meteoro.gif"))
        img_meteoro = pygame.transform.scale(img_meteoro, (TAMANHO_METEORO, TAMANHO_METEORO))
    except Exception as e:
        print(f"Erro ao carregar meteoro: {e}")
        img_meteoro = None

    try:
        img_explosao = pygame.image.load(os.path.join(caminho_imagens, "explosao.png"))
        img_explosao = pygame.transform.scale(img_explosao, (LARGURA_NAVE * 2, ALTURA_NAVE * 2))
    except:
        img_explosao = None

    # --- CARREGAMENTO DE SONS ---
    usa_sons = False
    try:
        som_explosao = pygame.mixer.Sound(os.path.join(caminho_sons, "explosao.wav"))
        som_ponto = pygame.mixer.Sound(os.path.join(caminho_sons, "ponto.wav"))
        pygame.mixer.music.load(os.path.join(caminho_sons, "musica.mp3"))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        usa_sons = True
    except:
        pass # Roda sem som se não achar os arquivos

    ARQUIVO_RECORDE = "recorde.txt"

    def reiniciar_jogo():
        return 3, 0, carregar_recorde(ARQUIVO_RECORDE)

    vidas, pontos, recorde = reiniciar_jogo()
    
    tempo_explosao = 0
    pos_explosao = (0, 0)

    # --- FUNDO ESTRELADO ANIMADO ---
    estrelas = []
    for _ in range(100):
        estrelas.append([random.randint(0, LARGURA_TELA), random.randint(0, ALTURA_TELA), random.randint(1, 3)])

    jogador_rect = pygame.Rect(LARGURA_TELA // 2, ALTURA_TELA - 60, LARGURA_NAVE, ALTURA_NAVE)
    
    lista_meteoros = []
    for _ in range(6):
        lista_meteoros.append(pygame.Rect(random.randint(0, LARGURA_TELA - TAMANHO_METEORO), random.randint(-500, -50), TAMANHO_METEORO, TAMANHO_METEORO))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclas = pygame.key.get_pressed()
        velocidade_extra = pontos // 10
        velocidade_atual_meteoro = VELOCIDADE_METEORO + velocidade_extra

        if vidas > 0:
            if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and jogador_rect.left > 0:
                jogador_rect.x -= VELOCIDADE_NAVE
            if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and jogador_rect.right < LARGURA_TELA:
                jogador_rect.x += VELOCIDADE_NAVE

            for meteoro in lista_meteoros:
                meteoro.y += velocidade_atual_meteoro
                
                if meteoro.top > ALTURA_TELA:
                    meteoro.y = random.randint(-200, -50)
                    meteoro.x = random.randint(0, LARGURA_TELA - TAMANHO_METEORO)
                    pontos += 1 
                    if usa_sons:
                        som_ponto.play()

            indice_colisao = jogador_rect.collidelist(lista_meteoros)
            if indice_colisao != -1:
                vidas -= 1
                if usa_sons:
                    som_explosao.play()
                
                tempo_explosao = 15
                pos_explosao = jogador_rect.center
                lista_meteoros[indice_colisao].y = random.randint(-200, -50)

            if pontos > recorde:
                recorde = pontos
                salvar_recorde(ARQUIVO_RECORDE, recorde)

        else:
            if teclas[pygame.K_r]:
                vidas, pontos, recorde = reiniciar_jogo()
                for m in lista_meteoros:
                    m.y = random.randint(-500, -50)

        # --- RENDERIZAÇÃO ---
        
        # 1. Fundo Estrelado Animado
        tela.fill(PRETO)
        for estrela in estrelas:
            estrela[1] += estrela[2] # A estrela cai
            if estrela[1] > ALTURA_TELA: # Se saiu da tela, volta pro topo
                estrela[1] = 0
                estrela[0] = random.randint(0, LARGURA_TELA)
            tamanho = 1 if estrela[2] == 1 else 2
            pygame.draw.circle(tela, BRANCO, (estrela[0], estrela[1]), tamanho)

        # 2. Gameplay
        if vidas > 0:
            if img_nave:
                tela.blit(img_nave, (jogador_rect.x, jogador_rect.y))
            else:
                pygame.draw.rect(tela, AZUL, jogador_rect)
            
            for meteoro in lista_meteoros:
                if img_meteoro:
                    tela.blit(img_meteoro, (meteoro.x, meteoro.y))
                else:
                    pygame.draw.rect(tela, VERMELHO, meteoro)
            
            if tempo_explosao > 0:
                if img_explosao:
                    rect_exp = img_explosao.get_rect(center=pos_explosao)
                    tela.blit(img_explosao, rect_exp.topleft)
                else:
                    pygame.draw.circle(tela, (255, 165, 0), pos_explosao, tempo_explosao * 2)
                tempo_explosao -= 1

            texto_vidas = fonte.render(f"Vidas: {vidas}", True, BRANCO)
            texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
            tela.blit(texto_vidas, (10, 10))
            tela.blit(texto_pontos, (10, 40))
        
        # 3. Game Over
        else:
            texto_go = fonte_grande.render("GAME OVER", True, VERMELHO)
            texto_pontuacao = fonte.render(f"Você fez: {pontos} pontos", True, BRANCO)
            texto_rec = fonte.render(f"Maior Recorde: {recorde}", True, (0, 255, 255))
            texto_restart = fonte.render("Pressione [R] para jogar novamente", True, (255, 255, 0))
            
            tela.blit(texto_go, (LARGURA_TELA//2 - texto_go.get_width()//2, ALTURA_TELA//2 - 80))
            tela.blit(texto_pontuacao, (LARGURA_TELA//2 - texto_pontuacao.get_width()//2, ALTURA_TELA//2 - 10))
            tela.blit(texto_rec, (LARGURA_TELA//2 - texto_rec.get_width()//2, ALTURA_TELA//2 + 30))
            tela.blit(texto_restart, (LARGURA_TELA//2 - texto_restart.get_width()//2, ALTURA_TELA//2 + 100))

        pygame.display.flip()
        relogio.tick(FPS)

if __name__ == "__main__":
    main()