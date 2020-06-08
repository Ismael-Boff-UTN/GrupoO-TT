import pygame
import math

def avanzar(x_cambio_actual, y_cambio_actual,unidad_de_avance, ang):
    #y_cambio = y_cambio_actual - math.sin(ang * (math.pi / 180)) * unidad_de_avance
    #x_cambio = x_cambio_actual + math.cos(ang * (math.pi / 180)) * unidad_de_avance
    y_cambio = - math.sin(ang * (math.pi / 180)) * unidad_de_avance
    x_cambio = + math.cos(ang * (math.pi / 180)) * unidad_de_avance
    return x_cambio, y_cambio

def sumar_vector(a,b):
    return a[0]+b[0],a[1]+b[1]


def esColision(enemyX, enemyY, balaX, balaY):
    try:
        distancia = math.sqrt(pow(enemyX - balaX, 2) + pow(enemyY - balaY, 2))
        if distancia < 27:
            return True
    except:
        return False

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image