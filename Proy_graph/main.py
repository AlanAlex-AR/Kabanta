### Graficas de deslegue continua  
# Autor: Alan 
# Informacion 
# https://www.pythonguis.com/tutorials/plotting-pyqtgraph/
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg 
import sys 
import numpy as np
import os
from data_test import ecg_signal
from window import Ui_window
Horiz_size = 800
Vert_size = 480 

class MainWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_window()
        self.ui.setupUi(self)
        
        ### Final de configuracion de los Widgets

        ### Codigo de main
        #Agregados al Layout vertical
        self.SignalGrahps()
        #Actualizacion de grafica
        self.su = 1
        self.timer = QtCore.QTimer()
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.Update_Grahp)
        self.timer.start()
        
        # User code starts Here 

    ### Funciones Agregados  
    def SignalGrahps(self):
        #Eje en x 
        self.x = list(range(100))
        np.zeros
        # Senales Derivaciones cardiacas
        self.der1 = [0 for i in self.x]
        self.der2 = [-1 for i in self.x]
        self.der3 = [-2 for i in self.x]
        #todo pen =
        self.data_line_der1 = self.ui.plt.plot(self.x,self.der1)
        self.data_line_der2 = self.ui.plt.plot(self.x,self.der2)
        self.data_line_der3 = self.ui.plt.plot(self.x,self.der3)
        # User code end Here 

    def Update_Grahp(self):
        self.su = self.su + 1
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.der1 = self.der1[1:]  # Remove the first
        self.der1.append(ecg_signal[self.su][0])  # Add a new random value.
        

        self.der2 = self.der2[1:]  # Remove the first
        self.der2.append(ecg_signal[self.su][1]-1)  # Add a new random value.

        self.der3 = self.der3[1:]  # Remove the first
        self.der3.append(ecg_signal[self.su][2]-2)  # Add a new random value.
        
        self.data_line_der1.setData(self.x, self.der1)  # Update the data.
        self.data_line_der2.setData(self.x, self.der2)
        self.data_line_der3.setData(self.x, self.der3)
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())