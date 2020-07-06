import pygame
import math

img_laberinto = None

INTERACCION_REBOTAR = 0
INTERACCION_DESLIZARSE = 1
INTERACCION_IGNORAR = 2
INTERACCION_CHOCAR = 3

def avance_ang_to_deltaXY(unidad_de_avance, ang):
    x_cambio = math.cos(math.radians(ang)) * unidad_de_avance
    y_cambio = -math.sin(math.radians(ang)) * unidad_de_avance #el eje Y crece hacia abajo en python...
    return x_cambio, y_cambio

def deltaXY_to_avance_ang(deltaXY):
    unidad_de_avance = math.sqrt(pow(deltaXY[0],2)+pow(deltaXY[1],2))
    ang = math.degrees(math.atan2(-deltaXY[1],deltaXY[0]+0.0000001))
    return unidad_de_avance, ang


def esColision(obj_1_xy, obj_2_xy,delta):
    if distancia(obj_1_xy, obj_2_xy) < delta:
        return True
    return False


def distancia(XY1, XY2):
    return math.sqrt(pow(XY1[0] - XY2[0], 2) + pow(XY1[1] - XY2[1], 2))


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def avanzar_segun_laberinto2(actual_xy, unidad_de_avance, ang, INTERACCION):
    return avanzar_segun_laberinto(actual_xy, avance_ang_to_deltaXY(unidad_de_avance, ang), INTERACCION)


def avanzar_segun_laberinto(actual_xy, delta_xy_propuesto, INTERACCION):
    delta_xy_habilitado = [0.0, 0.0]
    contacto_con_laberinto=False

    # Se fija si el punto central de la nave al moverse va a entrar en una zona blanca
    pos_x_propuesta = int(actual_xy[0] + delta_xy_propuesto[0] )
    pos_y_propuesta = int(actual_xy[1] + delta_xy_propuesto[1] )

    if pos_x_propuesta < 0 or pos_y_propuesta < 0:
        return [delta_xy_habilitado[0],delta_xy_habilitado[1],deltaXY_to_avance_ang(delta_xy_habilitado)[0],deltaXY_to_avance_ang(delta_xy_habilitado)[1],contacto_con_laberinto]
    if pos_x_propuesta > 2999 or pos_y_propuesta > 1999:
        return [delta_xy_habilitado[0],delta_xy_habilitado[1],deltaXY_to_avance_ang(delta_xy_habilitado)[0],deltaXY_to_avance_ang(delta_xy_habilitado)[1],contacto_con_laberinto]
    pos_x_quieto = int(actual_xy[0])
    pos_y_quieto = int(actual_xy[1])

    pos_x_rebote = int(actual_xy[0] - delta_xy_propuesto[0])
    pos_y_rebote = int(actual_xy[1] - delta_xy_propuesto[1])

    if (img_laberinto.get_at((pos_x_propuesta, pos_y_propuesta))[0]) == 255:
        delta_xy_habilitado[0] = delta_xy_propuesto[0]
        delta_xy_habilitado[1] = delta_xy_propuesto[1]
        contacto_con_laberinto = False
    elif INTERACCION == INTERACCION_DESLIZARSE:
        # Deslizarse. Si no puede ir para adelante pero puede ir al costado o viceversa que lo haga
        if (img_laberinto.get_at((pos_x_propuesta, pos_y_quieto))[0]) == 255:
            delta_xy_habilitado[0] = delta_xy_propuesto[0]
            contacto_con_laberinto = True
        elif (img_laberinto.get_at((pos_x_quieto, pos_y_propuesta))[0]) == 255:
            delta_xy_habilitado[1] = delta_xy_propuesto[1]
            contacto_con_laberinto = True
    elif INTERACCION == INTERACCION_REBOTAR:
        if (img_laberinto.get_at((pos_x_propuesta, pos_y_rebote))[0]) == 255:
            delta_xy_habilitado[0] = delta_xy_propuesto[0]
            delta_xy_habilitado[1] = -delta_xy_propuesto[1]
            contacto_con_laberinto = True
        elif (img_laberinto.get_at((pos_x_rebote, pos_y_propuesta))[0]) == 255:
            delta_xy_habilitado[0] = -delta_xy_propuesto[0]
            delta_xy_habilitado[1] = delta_xy_propuesto[1]
            contacto_con_laberinto=True
    elif INTERACCION == INTERACCION_IGNORAR:
        delta_xy_habilitado[0] = delta_xy_propuesto[0]
        delta_xy_habilitado[1] = delta_xy_propuesto[1]
    elif INTERACCION == INTERACCION_CHOCAR:
        delta_xy_habilitado[0] = 0
        delta_xy_habilitado[1] = 0

    return [delta_xy_habilitado[0],delta_xy_habilitado[1],deltaXY_to_avance_ang(delta_xy_habilitado)[0],deltaXY_to_avance_ang(delta_xy_habilitado)[1],contacto_con_laberinto]

def switcher (variable, valor1,valor2):
    if variable == valor1:
        variable = valor2
    else:
        variable = valor1
    return variable

def velocidad(fuerza,masa,tiempo_de_aplicacion):
    vx=(fuerza[0]/masa)*tiempo_de_aplicacion
    vy=(fuerza[1]/masa)*tiempo_de_aplicacion
    return vx,vy