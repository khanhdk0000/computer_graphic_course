import pygame
import numpy as np
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def init(radius, latCount, longCount):
    latDelta = math.pi/ latCount
    longDelta = 2* math.pi/longCount
    verticies = []

    for i in range(latCount+1):
        lat = i*latDelta
        for j in range(longCount+1):
            lon = j*longDelta
            x = radius*math.sin(lat)*math.cos(lon)
            y = radius*math.sin(lat)*math.sin(lon)
            z = radius * math.cos(lat)
            verticies.append([x,y,z])
    return verticies
    
def sphere(verticies, latCount, longCount):
    
    for i in range(latCount+1):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(longCount+1):
            glVertex3fv(verticies[j+i*longCount])
            glVertex3fv(verticies[j+(i+1)*longCount])
        glEnd()

def main():
    lat, lon = 20, 20
    vertices = init(10, lat, lon)
    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )

    gluPerspective(45, (display[0] / display[1]), 0.1, 150.0)

    glTranslatef(0, 0.0, -50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        sphere(vertices,lat,lon)
        glRotatef(1, 1, 1, 0)
        pygame.display.flip()
        pygame.time.wait(10)

main()