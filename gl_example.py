#!/usr/bin/env python3

import sys
import numpy
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    # ondraw is called all the time
    # GL_COLOR_BUFFER_BIT: The buffers currently enabled for color writing.
    # GL_DEPTH_BUFFER_BIT: The depth buffer.
    # GL_ACCUM_BUFFER_BIT: The accumulation buffer.
    # GL_STENCIL_BUFFER_BIT: The stencil buffer.
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    # replace the current matrix with the identity matrix
    glLoadIdentity()
    # size: relative size of the teapot
    #glutWireTeapot(0.5)

    glPointSize(3.0)
    """
    GL_POINTS
	    Treats each vertex as a single point. Vertex n defines point n. N points are drawn.
    GL_LINES
    	Treats each pair of vertices as an independent line segment. Vertices 2n - 1 and 2n define
    	line n. N/2 lines are drawn.
    GL_LINE_STRIP
    	Draws a connected group of line segments from the first vertex to the last. Vertices n and
    	n+1 define line n. N - 1 lines are drawn.
    GL_LINE_LOOP
    	Draws a connected group of line segments from the first vertex to the last, then back to
    	the first. Vertices n and n + 1 define line n. The last line, however, is defined by vertices
    	N and 1. N lines are drawn.
    GL_TRIANGLES
    	Treats each triplet of vertices as an independent triangle. Vertices 3n - 2, 3n - 1, and 3n
    	define triangle n. N/3 triangles are drawn.
    GL_TRIANGLE_STRIP
    	Draws a connected group of triangles. One triangle is defined for each vertex presented after
    	the first two vertices. For odd n, vertices n, n + 1, and n + 2 define triangle n. For even n,
    	vertices n + 1, n, and n + 2 define triangle n. N - 2 triangles are drawn.
    GL_TRIANGLE_FAN
    	Draws a connected group of triangles. one triangle is defined for each vertex presented after
    	the first two vertices. Vertices 1, n + 1, n + 2 define triangle n. N - 2 triangles are drawn.
    GL_QUADS
    	Treats each group of four vertices as an independent quadrilateral. Vertices 4n - 3, 4n - 2,
    	4n - 1, and 4n define quadrilateral n. N/4 quadrilaterals are drawn.
    GL_QUAD_STRIP
    	Draws a connected group of quadrilaterals. One quadrilateral is defined for each pair of
    	vertices presented after the first pair. Vertices 2n - 1, 2n, 2n + 2, and 2n + 1 define
    	quadrilateral n. N/2 - 1 quadrilaterals are drawn. Note that the order in which vertices are
    	used to construct a quadrilateral from strip data is different from that used with independent
    	data.
    GL_POLYGON
    	Draws a single, convex polygon. Vertices 1 through N define this polygon.
    """
    glColor3f(numpy.random.uniform(), numpy.random.uniform(), numpy.random.uniform())
    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()

    glColor3f(numpy.random.uniform(), numpy.random.uniform(), numpy.random.uniform())
    glBegin(GL_POINTS)

    for x in numpy.arange(-5.0, 5.0, 0.01):
        glVertex2f(x, x * x * x)

    glEnd()

    glutSwapBuffers()                   # important for double buffering
    # radius: radius of the sphere
    # slice: number of subdivision around the z axis (similar to lines of longitude)
    # stacks: number of subdivision long the z axis (similar to lines of latitude)
    #glutWireSphere(0.5, 10, 40)

# initialization
glutInit(sys.argv)                      # initialize glut
"""
GLUT_RGBA
    Bit mask to select an RGBA mode window. This is the default if neither GLUT_RGBA nor GLUT_INDEX
    are specified.
GLUT_RGB
    An alias for GLUT_RGBA.
GLUT_INDEX
    Bit mask to select a color index mode window. This overrides GLUT_RGBA if it is also specified.
GLUT_SINGLE
    Bit mask to select a single buffered window. This is the default if neither GLUT_DOUBLE or
    GLUT_SINGLE are specified.
GLUT_DOUBLE
    Bit mask to select a double buffered window. This overrides GLUT_SINGLE if it is also specified.
GLUT_ACCUM
    Bit mask to select a window with an accumulation buffer.
GLUT_ALPHA
    Bit mask to select a window with an alpha component to the color buffer(s).
GLUT_DEPTH
    Bit mask to select a window with a depth buffer.
GLUT_STENCIL
    Bit mask to select a window with a stencil buffer.
GLUT_MULTISAMPLE
    Bit mask to select a window with multisampling support. If multisampling is not available, a
    non-multisampling window will automatically be chosen. Note: both the OpenGL client-side and
    server-side implementations must support the GLX_SAMPLE_SGIS extension for multisampling to be
    available.
GLUT_STEREO
    Bit mask to select a stereo window.
GLUT_LUMINANCE
    Bit mask to select a window with a ``luminance'' color model. This model provides the
    functionality of OpenGL's RGBA color model, but the green and blue components are not maintained
    in the frame buffer. Instead each pixel's red component is converted to an index between zero
    and glutGet(GLUT_WINDOW_COLORMAP_SIZE)-1 and looked up in a per-window color map to determine
    the color of pixels within the window. The initial colormap of GLUT_LUMINANCE windows is
    initialized to be a linear gray ramp, but can be modified with GLUT's colormap routines.
"""
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(480, 480)            # set window size
glutInitWindowPosition(0, 0)            # set window position
win = glutCreateWindow("Simple OpenGL") # create window with title
glutDisplayFunc(draw)                   # set draw function callback
gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
glutMainLoop()                          # start everything
