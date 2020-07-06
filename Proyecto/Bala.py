import pygame
import comunes


class Bala:

    def __init__(self, img_ruta, camara):
        # Construcción (fijo, solo interviene en la creación)
        self.camara = camara
        self.img_ori = pygame.image.load(img_ruta).convert_alpha()
        self.img = self.img_ori
        self.unidad_de_avance = 24
        self.masa = 100
        self.fuerza_propulsor = 10

        # Estado (variable durante el juego)
        self.x=-100
        self.y=-100
        self.ancho = self.img_ori.get_width()
        self.alto = self.img_ori.get_height()
        self.velocidad = [0.0, 0.0]
        self.ang = 0.0
        self.quieta = True
        self.contador_de_avance = 0
        self.interaccion = comunes.INTERACCION_IGNORAR
        self.bazooca = False

    def mover_bala(self):
        if self.quieta == False:
            self.contador_de_avance += 1
            [self.velocidad[0], self.velocidad[1], _, self.ang, colision_con_pared] = \
                comunes.avanzar_segun_laberinto2(self.getPosicion(), self.unidad_de_avance, self.ang, self.interaccion)

            if self.bazooca:
                if colision_con_pared == False:
                    self.camara.fondo.img.lock()
                    self.camara.fondo.img_laberinto.lock()
                    radio = int(50 - self.contador_de_avance)  # hoyo menos profundo si esta mas lejos
                    if radio < 0:
                        radio = 0
                    pygame.draw.circle(self.camara.fondo.img, (255, 255, 255, 0), self.getPosicion(),radio)
                    pygame.draw.circle(self.camara.fondo.img_laberinto, (255, 255, 255), self.getPosicion(),radio)
                    self.camara.fondo.img.unlock()
                    self.camara.fondo.img_laberinto.unlock()

            self.x += self.velocidad[0]
            self.y += self.velocidad[1]
            self.img = comunes.rot_center(self.img_ori, self.ang)


            # si la bala se va de la pantalla, que se quede quieta
            if self.camara.visible_en_camara(self.x, self.y, 16, 16)==False:
                self.set_quieta()

            # si la bala se queda quieta... que se quede quieta
            if self.velocidad == [0, 0]:
                self.set_quieta()

    def dibujar(self):
        if self.quieta==False:
            self.camara.dibujar(self.img, [self.x, self.y])


    def set_quieta(self, quieta=True):
        if quieta:
            self.quieta = True
            self.contador_de_avance = 0
            self.velocidad = [0, 0]
            self.posicion = [-100, -100]

    def getPosicion(self,centro=True):
        if centro:
            return [int(self.x+self.ancho/2),int(self.y+self.alto/2)]
        else:
            return [int(self.x), int(self.y)]

    def setPosicion(self,xy,centro=True):
        if centro:
            self.x=xy[0]-self.ancho/2
            self.y=xy[1]-self.alto/2
        else:
            self.x = xy[0]
            self.y = xy[1]

    def getAnchoAlto(self):
        return [self.ancho,self.alto]