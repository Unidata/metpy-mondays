# Metpy Monday
# 237 - Making a Wet Bulb Calculator App with Qt Part 3
# https://www.youtube.com/watch?v=A5POmI2FgDE

import metpy.calc as mpcalc
import sys

from metpy.units import units
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QDoubleSpinBox, QLabel, QLCDNumber, QMainWindow, QPushButton, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle('Wet Bulb App')
		self.setFixedWidth(300)
		self.setFixedHeight(350)
		
		layout = QVBoxLayout()
		
		pressure = QDoubleSpinBox(minimum = 0, maximum = 2000, value = 1013.25)
		temperature = QDoubleSpinBox(minimum = -100, maximum = 100, value = 25)
		dewpoint = QDoubleSpinBox(minimum = -100, maximum = 100, value = 15)
		result = QLCDNumber()
		calculate_button = QPushButton('Calculate')
		pressure_label = QLabel('Pressure hPa')
		temperature_label = QLabel('Temperature degC')
		dewpoint_label = QLabel('Dewpoint degC')
		wbt_label = QLabel('Wet Bulb Temperature degC')
		
		widgets = [pressure_label, pressure, temperature_label, temperature,  dewpoint_label, dewpoint, wbt_label, result, calculate_button]
		
		for w in widgets:
			layout.addWidget(w)
		
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)
		
		# Connecting signals and slots
		calculate_button.clicked.connect(lambda: self.calculate_wet_bulb(pressure.value(), temperature.value(), dewpoint.value(), result))
		
	def calculate_wet_bulb(self, p, t, td, out):
		wet_bulb = mpcalc.wet_bulb_temperature(p * units('hPa'), t * units('degC'), td * units('degC'))
		out.display(wet_bulb.m)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()


