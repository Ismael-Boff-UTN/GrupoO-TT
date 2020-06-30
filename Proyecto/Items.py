import pygame
import comunes
import random




class Items:

    TIRO_TRIPLE = 1
    TIRO_RAPIDO = 2
    TIRO_REBOTE = 3
    REPARACION = 4
    ESCUDO_EXTRA = 5
    GRAVEDAD_CERO=6
    MIRA_LASER=7
    BONUS_PUNTOS = 8
    HIPERVELOCIDAD = 9

    def __init__(self,img_ruta,xy ,camara, img_laberinto):
        self.camara = camara
        self.img_ori = pygame.image.load(img_ruta).convert_alpha()
        self.img = self.img_ori
        self.x = xy[0]-32
        self.y = xy[1]- 32
        self.tipo = 3



        self.comido = False
        self.img_laberinto = img_laberinto

    def comer(self, jugador):

      jugador.item = self.tipo




    def dibujar (self):
        self.camara.dibujar(self.img,self.x, self.y)

    def desaparecer(self):
        self.comido = True






    #def tiro_rapido:

    #def escudo_extra():

    #def hipervelocidad():
    #def reparaciones
    #def puntos_extra