import pygame
import comunes
from Camara import Camara

class Bala:

    def __init__(self,img_ruta,screen,camara):
        self.camara = camara
        self.img_ori = pygame.image.load(img_ruta)
        self.img = self.img_ori
        self.x = 0
        self.y = 480
        self.unidad_de_avance = 6
        self.x_cambio = self.unidad_de_avance
        self.y_cambio = self.unidad_de_avance
        self.quieta = True
        self.ang = 0.0
        self.screen=screen

    def mover_bala(self):
        if self.quieta == False:
            tmp = comunes.avanzar(0,0, self.unidad_de_avance, self.ang)
            self.x_cambio = tmp[0]
            self.y_cambio = tmp[1]
            self.x += self.x_cambio
            self.y += self.y_cambio
            self.img = comunes.rot_center(self.img_ori, self.ang - 90)
            self.quieta = False
            self.screen.blit(self.img, (self.x + 16, self.y + 10))
            if self.y < -16 or  self.y > 600 or self.x < -16 or self.x > 800:
                self.quieta = True
