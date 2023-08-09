import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication,QWidget
import requests
import numpy
import pandas

class VentanaVacia(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        
    def inicializarUI(self):
        self.setGeometry(250,250,250,250)
        self.setWindowTitle("Ventanuken")
        self.show()


if __name__=='__main__': 
    app=QApplication(sys.argv) 
    ventana=VentanaVacia()
    sys.exit(app.exec())
