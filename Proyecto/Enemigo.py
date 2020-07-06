import pygame
import comunes
import os
from Items import Items

class Enemigo:

    def __init__(self, img_ruta, xy, camara,sonido_al_morir,items):
        self.camara = camara
        self.img_ani = []
        lista = os.listdir(img_ruta)
        self.ani_max = len(lista)
        lista.sort()
        for imagen in lista:
            self.img_ani.append(pygame.image.load(img_ruta + "/" + imagen).convert_alpha())
        self.ancho = self.img_ani[0].get_width()
        self.alto = self.img_ani[0].get_height()
        # Sonido
        self.sonido_al_morir = pygame.mixer.Sound(sonido_al_morir)
        self.sonido_al_morir.set_volume(0.15)


        self.x = 0
        self.y = 0
        self.setPosicion(xy)
        self.velocidad =[1.0,1.0]
        self.ani_num = 0
        self.muriendo=False
        self.muerto=False
        self.items=items
        self.ani_num=0

    def get_estado(self):
        estado = []
        estado.append(self.x)
        estado.append(self.y)
        estado.append(self.velocidad)
        estado.append(self.muriendo)
        estado.append(self.muerto)
        estado.append(self.items)
        estado.append(self.ani_num)
        return estado

    def set_estado(self,estado):
        self.x=estado[0]
        self.y=estado[1]
        self.velocidad=estado[2]
        self.muriendo=estado[3]
        self.muerto=estado[4]
        self.items=estado[5]
        self.ani_num=estado[6]

    def actualizar(self):
        if self.muriendo==True:
            self.ani_num += 1
            if self.ani_num==2:
                self.sonido_al_morir.play()
            if self.ani_num == self.ani_max:
                self.muerto = True
                self.muriendo = False
                self.items.append(Items("imagenes/item",self.getPosicion(),self.camara))
                self.setPosicion([-100,-100])
                self.ani_num = 0
        if self.muerto==False:
            self.mover()

    # Funcion que dibuja el enemigo
    def dibujar(self):
        if not self.muerto:
            self.mover()
            self.camara.dibujar(self.img_ani[self.ani_num], [self.x, self.y])

    def mover(self):
        # restringimos los movimientos para que no se escape de la pantalla

        self.velocidad = comunes.avanzar_segun_laberinto(self.getPosicion(), self.velocidad, comunes.INTERACCION_REBOTAR)


        xy = [0, 0]
        xy[0] = self.getPosicion()[0] + self.velocidad[0]
        xy[1] = self.getPosicion()[1] + self.velocidad[1]
        self.setPosicion(xy)

    def morir(self):
            self.muriendo = True

    def getPosicion(self,centro=True):
        if centro:
            return [int(self.x+self.ancho/2),int(self.y+self.alto/2)]
        else:
            return [int(self.x), int(self.y)]

    def setPosicion(self,xy,centro=True):
        if centro:
            self.x=xy[0]-self.ancho/2
            self.y=xy[1]-self.alto/2
        else:
            self.x = xy[0]
            self.y = xy[1]