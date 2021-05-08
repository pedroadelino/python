# Python
# Window App using PyQt6
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QPalette, QColor, QPalette
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QInputDialog
import sys

# global variables
app = QApplication(sys.argv)

# design global variables
window = QMainWindow()
label1 = QtWidgets.QLabel(window) # Put our label inside our main window
label2 = QtWidgets.QLabel(window) # Put our label inside our main window
label3 = QtWidgets.QLabel(window) # Put our label inside our main window
button1 = QtWidgets.QToolButton(window)
#button2 = QtWidgets.QPushButton()

def get_screensize():
    global app
    screen = app.primaryScreen()
    label1.setText('Screen: %s' % screen.name())
    size = screen.size()
    label2.setText('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    label3.setText('Available: %d x %d' % (rect.width(), rect.height()))

def get_windowsize():
    global window
    print(window.frameGeometry().width())
    print(window.frameGeometry().height())

def init_window(): # create our function
    global app, label1, button1, window
    app.setStyle('Fusion') 
    # android/ios apps run fullscreen by default
    window.setGeometry(500, 500, 500, 500) # for windows/mac/linux only
    window.setWindowTitle("PyQt6 Window app") # for windows/mac/linux only
    window.setStyleSheet("background-color: grey;")
    # label 1
    label1.setFixedWidth(500)
    label1.setFixedWidth(200)
    #label1.setText("") # change text in the label
    label1.move(10, 10) # change X,Y coordenates
    # label 2
    label2.setFixedWidth(500)
    label2.setFixedWidth(200)
    #label2.setText("") # change text in the label
    label2.move(10, 30) # change X,Y coordenates
    # label 3
    label3.setFixedWidth(500)
    label3.setFixedWidth(200)
    #label3.setText("") # change text in the label
    label3.move(10, 50) # change X,Y coordenates
    # button 1
    button1.setText('Get screen size')
    button1.move(150, 150) # change X,Y coordenates
    palette = button1.palette()
    role = button1.backgroundRole() #choose whatever you like
    palette.setColor(role, QColor('white'))
    button1.setPalette(palette)
    button1.setAutoFillBackground(True)
    button1.clicked.connect(get_screensize) # click event
    # button 2
    #button2.setText('Stop')
    #button2.move(250, 250) # change X,Y coordenates

    window.show() # load our window
    sys.exit(app.exec()) # end our app

init_window()
