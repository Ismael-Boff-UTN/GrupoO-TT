import pygame
import comunes

class Bala:

    def __init__(self,img_ruta,camara):
        self.camara = camara
        self.img_ori = pygame.image.load(img_ruta).convert_alpha()
        self.img = self.img_ori
        self.x = 400
        self.y = 400
        self.unidad_de_avance = 24
        self.x_cambio = self.unidad_de_avance
        self.y_cambio = self.unidad_de_avance

        self.velocidad =[0.0,0.0]
        self.masa=100
        self.fuerza_propulsor=10

        self.quieta = True
        self.ang = 0.0
        self.contador_de_avance = 0
        self.interaccion = comunes.INTERACCION_IGNORAR
        self.bazooca = False

    def mover_bala(self):
        if self.quieta == False:
            self.contador_de_avance+=1
            tmp = comunes.avanzar_segun_laberinto2((self.x,self.y),self.unidad_de_avance, self.ang,(32,20),self.interaccion)

            if self.bazooca:
                if tmp[4] == False:
                    self.camara.fondo.img.lock()
                    self.camara.fondo.img_laberinto.lock()
                    radio=int(50-self.contador_de_avance) #hoyo menos profundo si esta mas lejos
                    if radio<0:
                        radio=0
                    pygame.draw.circle(self.camara.fondo.img, (255, 255, 255,0), (int(self.x+16),int(self.y+16)), radio  )
                    pygame.draw.circle(self.camara.fondo.img_laberinto, (255, 255, 255), (int(self.x + 16), int(self.y + 16)), radio)
                    self.camara.fondo.img.unlock()
                    self.camara.fondo.img_laberinto.unlock()

            self.x_cambio = tmp[0]
            self.y_cambio = tmp[1]
            self.ang=tmp[3]
            self.x += self.x_cambio
            self.y += self.y_cambio
            self.img = comunes.rot_center(self.img_ori, self.ang)
            self.camara.dibujar(self.img, self.x + 16, self.y + 10)

            #si la bala se va de la pantalla, que se quede quieta
            if not self.camara.visible_en_camara(self.x,self.y,16,16 ):
                self.set_quieta()

                # si la bala se va de la pantalla, que se quede quieta
            if self.x_cambio==0 and self.y_cambio ==0:
                self.set_quieta()

    def set_quieta(self,quieta=True):
        if quieta:
            self.quieta=True
            self.contador_de_avance = 0
            self.x=-100
            self.y=-100
