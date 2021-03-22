from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0) # background color
    glColor3f(0.0, 0.0, 1.0) # shape color
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 4.0, -4.0, 2.0, -1.0, 1.0) # tam phim


def drawfigure():
    glBegin(GL_POLYGON)
    glVertex2f(-2.0, 0.0)
    glVertex2f(-2.0, 2.0)
    glVertex2f(0.0, 2.0)
    glVertex2f(0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0, -4.0)
    glVertex2f(2.0, 0.0)
    glVertex2f(4.0, -4.0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glViewport(320, 240, 240, 240)
    drawfigure()

    # second quadrant
    glViewport(0, 240, 240, 240)
    drawfigure()

    glViewport(320, 0, 240, 240)
    drawfigure()

    glViewport(0, 0, 240, 240)
    drawfigure()


    glFlush()


# sierpinski
def sierpinski_init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 50.0, 0.0, 50.0)
    glMatrixMode(GL_MODELVIEW)


def sierpinski():
    vertices = [(0.0, 0.0), (25.0, 50.0), (50.0, 0.0)]
    point = [7.5, 5.0]
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    for i in range(500000):
        j = random.randint(0, 65535) % 3
        point[0] = (point[0] + vertices[j][0])/2.0
        point[1] = (point[1] + vertices[j][1])/2.0
        glVertex2fv(point)
    glEnd()
    glFlush()

# vietnam flag
class Point2d:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

pi = math.pi
R = 2
pointArr = []

def flag_init():
    # calculatePoint()
    glClearColor(1.0, 0.0, 0.0, 1.0)
    glColor3f(0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-4.5, 4.5, -3.0, 3.0, -1.0, 1.0)


def calculatePoint():
    
    for i in range(5):
        point = Point2d(0, 0)
        point.x = R*math.cos(pi / 2 + i* 2 * pi / 5)
        point.y = R*math.sin(pi / 2 + i* 2 * pi / 5)
        pointArr.append(point)
    
    pointArr.append(lineIntersection(pointArr[0], pointArr[2], pointArr[1], pointArr[4]))
    pointArr.append(lineIntersection(pointArr[0], pointArr[2], pointArr[1], pointArr[3]))
    pointArr.append(lineIntersection(pointArr[1], pointArr[3], pointArr[2], pointArr[4]))
    pointArr.append(lineIntersection(pointArr[2], pointArr[4], pointArr[0], pointArr[3]))
    pointArr.append(lineIntersection(pointArr[0], pointArr[3], pointArr[1], pointArr[4]))

def drawPoint(point):
    glBegin(GL_POINTS)
    glVertex2f(point.x, point.y)
    glEnd()

def lineIntersection(p1, p2, p3, p4):

    res = Point2d(0, 0)
    A1 = (p2.y - p1.y) / (p2.x - p1.x)
    B1 = p1.y - A1*p1.x

    A2 = (p4.y - p3.y) / (p4.x - p3.x)
    B2 = p3.y - A2*p3.x

    res.x = (B2 - B1) / (A1 - A2)
    res.y = A1*res.x + B1
    return res
 

def flag():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5)
    calculatePoint()
    # for i in range(10):
    #     drawPoint(pointArr[i])

    # glLineWidth(4)
    # glBegin(GL_LINE_LOOP)
    glColor3f(1, 1, 0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    # glBegin(GL_POLYGON)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    glVertex2f(pointArr[0].x, pointArr[0].y)
    glVertex2f(pointArr[5].x, pointArr[5].y)
    glVertex2f(pointArr[1].x, pointArr[5].y)
    glVertex2f(pointArr[6].x, pointArr[6].y)
    glVertex2f(pointArr[2].x, pointArr[2].y)
    glVertex2f(pointArr[7].x, pointArr[7].y)
    glVertex2f(pointArr[3].x, pointArr[3].y)
    glVertex2f(pointArr[8].x, pointArr[8].y)
    glVertex2f(pointArr[4].x, pointArr[4].y)
    glVertex2f(pointArr[9].x, pointArr[9].y)
    glVertex2f(pointArr[0].x, pointArr[0].y)
    glEnd()


    glFlush()



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 400)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Simple")
    glutDisplayFunc(flag)

    # init()
    flag_init()
    glutMainLoop()

if __name__ == "__main__":
        main() 