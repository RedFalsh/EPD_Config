from PyQt5 import  QtGui
  
from matplotlib.backends.backend_qt4agg import  FigureCanvasQTAgg as FigureCanvas  
  

from matplotlib.figure import Figure  
  
import numpy as np  
  
from array import array  
  
import time  
  
import random  
  
import threading  
  
from datetime import datetime  
  
from matplotlib.dates import  date2num, MinuteLocator, SecondLocator, DateFormatter  
  
   
  
X_MINUTES = 1  
  
Y_MAX = 100  
  
Y_MIN = 1  
  
INTERVAL = 1  
  
MAXCOUNTER = int(X_MINUTES * 60/ INTERVAL)  
  
class MplCanvas(FigureCanvas):  
  
    def __init__(self):  
  
        self.fig = Figure()  
  
        self.ax = self.fig.add_subplot(111)  
  
        FigureCanvas.__init__(self, self.fig)  
  
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)  
  
        FigureCanvas.updateGeometry(self)  
  
        self.ax.set_xlabel("time of data generator")  
  
        self.ax.set_ylabel('random data value')  
  
        self.ax.legend()  
  
        self.ax.set_ylim(Y_MIN,Y_MAX)  
  
        self.ax.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator  
  
        self.ax.xaxis.set_minor_locator(SecondLocator([10,20,30,40,50])) # every 10 second is a minor locator  
  
        self.ax.xaxis.set_major_formatter( DateFormatter('%H:%M:%S') ) #tick label formatter  
  
        self.curveObj = None # draw object  
  
    def plot(self, datax, datay):  
  
        if self.curveObj is None:  
  
            #create draw object once  
  
            self.curveObj, = self.ax.plot_date(np.array(datax), np.array(datay),'bo-')  
  
        else:  
  
            #update data of draw object  
  
            self.curveObj.set_data(np.array(datax), np.array(datay))  
  
            #update limit of X axis,to make sure it can move  
  
            self.ax.set_xlim(datax[0],datax[-1])  
  
        ticklabels = self.ax.xaxis.get_ticklabels()  
  
        for tick in ticklabels:  
  
            tick.set_rotation(25)  
  
        self.draw()  