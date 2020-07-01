
import sys
import socket
import pygame

# import Server
# import jugador1
# import jugador2
# import jugador3
# import jugador4


class Menu:
    '''Muestra un menu y responde a elecciones cuando se ejecuta.'''
    def __init__(self):
        self.cuaderno = Cuaderno()
        self.elecciones = {
                "1" : self.jugador1,
                "2" : self.jugador2,
                "3" : self.juagdor3,
                "4" : self.jugador4,
                "5" : self.quit
                } 

    def mostrar_menu(self):
        print("""
Bienvenidos a   " AirMayhem " 

Menu Ingreso al juego

Seleccione un Jugador

1 Jugador 1: 
2 Jugador 2:
3 Jugador 3:
4 Jugador 4: 
5 Salir

""")

    def run(self):
        '''Muestra el menú y responde a las elecciones.'''
        while True:
            self.mostrar_menu()
            eleccion = input("Escribe una opción: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
            else:
                print("{0} no es una elección válida".format(eleccion))

    def juagdor1(self, jugador1=None):
        if not jugador1:
            jugador1 = self.jugador
            jugador1.py
    def juagdor1(self, jugador2=None):
        if not jugador2:
            jugador2 = self.jugador
            jugador2.py
    def juagdor1(self, jugador3=None):
        if not jugador3:
            jugador3 = self.jugador
            jugador3.py
    def juagdor1(self, jugador4=None):
        if not jugador4:
            jugador4 = self.jugador
            jugador4.py
    def quit(self):
        print("Gracias, ha salido del juego ... ")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
