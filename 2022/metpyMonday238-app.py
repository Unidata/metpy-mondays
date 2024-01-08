# Metpy Monday
# 238 - Making a Wet Bulb Calculator App with Qt Part 4
# https://www.youtube.com/watch?v=GBxu8SuBPW0

import metpy.calc as mpcalc
import sys

from metpy.units import units
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QAction, QApplication, QDoubleSpinBox, QLabel, QLCDNumber, QMainWindow, QPushButton, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle('Wet Bulb App')
		self.setFixedWidth(300)
		self.setFixedHeight(350)
		
		self.use_imperial_units = False
		
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
		
		button_action = QAction('&Imperial Units', self)
		button_action.setStatusTip('Change Units')
		button_action.toggled.connect(lambda: self.on_unit_button_click(button_action, temperature_label, dewpoint_label, wbt_label))
		button_action.setCheckable(True)
		
		menu = self.menuBar()
		file_menu = menu.addMenu('&File')
		file_menu.addAction(button_action)
		
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)
		
		# Connecting signals and slots
		calculate_button.clicked.connect(lambda: self.calculate_wet_bulb(pressure.value(), temperature.value(), dewpoint.value(), result))
		
	def on_unit_button_click(self, s, temperature_label, dewpoint_label, wbt_label):
		if s.ischecked():
			temperature_label.setText('Temperature degF')
			dewpoint_label.setText('Dewpoint degF')
			wbt_label.setText('Wet Bulb Temperature degF')
			self.use_imperial_units = True
		else:
			temperature_label.setText('Temperature degC')
			dewpoint_label.setText('Dewpoint degC')
			wbt_label.setText('Wet Bulb Temperature degC')
			self.use_imperial_units = False
		
		
	def calculate_wet_bulb(self, p, t, td, out):
		u = units('degC')
		if self.use_imperial_units:
			u = units('degF')
		wet_bulb = mpcalc.wet_bulb_temperature(p * units('hPa'), t * u, td * u)
		out.display(wet_bulb.to(u).m)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()


