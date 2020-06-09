import pygame
from Camara import Camara

class Fondo:

    def __init__(self,img_ruta,screen,camara, img_laberinto_ruta):
        self.camara = camara
        self.x = 0
        self.y = 0
        self.img = pygame.image.load(img_ruta)
        self.img_laberinto=pygame.image.load(img_laberinto_ruta)
        self.screen = screen

    def dibujar_fondo(self):
        self.camara.dibujar(self.img_laberinto, 0,0)
        self.camara.dibujar(self.img, 0,0)
