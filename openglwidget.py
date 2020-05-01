from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class OpenGLWidget(QOpenGLWidget):
	def __init__(self, parent=None):
		QOpenGLWidget.__init__(self, parent)
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update)
		self.timer.start(0)

	def initializeGL(self):
	    glEnable(GL_DEPTH_TEST)
	    glEnable(GL_LIGHT0)
	    glEnable(GL_LIGHTING)
	    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
	    glEnable(GL_COLOR_MATERIAL)

	def paintGL(self):
		glMatrixMode(GL_PROJECTION)
		glClearColor(0.0, 0.0, 0.0, 0.0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glColor3f(1.0, 0.0, 0.0)
		glBegin(GL_TRIANGLES)
		glVertex3f(-0.5, -0.5, 0.0)
		glVertex3f(0.5, -0.5, 0.0)
		glVertex3f(0.0, 0.5, 0.0)
		glEnd()

	def resizeGL(self, w, h):
		glViewport(0, 0, w, h)