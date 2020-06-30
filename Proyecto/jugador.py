import pygame
import comunes
import math
from Bala import Bala
from pygame import mouse
from Items import Items


class jugador:

    # Constructor def __init__(self, atributos)
    def __init__(self, img_ruta, xy, camara, img_bala_ruta, img_laberinto):
        self.energia = 50
        self.tipo_de_velocidad = 0
        self.contador_de_avance =0
        self.incremento_contador = 0
        self.item = 0

        self.tipo_de_disparo = 0
        self.camara = camara
        self.ancho = 64
        self.alto = 64
        self.x = xy[0] - 32
        self.y = xy[1] - 32
        self.camara.centrar(xy)
        self.img_ori = pygame.image.load(img_ruta).convert_alpha()
        self.img = self.img_ori
        self.x_cambio = 0.0
        self.y_cambio = 0.0
        self.unidad_de_avance = 3
        self.ang = 0.0
        self.avanzar = False
        self.retroceder = False
        self.img_laberinto = img_laberinto
        # Bala

        self.balas =  []
        for i in range (5):
            self.balas.append(Bala(img_bala_ruta, self.camara))



    # Funcion que dibuja el player
    def dibujar(self, x, y, mouse_x, mouse_y):
        self.mover_jugador()
        self.rotar_jugador(mouse_x, mouse_y)
        self.camara.dibujar(self.img, x, y)
        self.contador_de_avance += self.incremento_contador
        if (self.contador_de_avance > 5)and (self.balas[1].quieta==True):
            self.balas[1].quieta = False
            self.balas[1].mover_bala()

        if (self.contador_de_avance > 10)and (self.balas[2].quieta==True):
            self.balas[2].quieta = False
            self.balas[2].mover_bala()

        if (self.contador_de_avance > 15) and (self.balas[3].quieta == True):
            self.balas[3].quieta = False
            self.balas[3].mover_bala()
        if (self.contador_de_avance > 20) and (self.balas[4].quieta == True):
            self.balas[4].quieta = False
            self.balas[4].mover_bala()
            self.contador_de_avance = 0
            self.incremento_contador = 0

    def tecla_presionada(self, eventkey):
        if eventkey == pygame.K_w:
            self.avanzar = True
            self.retroceder = False
        if eventkey == pygame.K_s:
            self.retroceder = True
            self.avanzar = False
        if eventkey == pygame.K_SPACE:
            self.disparar()

    def disparar(self):
        self.incremento_contador=1


        if (self.item ==Items.TIRO_TRIPLE):
            for i in range (3):
                if self.balas[i].quieta:
                    self.balas[i].x = self.x
                    self.balas[i].y = self.y
                    self.balas[0].ang = self.ang-30
                    self.balas[1].ang = self.ang
                    self.balas[2].ang = self.ang+30
                    self.balas[i].quieta = False
                    self.balas[i].interaccion = comunes.INTERACCION_IGNORAR

                    self.balas[i].mover_bala()
        elif (self.item == Items.TIRO_RAPIDO):
            for i in range(5):
                if self.balas[i].quieta:
                    self.balas[i].x = self.x
                    self.balas[i].y = self.y
                    self.balas[i].ang = self.ang
                    self.balas[0].quieta = False
                    self.balas[i].interaccion = comunes.INTERACCION_IGNORAR
                    self.balas[0].mover_bala()

        elif (self.item == Items.TIRO_REBOTE):
            for i in range(5):
                if self.balas[i].quieta:
                    self.balas[i].x = self.x
                    self.balas[i].y = self.y
                    self.balas[i].ang = self.ang
                    self.balas[i].quieta = False
                    self.balas[i].interaccion= comunes.INTERACCION_REBOTAR
                    self.balas[i].mover_bala()


        else:

            for i in range(3):
                if self.balas[i].quieta:
                    self.balas[i].x = self.x
                    self.balas[i].y = self.y
                    self.balas[i].ang = self.ang
                    self.balas[i].quieta = False
                    self.balas[i].interaccion =comunes.INTERACCION_IGNORAR
                    self.balas[i].mover_bala()

    def tecla_levantada(self, eventkey):

        if eventkey == pygame.K_w:
            self.avanzar = False
            detener_avance = comunes.avance_ang_to_deltaXY(self.unidad_de_avance, self.ang)
            self.x_cambio = detener_avance[0]
            self.y_cambio = detener_avance[1]
        if eventkey == pygame.K_s:
            self.retroceder = False
            detener_retroceso = comunes.avance_ang_to_deltaXY(-self.unidad_de_avance, self.ang)
            self.x_cambio = detener_retroceso[0]
            self.y_cambio = detener_retroceso[1]

    def mover_jugador(self):
        # Movemos el jugador segun la tecla presionada


        avance_normal = [0.0, 0.0]

        if self.item==Items.HIPERVELOCIDAD:
            if self.avanzar:
                avance_normal = comunes.avance_ang_to_deltaXY(self.unidad_de_avance+15, self.ang)
            if self.retroceder:
                avance_normal = comunes.avance_ang_to_deltaXY(self.unidad_de_avance+15, self.ang + 180)
        else:
            if self.avanzar:
                avance_normal = comunes.avance_ang_to_deltaXY(self.unidad_de_avance, self.ang)
            if self.retroceder:
                avance_normal = comunes.avance_ang_to_deltaXY(self.unidad_de_avance, self.ang + 180)
        avance_normal = comunes.avanzar_segun_laberinto((self.x, self.y), avance_normal, (64, 64), comunes.INTERACCION_DESLIZARSE)

        self.x += avance_normal[0]
        self.y += avance_normal[1]

        # la camara sigue al jugador
        if (self.x - self.camara.x) < 200:
            self.camara.set_x(self.camara.x - abs(avance_normal[0]))
        elif (self.x - self.camara.x) > 400:
            self.camara.set_x(self.camara.x + abs(avance_normal[0]))
        if (self.y - self.camara.y) < 200:
            self.camara.set_y(self.camara.y - abs(avance_normal[1]))
        elif (self.y - self.camara.y) > 400:
            self.camara.set_y(self.camara.y + abs(avance_normal[1]))

        # mover bala
        for i in range(5):
            self.balas[i].mover_bala()

    def rotar_jugador(self, mouse_x, mouse_y):
        self.ang = comunes.deltaXY_to_avance_ang(((mouse_x - (800 / 2) + 0.0000001),(mouse_y - (600 / 2))))[1]
        self.img = comunes.rot_center(self.img_ori, self.ang)


        #Restringir mouse
        md = comunes.distancia(mouse.get_pos(), ((800 / 2), (600 / 2)))

        d = 100
        a = 60

        if md > (d + a / 2) or md < (d - a / 2):
            m_ang = math.atan2((mouse.get_pos()[1] - (600 / 2)), (mouse.get_pos()[0] - (800 / 2) + 0.0000001))
            m_x = d * math.cos(m_ang) + (800 / 2)
            m_y = d * math.sin(m_ang) + (600 / 2)
            mouse.set_pos(m_x, m_y)


