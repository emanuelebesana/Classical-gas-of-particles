from gasclass import *
import time
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation
import random



def moveAll (particles):
    for part in particles:
        part.Mve()


def checkSides (particles, win):
    for part in particles:
        if part.gitx() >= win.getWidth()-part.getR() or part.gitx() <= part.getR():
            part.setVelx(-part.getVelx())
            while part.gitx() >= win.getWidth()-part.getR() or part.gitx() <= part.getR():
                part.Mve()
        if part.gity() >= win.getHeight()-part.getR() or part.gity() <= part.getR():
            part.setVely(-part.getVely())
            while part.gity() >= win.getHeight()-part.getR() or part.gity() <= part.getR():
                part.Mve()


def checkCollisions(particles):
    for part in particles:
        for single in particles:
            if math.sqrt( (single.gitx()-part.gitx())*(single.gitx()-part.gitx()) + (single.gity()- part.gity())* (single.gity()- part.gity()) ) <= (single.getR() + part.getR()) and math.sqrt( (single.gitx()-part.gitx())*(single.gitx()-part.gitx()) + (single.gity()- part.gity())* (single.gity()- part.gity()) ) != 0:


                prodscal = (part.getVelx()-single.getVelx())*(part.gitx()-single.gitx()) + (part.getVely()-single.getVely())*(part.gity()-single.gity())
                norm = (single.gitx()-part.gitx())*(single.gitx()-part.gitx())+(single.gity()-part.gity())*(single.gity()-part.gity())

                single.setVelx( single.getVelx() - float((prodscal/norm))*(single.gitx()-part.gitx()))
                single.setVely( single.getVely() - float((prodscal/norm))*(single.gity()-part.gity()))

                part.setVelx(part.getVelx() - float((prodscal/norm))*(part.gitx()-single.gitx()))
                part.setVely(part.getVely() - float((prodscal/norm))*(part.gity()-single.gity()))


                while math.sqrt( (single.gitx()-part.gitx())*(single.gitx()-part.gitx()) + (single.gity()- part.gity())* (single.gity()- part.gity()) ) <= (single.getR() + part.getR()) <= (single.getR() + part.getR()):
                    single.Mve()
                    part.Mve()


def getVelocities(particles):
    data =[]
    for i in particles:
        data.append( math.sqrt( i.getVelx()*i.getVelx() + i.getVely()*i.getVely() ) )
    return data


def setVelocities(particles,dt):
    for part in particles:
        part.setVelx(float(part.getVelx()/dt))
        part.setVely(float(part.getVely()/dt))

def getRms(particles):
    acc = 0
    for part in particles:
        acc += part.getNormVel()
    return float(acc/len(particles))

def getTemperature(particles,rms):
    return rms*2.07e-21/(3*1.38e-23)
