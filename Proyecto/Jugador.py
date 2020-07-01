import pygame
import comunes
from Bala import Bala
from Items import Items
from Raton import Raton

class Jugador:
    FRICCION_ALTA = 0.55
    FRICCION_BAJA = 0.03
    VELOCIDAD_ALTA = 12
    VELOCIDAD_BAJA = 8

    # Constructor def __init__(self, atributos)
    def __init__(self, img_ruta, xy, camara, img_bala_ruta):
        self.energia = 50
        self.tipo_de_velocidad = 0
        self.contador_de_avance =0
        self.incremento_contador = 0
        self.item = 0
        self.tipo_de_disparo = 0

        self.camara = camara
        self.camara.centrar(xy)
        self.img_ori = pygame.image.load(img_ruta).convert_alpha()
        self.ancho = self.img_ori.get_width()
        self.alto = self.img_ori.get_height()
        self.x = xy[0] - self.ancho/2
        self.y = xy[1] - self.alto/2
        self.img = self.img_ori
        self.mira_laser=False

        self.velocidad =[0.0,0.0]
        self.fuerza_propulsor=100
        self.velocidad_maxima=Jugador.VELOCIDAD_ALTA
        self.ang = 0.0
        self.friccion=Jugador.FRICCION_ALTA
        self.interaccion = comunes.INTERACCION_DESLIZARSE
        self.fuerza_disparo = 50

        self.avanzar = False
        self.retroceder = False

        # Bala
        self.balas =  []
        for i in range (5):
            self.balas.append(Bala(img_bala_ruta, self.camara))
        # Mouse
        self.raton = Raton(self.camara)

    # Funcion que dibuja el player
    def dibujar(self, x, y):
        self.mover_jugador()
        self.rotar_jugador()

        if self.item == Items.OSCURIDAD:
            self.camara.dibujar(self.img, x, y,True)
        else:
            self.camara.dibujar(self.img, x, y,False)

        self.contador_de_avance += self.incremento_contador

        if self.item == Items.TIRO_RAPIDO:
            if (self.contador_de_avance > 5)and (self.balas[1].quieta==True):
                self.balas[1].x = self.x
                self.balas[1].y = self.y
                self.balas[1].ang = self.ang
                self.balas[1].quieta = False
                self.balas[1].mover_bala()
            if (self.contador_de_avance > 15) and (self.balas[2].quieta==True):
                self.balas[2].x = self.x
                self.balas[2].y = self.y
                self.balas[2].ang = self.ang
                self.balas[2].quieta = False
                self.balas[2].mover_bala()
            if (self.contador_de_avance > 20) and (self.balas[3].quieta == True):
                self.balas[3].x = self.x
                self.balas[3].y = self.y
                self.balas[3].ang = self.ang
                self.balas[3].quieta = False
                self.balas[3].mover_bala()
                self.contador_de_avance = 0
                self.incremento_contador = 0

    def tecla_presionada(self, eventkey):
        if eventkey == pygame.K_w:
            self.avanzar = True
        #if eventkey == pygame.K_s:
        #   self.friccion=comunes.switcher(self.friccion,Jugador.FRICCION_ALTA,Jugador.FRICCION_BAJA)
        if eventkey == pygame.K_d:
            self.mira_laser=comunes.switcher(self.mira_laser,True,False)
            self.velocidad_maxima=comunes.switcher(self.velocidad_maxima,Jugador.VELOCIDAD_ALTA,Jugador.VELOCIDAD_BAJA)
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
                    self.balas[i].interaccion = comunes.INTERACCION_CHOCAR
                    self.balas[i].mover_bala()
                    self.balas[i].bazooca = False
        elif (self.item == Items.TIRO_RAPIDO):
            for i in range(5):
                if self.balas[i].quieta:
                    self.balas[i].x = self.x
                    self.balas[i].y = self.y
                    self.balas[i].ang = self.ang
                    self.balas[0].quieta = False
                    self.balas[i].interaccion = comunes.INTERACCION_CHOCAR
                    self.balas[0].mover_bala()
                    self.balas[i].bazooca = False
        elif (self.item == Items.TIRO_REBOTE):
            for i in range(1):
                if self.balas[i].quieta:
                    self.balas[i].x = self.x
                    self.balas[i].y = self.y
                    self.balas[i].ang = self.ang
                    self.balas[i].quieta = False
                    self.balas[i].interaccion= comunes.INTERACCION_REBOTAR
                    self.balas[i].mover_bala()
                    self.balas[i].bazooca = False
        elif (self.item == Items.BAZOOCA):
            for i in range(1):
                if self.balas[i].quieta:
                    self.balas[i].x = self.x
                    self.balas[i].y = self.y
                    self.balas[i].ang = self.ang
                    self.balas[i].quieta = False
                    self.balas[i].interaccion = comunes.INTERACCION_CHOCAR
                    self.balas[i].bazooca = True
        else:
            for i in range(1):
                if self.balas[i].quieta:
                    self.balas[i].x = self.x
                    self.balas[i].y = self.y
                    self.balas[i].ang = self.ang
                    self.balas[i].quieta = False
                    self.balas[i].interaccion =comunes.INTERACCION_CHOCAR
                    self.balas[i].mover_bala()
                    self.balas[i].bazooca = False

    def tecla_levantada(self, eventkey):
        if eventkey == pygame.K_w:
            self.avanzar = False

    def mover_jugador(self):
        # Movemos el jugador segun la tecla presionada
        avance_por_propulsores = [0.0, 0.0]

        if self.item==Items.HIPERVELOCIDAD:
            self.velocidad_maxima = Jugador.VELOCIDAD_ALTA
        else:
            self.velocidad_maxima = Jugador.VELOCIDAD_BAJA

        if self.item == Items.GRAVEDAD_CERO:
            self.friccion = Jugador.FRICCION_BAJA
            self.interaccion = comunes.INTERACCION_REBOTAR
        else:
            self.friccion = Jugador.FRICCION_ALTA
            self.interaccion = comunes.INTERACCION_DESLIZARSE

        if self.avanzar:
            avance_por_propulsores = comunes.velocidad(
                comunes.avance_ang_to_deltaXY(self.fuerza_propulsor, self.ang), 300, 5)

        self.velocidad[0], self.velocidad[1], d, ang, contacto_con_pared = comunes.avanzar_segun_laberinto(
            (self.x, self.y),
            (avance_por_propulsores[0] + self.velocidad[0],
             avance_por_propulsores[1] + self.velocidad[1]),
            (64, 64),  self.interaccion)

        if comunes.deltaXY_to_avance_ang(self.velocidad)[0] > self.velocidad_maxima:
            self.velocidad[0], self.velocidad[1] = comunes.avance_ang_to_deltaXY(self.velocidad_maxima,
                                                                                 comunes.deltaXY_to_avance_ang(
                                                                                     self.velocidad)[1])

        if comunes.deltaXY_to_avance_ang(self.velocidad)[0] > 0:
            self.velocidad[0], self.velocidad[1] = comunes.avance_ang_to_deltaXY(
                comunes.deltaXY_to_avance_ang(self.velocidad)[0] - self.friccion,
                comunes.deltaXY_to_avance_ang(self.velocidad)[1])

        if comunes.deltaXY_to_avance_ang(self.velocidad)[0] < 0 or comunes.deltaXY_to_avance_ang(self.velocidad)[
            0] < 0.5:
            self.velocidad[0], self.velocidad[1] = 0, 0

        self.x += self.velocidad[0]
        self.y += self.velocidad[1]

        # la camara sigue al jugador
        if (self.x - self.camara.x) <  self.camara.screen_ancho*3/8:
            self.camara.set_x(self.camara.x - abs(self.velocidad[0]))
        elif (self.x - self.camara.x) > self.camara.screen_ancho*5/8:
            self.camara.set_x(self.camara.x + abs(self.velocidad[0]))
        if (self.y - self.camara.y) < self.camara.screen_alto*3/8:
            self.camara.set_y(self.camara.y - abs(self.velocidad[1]))
        elif (self.y - self.camara.y) > self.camara.screen_alto*5/8:
            self.camara.set_y(self.camara.y + abs(self.velocidad[1]))

        # mover bala
        for i in range(len(self.balas)):
            self.balas[i].mover_bala()

    def rotar_jugador(self):

        self.ang = self.raton.get_angulo()


        if self.item == Items.MIRA_LASER:
            self.raton.restringir_mouse( self.camara.screen_alto/2 * 6/7 )
            pygame.draw.line(self.camara.screen, (255,255, 255), (self.x-self.camara.x+32, self.y-self.camara.y+32), (
            comunes.avance_ang_to_deltaXY(1500, self.ang)[0] + self.x-self.camara.x+32,
            comunes.avance_ang_to_deltaXY(1500, self.ang)[1] + self.y-self.camara.y+32),3)
            pygame.draw.line(self.camara.screen, (255, 0, 0), (self.x - self.camara.x + 32, self.y - self.camara.y + 32), (
                comunes.avance_ang_to_deltaXY(1500, self.ang)[0] + self.x - self.camara.x + 32,
                comunes.avance_ang_to_deltaXY(1500, self.ang)[1] + self.y - self.camara.y + 32))
        else:
            self.raton.restringir_mouse(100)

        self.img = comunes.rot_center(self.img_ori, self.ang)


