from graphics import *


class Particle:

    def __init__(self,velx,vely,cx,cy,R):
        self.vx = float(velx/0.175)
        self.vy = float(vely/0.175)
        self.head = Circle(Point(cx,cy),R)

    def Drw(self,win):
        self.head.draw(win)

    def filll (self,color):
        self.head.setFill(color)

    def Mve (self):
        self.head.move(self.vx,self.vy)

    def getVelx(self):
        return self.vx

    def getVely(self):
        return self.vy

    def setVelx(self,newvx):
        self.vx = newvx

    def setVely(self,newvy):
        self.vy = newvy

    def getNormVel(self):
        return self.vx*self.vx+self.vy*self.vy

    def getR(self):
        return self.head.getRadius()

    def gitx(self):
        return self.head.getCenter().getX()

    def gity(self):
        return self.head.getCenter().getY()
