import pygame
import random

class Fondo:

    def __init__(self,img_ruta,camara, img_laberinto_ruta,img_fondo_estatico_ruta):
        self.camara = camara
        self.camara.fondo=self
        self.x = 0
        self.y = 0
        self.img = pygame.image.load(img_ruta).convert_alpha()
        self.img_laberinto=pygame.image.load(img_laberinto_ruta).convert()
        #Adapta la imagen estatica de fondo al tamaño de pantalla
        w, h = self.img_laberinto.get_size()
        self.img_fondo_estatico = pygame.transform.smoothscale(pygame.image.load(img_fondo_estatico_ruta).convert(), (
        camara.screen_ancho, int((h / w) * camara.screen_ancho)))

    def dibujar_fondo(self):
        self.camara.dibujar(self.img_laberinto, 0, 0)
        self.camara.dibujar(self.img_fondo_estatico, self.camara.x, self.camara.y)
        self.camara.dibujar(self.img, 0,0)


    def punto_posible_segun_laberinto(self,x,y):
        if (self.img_laberinto.get_at((x,y))[0]) == 255:
            return True
        else:
            return False

    def punto_aleatorio_posible_segun_laberinto(self):
        while (True):
            x = random.randint(1,2999)
            y = random.randint(1,1999)
            if self.punto_posible_segun_laberinto(x,y):
                return x,y