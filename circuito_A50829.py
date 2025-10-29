# Importar o módulo pygame
import pygame, sys
from pygame.locals import *
from math import cos, sin, sqrt

# inicialização do módulo pygame
pygame.init()
pygame.mixer.init()

# criação de uma janela
largura = 454
altura  = 400
tamanho = (largura, altura)
janela  = pygame.display.set_mode(tamanho)
pygame.display.set_caption('CarRace da Joana') #nome da janela
#Nesta janela o ponto (0,0) é o canto superior esquerdo
#e (532-1,410-1) = (531,409) o canto inferior direito.


# número de imagens por segundo
frame_rate = 30

# relógio para controlo do tempo
clock = pygame.time.Clock()

# ler uma imagem em formato bmp
pista = pygame.image.load("circuitoA50829.jpg")
carro = pygame.image.load("carroA50829.jpg")
carro = pygame.transform.rotate(carro, 90)
pygame.mixer.music.load("som carro.mp3")
pygame.mixer.music.play(-1, 0)
pygame.mixer.music.set_volume(0.8)   



    
#Inicializa o tempo
t=0.0
v=0.0


#########################
#Para escrever o tempo:
font_size = 25
font = pygame.font.Font(None, font_size) # fonte pré-definida
antialias = True # suavização
WHITE = (255, 255, 255)# cor (terno com os valores Red, Green, Blue entre 0 e 255)


##################################
##Exemplo ajustado à pista
##Vel das retas 200
##Vel das curvas 100
def parametrizacao (t):
    if t == 0:
        resultado=(62, 145) #v=0
    if 0 < t <= 0.3:
        resultado=(62, -200 * (t) + 145) #v=200
    if 0.3 < t <= 1.4:
        resultado=(91 - 27 * cos(3 * (t - 2.4)), 85 - 30 * sin(3 * (t - 2.4))) #93<=v<=114
    if 1.4 < t <= 2.0:
        resultado=(120.7, 200 * (t - 1.4) + 89) #v=200
    if 2.0 < t <= 3.1:
        resultado=(153 - 36 * cos(3 * (t - 4.1)), 205 + 14 * sin(3 * (t - 4.1))) #54<=v<=111
    if 3.1 < t <= 3.6:
        resultado=(190, - 200 * (t - 4.1)) #v=200
    if 3.6 < t <= 4.2:
        resultado=(198 + 10 * cos(3 * (t - 2.6)), 100 + 36 * sin(3 * (t - 2.6))) #90<=v<=99
    if 4.2 < t <= 4.9:
        resultado=(199 * (t - 4.2)+ 200 , 64) #v=200
    if 4.9 < t <= 6.5:
        resultado=(338 + 30 * cos(2 * (t - 5.7)), 105 + 42 * sin(2 * (t - 5.7))) #98<=v<=102
    if 6.5 < t <= 6.8:
        resultado=(-200 * (t - 8.2), 145) #v=200
    if 6.8 < t <= 8.4:
        resultado=(280 + 46 * cos(2 * (t - 9.2)), 177 - 32 * sin(2 * (t - 9.2))) #64<=v<=88
    if 8.4 < t <= 9.8:
        resultado=(272 + 80 * cos(2 * (t - 6.0)), 273 + 65 * sin(2 * (t - 6.0))) #128<=v<=134
    if 9.8 < t <= 10.6:
        resultado=(293 + 40 * cos(2 * (t - 9.0)), 289 + 47 * sin(2 * (t - 9.0))) #20<=v<=94
    if 10.6 < t <= 12.1:
        resultado=(213 - 40 * cos(2 * (t - 12.2)), 284 + 32 * sin(2 * (t - 12.2))) #108<=v<=154
    if 12.1 < t <= 13.8:
        resultado=(120 + 58 * cos(2 * (t - 12.1)), 278 + 35 * sin(2 * (t - 12.1))) #108<=v<=200
    if 13.8 < t <= 14.4:
        resultado=(62, -200 * (t - 15.1)) #v=200
    if t > 14.4:
        resultado=(62, 145)
    return resultado

#######################

##################################
##Exemplo ajustado à pista
##Vel das retas 200
##Vel das curvas 100
def parametrizacaoRotação (t):
    carro = pygame.image.load("carroA50829.jpg")
    if t == 0:
        carro = pygame.transform.rotate(carro, 90)
    if 0 < t <= 0.3:
        carro = pygame.transform.rotate(carro, 90)
    if 0.3 < t <= 1.4:
        carro = pygame.transform.rotate(carro, -90 * (t * 1.8 - 1.54))
    if 1.4 < t <= 2.0:
        carro = pygame.transform.rotate(carro, -90)
    if 2.0 < t <= 3.1:
        carro = pygame.transform.rotate(carro, 90 * (t * 1.8 - 4.6))
    if 3.1 < t <= 3.6:
        carro = pygame.transform.rotate(carro, 90)
    if 3.6 < t <= 4.2:
        carro = pygame.transform.rotate(carro, 90 * (t *(- 1.6) + 6.72))
    if 4.2 < t <= 4.9:
        carro = pygame.transform.rotate(carro, 360)
    if 4.9 < t <= 6.5:
        carro = pygame.transform.rotate(carro, -360 * (t * (0.3) - 2.5))
    if 6.5 < t <= 6.8:
        carro = pygame.transform.rotate(carro, 180)
    if 6.8 < t <= 8.4:
        carro = pygame.transform.rotate(carro, 90 * (t * (1.3) - 10.9))
    if 8.4 < t <= 9.8:
        carro = pygame.transform.rotate(carro, -90 * (t * (1.4) - 11.8))
    if 9.8 < t <= 10.6:
        carro = pygame.transform.rotate(carro, -90 * (t * (1.4) - 11.8))
    if 10.6 < t <= 12.1:
        carro = pygame.transform.rotate(carro, 90 * (t * (1.4) - 10))
    if 12.1 < t <= 13.8:
        carro = pygame.transform.rotate(carro, 90 * (t * (-1.2) + 9.5))
    if 13.8 < t <= 14.4:
        carro = pygame.transform.rotate(carro, 90)
    if t > 14.4:
        carro = pygame.transform.rotate(carro, 90)
    return carro


