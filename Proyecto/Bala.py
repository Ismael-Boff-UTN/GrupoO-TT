import pygame
import comunes
from Camara import Camara

class Bala:

    def __init__(self,img_ruta,camara):
        self.camara = camara
        self.img_ori = pygame.image.load(img_ruta)
        self.img = self.img_ori
        self.x = 400
        self.y = 400
        self.unidad_de_avance = 12
        self.x_cambio = self.unidad_de_avance
        self.y_cambio = self.unidad_de_avance
        self.quieta = True
        self.ang = 0.0


    def mover_bala(self):
        if self.quieta == False:
            tmp = comunes.avanzar_segun_laberinto2((self.x,self.y),self.unidad_de_avance, self.ang,(32,20),comunes.INTERACCION_REBOTAR)
            self.x_cambio = tmp[0]
            self.y_cambio = tmp[1]
            self.ang=tmp[3]
            self.x += self.x_cambio
            self.y += self.y_cambio
            self.img = comunes.rot_center(self.img_ori, self.ang)
            self.camara.dibujar(self.img, self.x + 16, self.y + 10)


            #si la bala se va de la pantalla, que se quede quieta
            if not self.camara.visible_en_camara(self.x,self.y,16,16 ):
                self.quieta = True
