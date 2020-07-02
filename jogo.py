import pygame
import time
import random

pygame.init()

# Variáveis Gerais #############s

larguraTela = 335
alturaTela = 600
gamedisplay = pygame.display.set_mode((larguraTela, alturaTela))
clock = pygame.time.Clock()
# RGB (Red, Green, Blue) (0,255)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)
skateImg = pygame.image.load('assets/skate2.png')
pedraImg = pygame.image.load('assets/buraco.png')
fundo = pygame.image.load("assets/rua.jpg")
iconeJogo = pygame.image.load("assets/icon.png")
pygame.display.set_icon(iconeJogo)
pygame.display.set_caption('To School Game')
caiu = pygame.mixer.Sound("assets/caiu.wav")

# Funções Gerais #############

def mostraskate(x, y):
    gamedisplay.blit(skateImg, (x, y))
def mostraPedra(x, y):
    gamedisplay.blit(pedraImg, (int(x), int(y)))
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 45)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((larguraTela/2, alturaTela/2))
    gamedisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    game_loop()
def Caiuskate():
    pygame.mixer.Sound.play(caiu)
    message_display("Você Caiu!")
def escrevePlacar(contador):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Desvios: "+str(contador), True, white)
    gamedisplay.blit(text, (10, 30))
def game_loop():

    # Looping do Jogo

    pygame.mixer.music.load("assets/superman.mp3")
   #parametro -1, é looping infinito
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    skatePosicaoX = int(larguraTela/2)
    skatePosicaoY = int(alturaTela-200)
    movimentoX = 0
    largura_skate = 80
    altura_skate = 180
    # random é um sorteio de 0 até 800
    pedraPosicaoX = random.randrange(0, larguraTela)
    pedraPosicaoY = -600
    largura_pedra = 67
    altura_pedra = 88
    pedra_speed = 7
    contador = 0
    skate_speed = 10
    posicaoBg = 0
    while True:
        # inicio -  event.get() devolve uma lista de eventos que estão acontecendo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # quit() é comando native terminar o programa
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoX = skate_speed * -1 
                elif event.key == pygame.K_RIGHT:
                    movimentoX = skate_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    movimentoX = 0
        # fim -  event.get() devolve uma lista de eventos que estão acontecendo
        skatePosicaoX = skatePosicaoX + movimentoX
        if skatePosicaoX<0:
            skatePosicaoX = 0
        elif skatePosicaoX> larguraTela-largura_skate:
            skatePosicaoX= larguraTela-largura_skate
        
        gamedisplay.fill(white)
        posicaoBg = posicaoBg+pedra_speed
        gamedisplay.blit(fundo, (0, posicaoBg))
        gamedisplay.blit(fundo, (0, posicaoBg -600))
        if posicaoBg >=600:
            posicaoBg=0

        mostraskate(skatePosicaoX, skatePosicaoY)
        escrevePlacar(contador)
        mostraPedra(pedraPosicaoX, pedraPosicaoY)
        pedraPosicaoY = pedraPosicaoY + pedra_speed
        if pedraPosicaoY > alturaTela:
            pedraPosicaoY = 0 - altura_pedra
            pedraPosicaoX = random.randrange(0, larguraTela)
            pedra_speed = pedra_speed + 0.5
            contador = contador + 1

  
        if skatePosicaoY + 50 < pedraPosicaoY + altura_pedra:
            if skatePosicaoX < pedraPosicaoX and skatePosicaoX + largura_skate > pedraPosicaoX or pedraPosicaoX+largura_pedra > skatePosicaoX and pedraPosicaoX+largura_pedra < skatePosicaoX + largura_skate:
                Caiuskate()

        pygame.display.update()
        clock.tick(60)
game_loop()