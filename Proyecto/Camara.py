import pygame
import pygame.gfxdraw

class Camara:

    def __init__(self, screen_ancho, screen_alto, fullscreen):
        self.fondo = object
        self.x=0
        self.y=0
        self.screen_ancho = screen_ancho
        self.screen_alto = screen_alto

        if fullscreen:
            self.screen = pygame.display.set_mode((self.screen_ancho, self.screen_alto), pygame.FULLSCREEN | pygame.HWSURFACE| pygame.DOUBLEBUF)
        else:
            self.screen = pygame.display.set_mode((self.screen_ancho, self.screen_alto), pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.dark=pygame.image.load("imagenes/dark.bmp").convert()


    def centrar(self,xy):
        self.set_x(xy[0]-800/2)
        self.set_y(xy[1] - 600 / 2)

    def set_x(self,x):
        if x<0:
            self.x=0
        elif x>3000-800:
            self.x=3000-800
        else:
            self.x=x

    def set_y(self,y):
        if y<0:
            self.y=0
        elif y>2000-600:
            self.y=2000-600
        else:
            self.y=y

    def dibujar(self,img,xy, dark=False):
        x=xy[0]
        y=xy[1]
        self.screen.blit(img, (x-self.x, y-self.y))

        if dark:
            color = (0,0,0,255-self.dark.get_at([1,1])[0]) #(0, 0, 0, 190)

            self.screen.blit(self.dark, (x-self.x-726/2, y-self.y-726/2), special_flags=pygame.BLEND_RGB_MULT)

            if (y - self.y - 726 / 2)>0:
                pygame.gfxdraw.box(self.screen, pygame.Rect(x - self.x - 726 / 2, 0, 726, y - self.y - 726 / 2), color)
                #pygame.draw.rect(self.screen, [0, 0, 0], [0, 0, self.screen_ancho, y - self.y - 726 / 2])
            if (y - self.y + 726) > 0:
                pygame.gfxdraw.box(self.screen, pygame.Rect(x - self.x - 726 / 2,  y - self.y + 726/2, 726, y - self.y + 726 ),color)
                #pygame.draw.rect(self.screen, [0, 0, 0], [0,  y - self.y + 726/2, self.screen_ancho, y - self.y + 726 ])
            if (x - self.x - 726 / 2) > 0:
                pygame.gfxdraw.box(self.screen,pygame.Rect(0, 0, x - self.x - 726 / 2,self.screen_alto ),color)
                #pygame.draw.rect(self.screen, [0, 0, 0], [0, 0, x - self.x - 726 / 2,self.screen_alto ])
            if (self.screen_ancho-(x - self.x + 726 / 2)) > 0:
                pygame.gfxdraw.box(self.screen, pygame.Rect(x - self.x + 726 / 2, 0, self.screen_ancho-(x - self.x + 726 / 2)+1, self.screen_alto),color)
                #pygame.draw.rect(self.screen, [0, 0, 0], [x - self.x + 726 / 2, 0, self.screen_ancho-(x - self.x + 726 / 2), self.screen_alto])


    def visible_en_camara(self,x,y,ancho,alto):
        if (x + ancho)<self.x or (y + alto)<self.y or x>(self.x+self.screen_ancho) or y>(self.y+self.screen_alto):
            return False
        else:
            return True