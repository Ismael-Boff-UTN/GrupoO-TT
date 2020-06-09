import pygame
from jugador import jugador  # importa a jugador como un objeto instanciable
from Enemigo import Enemigo
from Fondo import Fondo
from Camara import Camara
import comunes
from pygame import mouse

# Inicializa PyGame
pygame.init()
mouse.set_visible(False)
# Crear la pantalla y camara
screen = pygame.display.set_mode((800, 600))
camara=Camara(screen)

# Fondo
fondo = Fondo("imagenes/fondo.jpg",screen,camara,"imagenes/Laberinto.png")

# Titulo e Icono
pygame.display.set_caption("AirMayhaem")
icono = pygame.image.load('imagenes/icono.png') # https://www.flaticon.com/search?search-type=icons&word=arcade+space
pygame.display.set_icon(icono)

player = jugador("imagenes/player.png", 170, 280, screen,camara,"imagenes/bullet.png", fondo.img_laberinto)

enemy_cantidad = 3
enemy = []

for i in range(enemy_cantidad):
    enemy.append(Enemigo("imagenes/alien.png",screen,camara))

# Variable Puntaje
puntaje_valor = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)  # dafont.com
textX = 10
textY = 10


def puntaje_mostrar(x, y):
    puntaje = fuente.render("Puntaje: " + str(puntaje_valor), True, (255, 255, 255))
    screen.blit(puntaje, (x, y))

# Loop principal del juego
ejecutandose = True
while ejecutandose:
    for event in pygame.event.get():  # recorre todos los eventos que suceden en la pantalla
        if event.type == pygame.QUIT:  # si el evento es el tratar de cerrar la pantalla, sale del loop
            ejecutandose = False

        # si se presiona una tecla, mover el jugador
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # si el evento es el tratar de cerrar la pantalla, sale del loop
                ejecutandose = False
            player.tecla_presionada(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT :
            player.disparar()
        if event.type == pygame.KEYUP:
            player.tecla_levantada(event.key)

    # Dibujar Imagen de fondo
    fondo.dibujar_fondo()

    # Dibujar el jugador
    player.dibujar(player.x, player.y,pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    # Movemos enemigos
    for i in range(enemy_cantidad):
        # Colisiones
        colision = comunes.esColision(enemy[i].x+32, enemy[i].y+32, player.bala.x+16, player.bala.y+16)
        if colision:
            player.bala.quieta = True
            puntaje_valor += 1
            enemy[i].morir()

        enemy[i].dibujar()

    puntaje_mostrar(textX, textY)

    # sin esta linea no actualiza el relleno de pantalla
    pygame.display.update()
mouse.set_visible(True)
