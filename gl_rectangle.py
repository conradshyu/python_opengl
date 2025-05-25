#!/usr/bin/env python3

from OpenGL.GLUT import *
from OpenGL.GL import *
import sys
import numpy

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_QUADS)

    for i in range(0, 40):
        glColor3f(numpy.random.uniform(), numpy.random.uniform(), numpy.random.uniform())
        x, y = (numpy.random.uniform(), numpy.random.uniform())
        glVertex3f(x, y, 0.0)
        glVertex3f(x, -1.0 * y, 0.0)
        glVertex3f(-1.0 * x, -1.0 * y, 0.0)
        glVertex3f(-1.0 * x, y, 0.0)

    glEnd()
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400, 400)
glutCreateWindow("Rectangle")
glutDisplayFunc(display)
glutMainLoop()
