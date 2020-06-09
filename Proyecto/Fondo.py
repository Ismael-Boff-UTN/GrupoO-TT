import pygame
from Camara import Camara

class Fondo:

    def __init__(self,img_ruta,screen,camara, img_laberinto_ruta):
        self.camara = camara
        self.x = 0
        self.y = 0
        self.img = pygame.image.load(img_ruta)
        self.img_laberinto=pygame.image.load(img_laberinto_ruta)
        self.img_laberintofondo = pygame.image.load(img_ruta)
        self.screen = screen

    def dibujar_fondo(self):

        self.screen.blit(self.img_laberinto, (-self.camara.x, -self.camara.y))
        self.screen.blit(self.img_laberintofondo, (-self.camara.x, -self.camara.y))
        self.screen.blit(self.img, (-self.camara.x, -self.camara.y))
