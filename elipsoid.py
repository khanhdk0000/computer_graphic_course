import pygame
import numpy as np
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def elipsoid(a, b, c, latCount, longCount):
    latDelta = math.pi/ latCount
    longDelta = 2* math.pi/longCount
    verticies = []

    for i in range(latCount+1):
        lat = i*latDelta
        for j in range(longCount+1):
            lon = j*longDelta
            x = a*math.sin(lat)*math.cos(lon)
            y = b*math.sin(lat)*math.sin(lon)
            z = c * math.cos(lat)
            verticies.append([x,y,z])
    for i in range(latCount + 1):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(longCount+1):
            glVertex3fv(verticies[j+i*longCount])
            glVertex3fv(verticies[j+(i+1)*longCount])
        glEnd()

def main():
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
        elipsoid(4, 9, 16, 20,20)
        glRotatef(1, 0, 1, 0)
        pygame.display.flip()
        pygame.time.wait(10)

main()