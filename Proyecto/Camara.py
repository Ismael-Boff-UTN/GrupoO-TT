
class Camara:
    def __init__(self, screen):
        self.x=0 #xy[0]
        self.y=0 #xy[1]
        self.screen=screen

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

    def dibujar(self,img,x,y):
        self.screen.blit(img, (x-self.x, y-self.y))


    def visible_en_camara(self,x,y,ancho,alto):
        if (x + ancho)<self.x or (y + alto)<self.y or x>(self.x+800) or y>(self.y+600):
            return False
        else:
            return True