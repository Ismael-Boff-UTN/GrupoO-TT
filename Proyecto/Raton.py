from pygame import mouse
import comunes
import pygame

class Raton:

    def __init__(self,camara):
        self.camara = camara
        self.angulo=0.0
        self.radio=100


    def set_angulo(self,radio,angulo):
        centro = [(self.camara.screen_ancho / 2), (self.camara.screen_alto / 2)]

        m_x,m_y=comunes.avance_ang_to_deltaXY(radio,angulo)
        mouse.set_pos(m_x+centro[0], m_y+centro[1])
        self.angulo=angulo

    def get_angulo(self):
        centro = [(self.camara.screen_ancho / 2), (self.camara.screen_alto / 2)]

        mouse_x=pygame.mouse.get_pos()[0]
        mouse_y=pygame.mouse.get_pos()[1]
        self.angulo=comunes.deltaXY_to_avance_ang(
            ((mouse_x - centro[0] + 0.0000001), (mouse_y - centro[1])))[1]
        return self.angulo

    def restringir_mouse(self,radio):
        centro = [(self.camara.screen_ancho / 2), (self.camara.screen_alto / 2)]
        md = comunes.distancia(mouse.get_pos(), centro)
        a = 2
        if md > (radio + a ) or md < (radio - a ):
            m_ang=comunes.deltaXY_to_avance_ang(((mouse.get_pos()[0] - centro[0] + 0.0000001),(mouse.get_pos()[1] - centro[1])))[1]
            self.set_angulo(radio,m_ang)