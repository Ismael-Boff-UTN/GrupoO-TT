import pygame
import comunes
import math
from Bala import Bala
import random
from Camara import Camara

class Enemigo:

    def __init__(self, img_ruta, screen,camara):
        self.camara = camara
        self.img_ori = pygame.image.load(img_ruta)
        self.img = self.img_ori
        self.x = random.randint(0, 800 - 64)
        self.y = random.randint(50, 150)
        self.unidad_de_avance=0.3
        self.x_cambio = 1.0
        self.y_cambio = 1.0
        self.screen = screen
        self.muerto=False

    def morir(self):
        self.muerto=True
        self.x=-100
        self.y=-100
    # Funcion que dibuja el enemigo
    def dibujar(self):
        self.mover()
        if not self.muerto:
            self.screen.blit(self.img, (self.x-self.camara.x, self.y-self.camara.y))
        
    def mover(self):
        self.y += self.y_cambio
        self.x += self.x_cambio
        # restringimos los movimientos para que no se escape de la pantalla

        if self.x < 0:
            self.unidad_de_avance *= random.random() + 0.5
            self.x_cambio = self.unidad_de_avance
        elif self.x > (800 - 64):
            self.unidad_de_avance *= random.random() + 0.5
            self.x_cambio = -self.unidad_de_avance
        if self.y < 0:
            self.unidad_de_avance *= random.random() + 0.5
            self.y_cambio = self.unidad_de_avance
        elif self.y > (600 - 64):
            self.unidad_de_avance *= random.random() + 0.5
            self.y_cambio = -self.unidad_de_avance