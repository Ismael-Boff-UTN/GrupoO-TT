import pygame
from pygame import mouse
from Jugador import Jugador  # importa a Jugador como un objeto instanciable
from Enemigo import Enemigo
from Fondo import Fondo
from Camara import Camara
import comunes


# Inicializa PyGame
pygame.init()
mouse.set_visible(False)



# Crear la pantalla y camara
camara=Camara(1280,720,False)
#camara=Camara(1920,1080,True)

# Fondo
fondo = Fondo("imagenes/fondo1.png",camara,"imagenes/Laberinto.png","imagenes/fondo_quieto.jpg")

comunes.img_laberinto=fondo.img_laberinto

# Titulo e Icono
pygame.display.set_caption("AirMayhaem")
icono = pygame.image.load('imagenes/icono.png') # https://www.flaticon.com/search?search-type=icons&word=arcade+space
pygame.display.set_icon(icono)

player = Jugador("imagenes/player.png", fondo.punto_aleatorio_posible_segun_laberinto(), camara, "imagenes/bullet.png")

enemy_cantidad = 30
enemy = []
items = []

for i in range(enemy_cantidad):
    enemy.append(Enemigo("imagenes/alien",fondo.punto_aleatorio_posible_segun_laberinto(),camara,"sonido\splat.wav",items))

# Variable Puntaje
puntaje_valor = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)  # dafont.com
textX = 10
textY = 10


def puntaje_mostrar(x, y,fps):
    puntaje = fuente.render("Puntaje: " + str(puntaje_valor) + " FPS: " + fps, True, (255, 255, 255))
    camara.screen.blit(puntaje, (x, y))

escala = 1 / 8
w = int(camara.screen_ancho * escala)
h = int(camara.screen_alto * escala)
mini = pygame.transform.smoothscale(fondo.img_laberinto, (w, h))

def minimapa():
    escala = 1 / 8
    w = int(camara.screen_ancho * escala)
    h = int(camara.screen_alto * escala)
    x = int(camara.screen_ancho * (1 - escala) - 50)
    y = int(camara.screen_alto * (1 - escala) - 50)
    s = pygame.Surface((w, h))  # the size of your rect
    s.set_alpha(128)  # alpha level
    s.fill((0, 0, 0))  # this fills the entire surface
    s.blit(mini, (0, 0))

    pygame.draw.circle(s, (200, 200, 255), (
        int(player.x / 3000 * w),
        int(player.y / 2000 * h)), 4, 0)

    for i in range(len(enemy)):
        if not enemy[i].muerto:
            pygame.draw.circle(s, (255, 0, 0),
                               (int(enemy[i].x / 3000 * w),
                                int(enemy[i].y / 2000 * h)), 5, 0)

    for i in range(len(player.balas)):
        pygame.draw.circle(s, (100, 100, 255), (
            int(player.balas[i].x / 3000 * w),
            int(player.balas[i].y / 2000 * h)), 5, 0)


    for h in range (len(items)):
        if items[h] != None:
            pygame.draw.circle(s, (255, 255, 255),
                               (int(items[h].x / 3000 * w),
                                int(items[h].y / 2000 * h)), 5 , 0)

    camara.screen.blit(s, (x, y))

#Control de FPS
clock = pygame.time.Clock()




# Loop principal del juego
ejecutandose = True
while ejecutandose:

    # Max FPS 120
    clock.tick(62)
    for event in pygame.event.get():  # recorre todos los eventos que suceden en la pantalla
        if event.type == pygame.QUIT:  # si el evento es el tratar de cerrar la pantalla, sale del loop
            ejecutandose = False



        # si se presiona una tecla, mover el Jugador
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


    # Movemos enemigos
    for i in range(len(enemy)):
        # Colisiones
        # Balas/Enemigos
        for j in range(len(player.balas)):
                colision = comunes.esColision((enemy[i].x+32, enemy[i].y+32), (player.balas[j].x+16, player.balas[j].y+16))
                if colision and player.balas[j].quieta==False:
                    player.balas[j].set_quieta()
                    puntaje_valor += 1
                    enemy[i].muriendo=True
        enemy[i].dibujar()

    # Player/Items
    for i in range(len(items)):
        if items[i] != None:
            colision = comunes.esColision((player.x + 32, player.y + 32),
                                          (items[i].x + 32, items[i].y + 32))
            if colision:
                items[i].comer(player)
                items[i]=None
                continue
            items[i].dibujar()

    # Dibujar el Jugador
    player.dibujar(player.x, player.y)

    puntaje_mostrar(textX, textY, str(int(clock.get_fps())))
    minimapa()
    # sin esta linea no actualiza el relleno de pantalla
    pygame.display.update()
mouse.set_visible(True)
