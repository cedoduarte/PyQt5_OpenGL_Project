from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from openglwidget import OpenGLWidget

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		self.openglwidget = OpenGLWidget(self)
		self.setCentralWidget(self.openglwidget)
		self.setWindowTitle("Test OpenGL")
		self.setGeometry(0, 0, 1000, 1000)