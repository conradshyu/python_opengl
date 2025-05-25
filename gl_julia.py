#!/usr/bin/env python3

from __future__ import absolute_import, division, print_function, unicode_literals
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy

class Rosette():
    def __init__(self, n = 25, radius = 95):
        self.N = 25
        self.RADIUS = 95

    def reshapeFun(self, w, h):
        glViewport(int((w - h) / 2), 0, h, h) if w > h else glViewport(0, int((h - w) / 2), w, w)

    def displayFun(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(numpy.random.uniform(), numpy.random.uniform(), numpy.random.uniform())
        xpts = [self.RADIUS * math.sin(2.0 * math.pi * i / self.N) for i in range(0, self.N)]
        ypts = [self.RADIUS * math.cos(2.0 * math.pi * i / self.N) for i in range(0, self.N)]

        glBegin(GL_LINE_STRIP)

        for i in range(0, self.N):
            for j in range(i, self.N):
                glVertex2f(xpts[i], ypts[i])
                glVertex2f(xpts[j], ypts[j])
        glEnd()
        glFlush()

    def Run(self, w = 400, h = 400):
        glutInit()
        glutInitWindowSize(w, h)
        glutCreateWindow("Rosette")
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutDisplayFunc(self.displayFun)
        glutReshapeFunc(self.reshapeFun)

        glClearColor(1.0, 1.0, 1.0, 0.0)
        glColor3f(0.0, 0.0, 0.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-100, 100, -100, 100)
        glutMainLoop()

if __name__ == '__main__':
    r = Rosette(400, 400)
    r.Run()
