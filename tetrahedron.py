import pygame
import numpy as np
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def sphere():
    vertices = (
        (1, 1, 1),
        (1, -1, -1),
        (-1, -1, 1),
        (-1, 1, -1)
    )

    edges = (
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 3)
    )
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    frame = 0
    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )

    gluPerspective(45, (display[0] / display[1]), 0.1, 150.0)

    

    glTranslatef(0, 0.0, -50)
    glScalef(10,10,10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        sphere()
        glRotatef(1, 1, 1, 0.5)
        pygame.display.flip()
        pygame.time.wait(10)

main()