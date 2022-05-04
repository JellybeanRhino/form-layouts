# form_layouts.py
# Rhiannon MacCreadie
# 04/05/2022
# 

# Intialising
import sys
from PySide6 import QtWidgets

app = QtWidgets.QApplication()

window = QtWidgets.QMainWindow()
window.setWindowTitle('QForm')
window.setGeometry(500, 200, 600, 300)

window.setCentralWidget(QtWidgets.QWidget())

# Create Widget


h_layout = QtWidgets.QHBoxLayout()
form_layout = QtWidgets.QFormLayout()
right_layout = QtWidgets.QVBoxLayout()
window.centralWidget().setLayout(h_layout)

right_widget = QtWidgets.QWidget()
form_widget = QtWidgets.QWidget()

right_widget.setLayout(right_layout)
form_widget.setLayout(form_layout)

form_layout.addRow("First Name", QtWidgets.QLineEdit())
form_layout.addRow("Last Name", QtWidgets.QLineEdit())
form_layout.addRow("Address", QtWidgets.QLineEdit())
form_layout.addRow("City", QtWidgets.QLineEdit())
form_layout.addRow("Child", QtWidgets.QCheckBox())

h_layout.addWidget(form_widget)


departure_date_calendar = QtWidgets.QCalendarWidget()
right_layout.addWidget(departure_date_calendar)
arrival_date_calendar = QtWidgets.QCalendarWidget()
right_layout.addWidget(arrival_date_calendar)

h_layout.addWidget(right_widget)

window.setLayout(h_layout)

window.show()

app.exec_()