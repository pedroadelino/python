# Python
# Window App using PyQt6
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
def init_window(): # create our function
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(500, 500, 500, 500)
    window.setWindowTitle("PyQt6 Window app")
    label = QtWidgets.QLabel(window) # Put our label inside our main window
    label.setText("Hello") # change text in the label
    label.move(50, 50) # change X,Y coordenates
    window.show() # load our window
    sys.exit(app.exec()) # end our app
init_window()