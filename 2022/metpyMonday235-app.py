# Metpy Monday
# 235 - Making a Wet Bulb Calculator App with Qt Part 1
# https://www.youtube.com/watch?v=QvXz30S7vis

import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QDoubleSpinBox, QLCDNumber, QMainWindow, QPushButton, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle('Wet Bulb App')
		
		layout = QVBoxLayout()
		widgets = [QDoubleSpinBox(), QDoubleSpinBox(), QDoubleSpinBox(), QLCDNumber(), QPushButton('Calculate')]
		
		for w in widgets:
			layout.addWidget(w)
		
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()


