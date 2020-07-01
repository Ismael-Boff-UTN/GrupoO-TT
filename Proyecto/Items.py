import pygame
import random
import os



class Items:

    TIRO_TRIPLE = 1
    TIRO_RAPIDO = 2
    TIRO_REBOTE = 3
    GRAVEDAD_CERO=4
    MIRA_LASER=5
    HIPERVELOCIDAD = 6
    OSCURIDAD = 7
    BAZOOCA = 8

    BONUS_PUNTOS = 10
    REPARACION = 11
    ESCUDO_EXTRA = 12

    def __init__(self,img_ruta,xy ,camara):
        self.camara = camara

        self.img_ani = []
        lista = os.listdir(img_ruta)
        self.ani_max = len(lista)
        lista.sort()
        for imagen in lista:
            self.img_ani.append(pygame.image.load(img_ruta + "/" + imagen).convert_alpha())

        self.x = xy[0]-32
        self.y = xy[1]- 32
        self.tipo = random.randint(1,8)

    def comer(self, jugador):

      jugador.item = self.tipo




    def dibujar (self):
        self.camara.dibujar(self.img_ani[self.tipo-1],self.x, self.y)








    #def tiro_rapido:

    #def escudo_extra():

    #def hipervelocidad():
    #def reparaciones
    #def puntos_extra