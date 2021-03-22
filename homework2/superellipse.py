from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math

#Width and height of the eclipse
W = 1.0
H = 1.0
N = 0.1

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.5, 1.5, -1.5, 1.5, 0.0, 1.0)

def keyPressed(*args):
    global N
    if args[0] == GLUT_KEY_UP and N < 1.91:
        N += 0.1
    if args[0] == GLUT_KEY_DOWN and N > 0.1:
        N -= 0.1
    # if args[0] == GLUT_KEY_RIGHT and W < 0.9:
    #     W += 0.1
    # if args[0] == GLUT_KEY_LEFT and W >= 0.2:
    #     W -= 0.1
    print(N)


def draw_coor():
    """
    Draw the 2D (Oxy) coordinate.
    """
    glBegin(GL_LINE_STRIP)

    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-1.5, 0.0)
    glVertex2f(1.5, 0.0)

    glEnd()

    glBegin(GL_LINE_STRIP)

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.0, -1.5)
    glVertex2f(0.0, 1.5)

    glEnd()

def draw_eclipse():
    """
    Draw the eclipse.
    """

    glBegin(GL_LINE_LOOP)
    glColor3f(1.0, 1.0, 1.0)
    for t in np.arange(0, 2 * math.pi + math.pi / 100, math.pi / 100):
        x = W * math.cos(t) * abs(math.cos(t)**(2/N - 1))
        y = H * math.sin(t) * abs(math.sin(t)**(2/N - 1))
        glVertex2f(x, y)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    draw_coor()
    draw_eclipse()
    
    glFlush()

def main():
    global window 

    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(480, 480)
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Line")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutSpecialFunc(keyPressed)
    InitGL()
    glutMainLoop()

if __name__ == "__main__":
    main()