def velocidade (t):
    if t == 0:
        v = 0
    if 0 < t <= 0.3:
        v = sqrt((0)**2 + (-200 + 0)**2)
    if 0.3 < t <= 1.4:
        v = sqrt((81 * sin(3 * (t - 2.4)))**2 + ((-90 * cos(3 * (t - 2.4))))**2)
    if 1.4 < t <= 2.0:
        v = sqrt((0)**2 + (200)**2)
    if 2.0 < t <= 3.1:
        v = sqrt((108 * sin(3 * (t - 4.1)))**2 + (42 * cos(3 * (t - 4.1)))**2)
    if 3.1 < t <= 3.6:
        v = sqrt((0)**2 + (200)**2)
    if 3.6 < t <= 4.2:
        v = sqrt((-30 * sin(3 * (t - 135)))**2 + (108 * cos(3 * (t - 135)))**2)
    if 4.2 < t <= 4.9:
        v = sqrt((199)**2 + (0)**2)
    if 4.9 < t <= 6.5:
        v = sqrt((-60 * sin(2 * (t - 5.7)))**2 + (84 * cos(2 * (t - 5.7)))**2)
    if 6.5 < t <= 6.8:
        v = sqrt((-200)**2 + (0)**2)
    if 6.8 < t <= 8.4:
        v = sqrt((-92 * sin(2 * (t - 465)))**2 + (-64 * cos(2 * (t - 465)))**2)
    if 8.4 < t <= 9.8:
        v = sqrt((-160 * sin(2 * (t - 6)))**2 + (130 * cos(2 * (t - 6)))**2)
    if 9.8 < t <= 10.6:
        v = sqrt((-80 * sin(2 * (t - 9)))**2 + (94 * cos(2 * (t - 9)))**2)
    if 10.6 < t <= 12.1:
        v  = sqrt((80 * sin(2 * (t - 12.2)))**2 + (64 * cos(2 * (t - 12.2)))**2)
    if 12.1 < t <= 13.8:
        v = sqrt((-116 * sin(2 * (t - 12.1)))**2 + (70 * cos(2 * (t - 12.1)))**2)
    if 13.8 < t <= 14.4:
        v = sqrt((0)**2 + (-200)**2)
    if t > 14.4:
        v = 0
    return v  

#######################

#(A) Se descomentar aqui (e comentar B) vejo onde passou/ rasto da trajetória
# Pois neste caso só junta a pista uma vez,
#no outro caso está sempre a juntar/desenhar a pista
#janela.blit(pista, (0, 0)) 

#################################
#Ciclo principal do jogo
while True:
    tempo = font.render("t="+str(int(t)), antialias, WHITE) 
    velocity = font.render("v="+str(int(velocidade(t))), antialias, WHITE) 
    janela.blit(pista, (0, 0))  #(B) se descomentar aqui (e comentar (A)) vejo movimento
    janela.blit(parametrizacaoRotação(t), parametrizacao(t))
    janela.blit(tempo, (10, 10))
    janela.blit(velocity, (10, 30))
    pygame.display.update()
    clock.tick(frame_rate)
    t=t+0.1

    if t == 0.1:
        pygame.mixer.music.play(-1, 0)
        pygame.mixer.music.set_volume(0.8)   


    if t >=14.4:
        pygame.mixer.music.stop()


    for event in pygame.event.get():
        #Para sair...
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #Ao clicar em qualquer local, o tempo recomeça com t=0
        # evento mouse click botão esquerdo (código = 1)
        elif event.type== pygame.MOUSEBUTTONUP and event.button == 1:
            t = 0
                       

##        #Quando queremos saber as coordenadas de um ponto: 
##        # descomentar isto e comentar o "evento mouse click"...
##        #"clicar" nesse ponto... o python print as coordenadas.
##        # evento mouse click botão esquerdo (código = 1)
        #elif event.type== pygame.MOUSEBUTTONUP and event.button == 1:
        #    (x, y) = event.pos
        #    localizacao="posicao=(" + str(x) + "," + str(y) + ")"
        #    print(localizacao)


##FAQs:
##Faça uma parametrização e teste no programa,depois faça a seguinte
##            e teste, e continue assim até ao fim.
##            Pois se fizer tudo “no papel” e depois testar no fim,
##            certamente não vai funcionar. 
##
##Quando uma imagem (por exemplo do carro) é colocada no ponto (x,y),
##isso significa que a o canto superior esquerdo dessa imagem
##fica nesse ponto.


#No meu trabalho eu realizei o primeiro parâmetro de avaliação bastante bem, penso eu. 
#O meu carro percorre o circuito sem sair muito por fora e as vezes que sai, é mais o retângulo
#do que o próprio carro. Fiz o segundo e terceiros parâmetros, pois adequei a velocidade às
#curvas e o valor da mesma aparece no ecrã em todos os momentos. Relativamente ao penúltimo ponto, 
#de adequar o objeto ao sentido do percurso, consegui pôr o carro a girar calmamente e não bruscamente 
#ao longo das curvas. Por fim, como detalhes adicionais e pessoais adicionei som. 
#Assim, penso que merecia um 16, pois pode haver algum ponto ou outro que possa ter ficado menos
#completo.