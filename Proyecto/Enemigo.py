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
        self.x = xy[0]-32
        self.y = xy[1]-32
        self.unidad_de_avance=0.5
        self.x_cambio = 1.0
        self.y_cambio = 1.0
        self.muriendo=False
        self.muerto=False
        self.ani_num=0
        self.items=items

        # Sonido
#        self.sonido_al_morir = pygame.mixer.Sound(sonido_al_morir)
#        self.sonido_al_morir.set_volume(0.15)



    # Funcion que dibuja el enemigo
    def dibujar(self):
        if self.muriendo==True:
            self.ani_num += 1
#            if self.ani_num==2:
#                self.sonido_al_morir.play()
            if self.ani_num == self.ani_max:
                self.muerto = True
                self.muriendo = False
                self.items.append(Items("imagenes/item",(self.x+32,self.y+32),self.camara))
                self.x = -100
                self.y = -100
                self.ani_num = 0


        if not self.muerto:
            self.mover()
            self.camara.dibujar(self.img_ani[self.ani_num], self.x, self.y)

    def mover(self):
        # restringimos los movimientos para que no se escape de la pantalla

        avance_normal = [self.x_cambio,self.y_cambio]

        avance_normal = comunes.avanzar_segun_laberinto((self.x, self.y), avance_normal, (64, 64), comunes.INTERACCION_REBOTAR)

        self.x_cambio=avance_normal[0]
        self.y_cambio=avance_normal[1]

        self.x += self.x_cambio
        self.y += self.y_cambio

    def morir(self):
            self.muriendo = True