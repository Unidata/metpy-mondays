# Metpy Monday
# 236 - Making a Wet Bulb Calculator App with Qt Part 2
# https://www.youtube.com/watch?v=LDV8dxpljLY

import metpy.calc as mpcalc
import sys

from metpy.units import units
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QDoubleSpinBox, QLCDNumber, QMainWindow, QPushButton, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle('Wet Bulb App')
		
		layout = QVBoxLayout()
		
		pressure = QDoubleSpinBox(minimum = 0, maximum = 2000)
		temperature = QDoubleSpinBox(minimum = -100, maximum = 100)
		dewpoint = QDoubleSpinBox(minimum = -100, maximum = 100)
		result = QLCDNumber()
		calculate_button = QPushButton('Calculate')
		
		widgets = [pressure, temperature, dewpoint, result, calculate_button]
		
		for w in widgets:
			layout.addWidget(w)
		
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)
		
		# Connecting signals and slots
		calculate_button.clicked.connect(lambda: self.calculate_wet_bulb(pressure.value(), temperature.value(), dewpoint.value()))
		
	def calculate_wet_bulb(self, p, t, td):
		wet_bulb = mpcalc.wet_bulb_temperature(p * units('hPa'), t * units('degC'), td * units('degC'))
		print(wet_bulb)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()


