import pygame
import sys
import random
import os
from src.config import *
from src.dados import carregar_recorde, salvar_recorde

def main():
    # 1. Inicializações
    pygame.init()
    pygame.mixer.init() # Inicializa o sistema de som!

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Meteor Evasion - Edição Premium")
    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 36)
    fonte_grande = pygame.font.SysFont(None, 60)

    # 2. Carregando ASSETS (Se não achar, usa os blocos coloridos para não dar erro)
    try:
        # Carrega Imagens
        img_nave = pygame.transform.scale(pygame.image.load(os.path.join("assets", "nave.png")), (LARGURA_NAVE, ALTURA_NAVE))
        img_meteoro = pygame.transform.scale(pygame.image.load(os.path.join("assets", "meteoro.png")), (TAMANHO_METEORO, TAMANHO_METEORO))
        img_fundo = pygame.transform.scale(pygame.image.load(os.path.join("assets", "fundo.png")), (LARGURA_TELA, ALTURA_TELA))
        img_explosao = pygame.transform.scale(pygame.image.load(os.path.join("assets", "explosao.png")), (LARGURA_NAVE * 2, ALTURA_NAVE * 2))
        usa_imagens = True
    except:
        print("Aviso: Imagens não encontradas na pasta 'assets'. Usando gráficos básicos.")
        usa_imagens = False

    try:
        # Carrega Sons
        som_explosao = pygame.mixer.Sound(os.path.join("assets", "explosao.wav"))
        som_ponto = pygame.mixer.Sound(os.path.join("assets", "ponto.wav"))
        pygame.mixer.music.load(os.path.join("assets", "musica.mp3"))
        pygame.mixer.music.set_volume(0.3) # Volume da música em 30%
        pygame.mixer.music.play(-1) # Toca a música em loop infinito (-1)
        usa_sons = True
    except:
        print("Aviso: Arquivos de áudio não encontrados. Jogando sem som.")
        usa_sons = False

    ARQUIVO_RECORDE = "recorde.txt"

    def reiniciar_jogo():
        return 3, 0, carregar_recorde(ARQUIVO_RECORDE)

    vidas, pontos, recorde = reiniciar_jogo()
    
    # Variáveis do Efeito de Explosão
    tempo_explosao = 0
    pos_explosao = (0, 0)

    jogador_rect = pygame.Rect(LARGURA_TELA // 2, ALTURA_TELA - 60, LARGURA_NAVE, ALTURA_NAVE)
    
    lista_meteoros = []
    for _ in range(6): # Quantidade de meteoros caindo
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
            # Controle da Nave
            if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and jogador_rect.left > 0:
                jogador_rect.x -= VELOCIDADE_NAVE
            if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and jogador_rect.right < LARGURA_TELA:
                jogador_rect.x += VELOCIDADE_NAVE

            # Física dos Meteoros
            for meteoro in lista_meteoros:
                meteoro.y += velocidade_atual_meteoro
                
                # Meteoro passou da tela (Ponto para o jogador!)
                if meteoro.top > ALTURA_TELA:
                    meteoro.y = random.randint(-200, -50)
                    meteoro.x = random.randint(0, LARGURA_TELA - TAMANHO_METEORO)
                    pontos += 1 
                    if usa_sons:
                        som_ponto.play() # Toca o sonzinho de ponto

            # Colisão (Nave x Meteoro)
            indice_colisao = jogador_rect.collidelist(lista_meteoros)
            if indice_colisao != -1:
                vidas -= 1
                if usa_sons:
                    som_explosao.play() # Toca o som de batida
                
                # Inicia o visual da explosão
                tempo_explosao = 15 # A explosão fica na tela por 15 frames
                pos_explosao = jogador_rect.center # Posição exata da nave

                # Joga o meteoro de volta pro céu
                lista_meteoros[indice_colisao].y = random.randint(-200, -50)

            if pontos > recorde:
                recorde = pontos
                salvar_recorde(ARQUIVO_RECORDE, recorde)

        else:
            # Controle para reiniciar no Game Over
            if teclas[pygame.K_r]:
                vidas, pontos, recorde = reiniciar_jogo()
                for m in lista_meteoros:
                    m.y = random.randint(-500, -50)

        # --- RENDERIZAÇÃO (DESENHANDO TUDO NA TELA) ---
        
        # 1. Desenha o Fundo
        if usa_imagens:
            tela.blit(img_fundo, (0, 0))
        else:
            tela.fill(PRETO)

        # 2. Desenha o Jogo se o jogador estiver vivo
        if vidas > 0:
            # A. Desenha a Nave
            if usa_imagens:
                tela.blit(img_nave, (jogador_rect.x, jogador_rect.y))
            else:
                pygame.draw.rect(tela, AZUL, jogador_rect)
            
            # B. Desenha os Meteoros
            for meteoro in lista_meteoros:
                if usa_imagens:
                    tela.blit(img_meteoro, (meteoro.x, meteoro.y))
                else:
                    pygame.draw.rect(tela, VERMELHO, meteoro)
            
            # C. Desenha a Animação de Explosão (Se houver)
            if tempo_explosao > 0:
                if usa_imagens:
                    # Centraliza a imagem da explosão em cima da nave
                    rect_exp = img_explosao.get_rect(center=pos_explosao)
                    tela.blit(img_explosao, rect_exp.topleft)
                else:
                    # Se não tiver imagem, desenha um círculo laranja expandindo
                    pygame.draw.circle(tela, (255, 165, 0), pos_explosao, tempo_explosao * 2)
                tempo_explosao -= 1 # Diminui o tempo até a explosão sumir

            # D. Textos na Tela
            texto_vidas = fonte.render(f"Vidas: {vidas}", True, BRANCO)
            texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
            tela.blit(texto_vidas, (10, 10))
            tela.blit(texto_pontos, (10, 40))
        
        # 3. Desenha a Tela de Game Over
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