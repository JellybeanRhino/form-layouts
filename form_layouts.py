# form_layouts.py
# Rhiannon MacCreadie
# 04/05/2022
# Practice making form layouts for class

# Intialising
import sys
from PySide6 import QtWidgets

app = QtWidgets.QApplication()

window = QtWidgets.QMainWindow()
window.setWindowTitle('QForm')
window.setGeometry(500, 200, 600, 300)

window.setCentralWidget(QtWidgets.QWidget())
# Define Layouts
# Main Layout
h_layout = QtWidgets.QHBoxLayout()
# Sub Layout
form_layout = QtWidgets.QFormLayout()
right_layout = QtWidgets.QVBoxLayout()

# Set main layout
window.centralWidget().setLayout(h_layout)

# Define Widgets
right_widget = QtWidgets.QWidget()
form_widget = QtWidgets.QWidget()

# Set Sub Layouts
right_widget.setLayout(right_layout)
form_widget.setLayout(form_layout)

# Left Side Widgets
# Create a form
# String Answers
form_layout.addRow("First Name", QtWidgets.QLineEdit())
form_layout.addRow("Last Name", QtWidgets.QLineEdit())
form_layout.addRow("Address", QtWidgets.QLineEdit())
form_layout.addRow("City", QtWidgets.QLineEdit())
# Checkbox Answer
form_layout.addRow("Child", QtWidgets.QCheckBox())

# Add widget to Main widget
h_layout.addWidget(form_widget)

# Right Side Widgets
# Top Calender
departure_date_calendar = QtWidgets.QCalendarWidget()
right_layout.addWidget(departure_date_calendar)
# Bottom Calender
arrival_date_calendar = QtWidgets.QCalendarWidget()
right_layout.addWidget(arrival_date_calendar)

# Add right side widgets to main widget
h_layout.addWidget(right_widget)

# Output Code
window.show()

app.exec_()