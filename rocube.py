import pygame
from pygame.locals import *
import math
from OpenGL.GL import *
from OpenGL.GLU import *

pi = math.pi

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()

def DrawEllipsoid(uiStacks, uiSlices, fA, fB, fC):
    tStep = pi / uiSlices
    sStep = pi / uiStacks
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    t = -pi / 2
    s = -pi
    while( t <= pi / 2 + 0.0001):
        glBegin(GL_TRIANGLE_STRIP)
        while( s <= pi + 0.0001):
            glVertex3f(
                fA * math.cos(t) * math.cos(s),
                fB * math.cos(t) * math.sin(s),
                fC * math.sin(t),
            )
            glVertex3f(
                fA * math.cos(t + tStep) * math.cos(s),
                fB * math.cos(t + tStep) * math.sin(s),
                fC * math.sin(t + tStep),
            )
            s+= sStep
        glEnd()
        t += tStep

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) 

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 1, 2, 3)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        DrawEllipsoid(10, 10, 40, 90, 250)
        pygame.display.flip()
        pygame.time.wait(10)

main()