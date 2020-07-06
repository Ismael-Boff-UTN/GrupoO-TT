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
        self.camara = camara
        self.camara.centrar(xy)
        self.img_ori = pygame.image.load(img_ruta).convert_alpha()
        self.ancho = self.img_ori.get_width()
        self.alto = self.img_ori.get_height()
        self.img = self.img_ori
        self.fuerza_propulsor=100
        # Mouse
        self.raton = Raton(self.camara)


        self.x = 0
        self.y = 0
        self.setPosicion(xy)
        self.velocidad =[0.0,0.0]
        self.velocidad_maxima=Jugador.VELOCIDAD_ALTA
        self.ang = 0.0
        self.friccion=Jugador.FRICCION_ALTA
        self.interaccion = comunes.INTERACCION_DESLIZARSE
        self.fuerza_disparo = 50
        self.mira_laser=False
        self.energia = 50
        self.tipo_de_velocidad = 0
        self.contador_de_avance = 0
        self.incremento_contador = 0
        self.item = 0
        self.tipo_de_disparo = 0
        self.avanzar = False
        self.retroceder = False
        # Bala
        self.balas = []
        for i in range (5):
            self.balas.append(Bala(img_bala_ruta, self.camara))

    def get_estado(self):
        estado=[]
        estado.append(self.x)
        estado.append(self.y)
        estado.append(self.velocidad)
        estado.append(self.velocidad_maxima)
        estado.append(self.ang)
        estado.append(self.friccion)
        estado.append(self.interaccion)
        estado.append(self.fuerza_disparo)
        estado.append(self.mira_laser)
        estado.append(self.energia)
        estado.append(self.tipo_de_velocidad)
        estado.append(self.contador_de_avance)
        estado.append(self.incremento_contador)
        estado.append(self.item)
        estado.append(self.tipo_de_disparo)
        estado.append(self.avanzar)
        estado.append(self.retroceder)
        estado.append(self.balas)
        return estado


    def set_estado(self, estado):
        self.x = estado[0]
        self.y = estado[1]
        self.velocidad= estado[2]
        self.velocidad_maxima= estado[3]
        self.ang= estado[4]
        self.friccion= estado[5]
        self.interaccion= estado[6]
        self.fuerza_disparo= estado[7]
        self.mira_laser= estado[8]
        self.energia= estado[9]
        self.tipo_de_velocidad= estado[10]
        self.contador_de_avance= estado[11]
        self.incremento_contador= estado[12]
        self.item= estado[13]
        self.tipo_de_disparo= estado[14]
        self.avanzar= estado[15]
        self.retroceder= estado[16]
        self.balas = estado[17]



    # Funcion que dibuja el player
    def dibujar(self):
        self.mover_jugador()
        self.rotar_jugador()

        if self.item == Items.OSCURIDAD:
            self.camara.dibujar(self.img, self.getPosicion(False),True)
        else:
            self.camara.dibujar(self.img, self.getPosicion(False),False)

        self.contador_de_avance += self.incremento_contador

        if self.item == Items.TIRO_RAPIDO:
            if (self.contador_de_avance > 5)and (self.balas[1].quieta==True):
                self.balas[1].setPosicion(self.getPosicion())
                self.balas[1].ang = self.ang
                self.balas[1].quieta = False
                self.balas[1].mover_bala()
            if (self.contador_de_avance > 15) and (self.balas[2].quieta==True):
                self.balas[2].setPosicion(self.getPosicion())
                self.balas[2].ang = self.ang
                self.balas[2].quieta = False
                self.balas[2].mover_bala()
            if (self.contador_de_avance > 20) and (self.balas[3].quieta == True):
                self.balas[3].setPosicion(self.getPosicion())
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
                    self.balas[i].setPosicion(self.getPosicion())
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
                    self.balas[i].setPosicion(self.getPosicion())
                    self.balas[i].ang = self.ang
                    self.balas[i].quieta = False
                    self.balas[i].interaccion = comunes.INTERACCION_CHOCAR
                    self.balas[i].mover_bala()
                    self.balas[i].bazooca = False
        elif (self.item == Items.TIRO_REBOTE):
            for i in range(1):
                if self.balas[i].quieta:
                    self.balas[i].setPosicion(self.getPosicion())
                    self.balas[i].ang = self.ang
                    self.balas[i].quieta = False
                    self.balas[i].interaccion= comunes.INTERACCION_REBOTAR
                    self.balas[i].mover_bala()
                    self.balas[i].bazooca = False
        elif (self.item == Items.BAZOOCA):
            for i in range(1):
                if self.balas[i].quieta:
                    self.balas[i].setPosicion(self.getPosicion())
                    self.balas[i].ang = self.ang
                    self.balas[i].quieta = False
                    self.balas[i].interaccion = comunes.INTERACCION_CHOCAR
                    self.balas[i].mover_bala()
                    self.balas[i].bazooca = True
        else:
            for i in range(1):
                if self.balas[i].quieta:
                    self.balas[i].setPosicion(self.getPosicion())
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
            self.getPosicion(),
            (avance_por_propulsores[0] + self.velocidad[0],
             avance_por_propulsores[1] + self.velocidad[1]),self.interaccion)

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
            self.velocidad[0], self.velocidad[1] = [0, 0]

        xy=[0,0]
        xy[0] = self.getPosicion()[0] + self.velocidad[0]
        xy[1] = self.getPosicion()[1] + self.velocidad[1]
        self.setPosicion(xy)

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


    def getPosicion(self,centro=True):
        if centro:
            return [self.x+self.ancho/2,self.y+self.alto/2]
        else:
            return [self.x, self.y]

    def setPosicion(self,xy,centro=True):
        if centro:
            self.x=xy[0]-self.ancho/2
            self.y=xy[1]-self.alto/2
        else:
            self.x = xy[0]
            self.y = xy[1]