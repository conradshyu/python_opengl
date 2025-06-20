#!/usr/bin/env python3

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

def initFun():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(0.0,0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 640.0, 0.0, 480.0)

def displayFun():
    x = [0.0, 640.0, 320.0]
    y = [0.0, 0.0, 480.0]
    curx = 0
    cury = 320

    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    glVertex2f(curx, cury)

    for i in range(0,500000):
        idx = random.randint(0, 2)
        curx = (curx + x[idx]) / 2.0
        cury = (cury + y[idx]) / 2.0
        glVertex2f(curx, cury)

    glEnd()
    glutSwapBuffers()    # important for double buffering

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640, 480)
    glutCreateWindow("Sierpinski")
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
