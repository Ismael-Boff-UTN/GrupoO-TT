
class Camara:
    def __init__(self):
        self.x=0
        self.y=0


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