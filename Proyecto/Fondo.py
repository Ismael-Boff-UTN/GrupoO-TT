import pygame
from Camara import Camara

class Fondo:

    def __init__(self,img_ruta,screen,camara):
        self.camara = camara
        self.x = 0
        self.y = 0
        self.img = pygame.image.load(img_ruta)
        self.screen = screen

    def dibujar_fondo(self):
        self.screen.blit(self.img, (-self.camara.x, -self.camara.y))

