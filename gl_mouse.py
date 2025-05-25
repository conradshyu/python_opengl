#!/usr/bin/env python3

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy

class MouseDraw():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.points = []

    def displayFun(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_LINE_STRIP)
        glColor3f(numpy.random.uniform(), numpy.random.uniform(), numpy.random.uniform())

        for p in self.points:
            glVertex2i(p["x"], p["y"])

        glEnd()
        glFlush()

    def mouseFun(self, button, state, x, y):
        # left click to connect two points and draw a line
        if (button == GLUT_LEFT_BUTTON) and (state == GLUT_DOWN):
            self.points.append({"x": x, "y": self.h - y})

        # right click to remove the last line
        if (button == GLUT_RIGHT_BUTTON) and (state == GLUT_DOWN):
            if len(self.points) != 0:
                self.points = self.points[:-1]

        glutPostRedisplay()

    def Run(self):
        glutInit()
        glutInitWindowSize(self.w, self.h)
        glutCreateWindow("Polyline")
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutDisplayFunc(self.displayFun)
        glutMouseFunc(self.mouseFun)

        glClearColor(1.0, 1.0, 1.0, 0.0)
        glColor3f(0.0, 0.0, 0.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0.0, self.w, 0.0, self.h)
        glutMainLoop()

if __name__ == '__main__':
    r = MouseDraw(800, 600)
    r.Run()
