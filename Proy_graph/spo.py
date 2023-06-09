import sys
from typing import Any, Union, List
from time import time

import numpy as np
from time import time
import scipy.io as sio

from collections import deque
from multiprocessing import Queue

# @brief Buffer size for the data (number of points in the plot)
N_SAMPLES = 501
# @brief Update time of the plot, in ms
PLOT_UPDATE_TIME = 1
# @brief Point to update in each redraw
PLOT_UPDATE_POINTS = -1

class SPO():
    def __init__(self):
        self.dataR = deque([], maxlen = N_SAMPLES)
        self.dataIR = deque([], maxlen = N_SAMPLES)
        self.time = deque([], maxlen = N_SAMPLES)
        self.hr = 0

        # Spo2 signal initial parameters
        self.timestamp = 0.0
        self.ampR = 0.4  # amplitude for Red signal
        self.ampIR = 0.270  # amplitude for InfraRed signal
        self.minR = 1.45  # Displacement from zero for Red signal
        self.minIR = 1.45  # Displacement from zero for Red signal
        
        self.init_values(self.ampR, self.ampIR, 60, 100)
        self.spo2sl_change(100)
        self.timestamp = time()
    
    def ppg_parameters(self, minR, ampR, minIR, ampIR, t, HR):
        """
        Store the function of two signals - e.g PPG Red and Infrared channel signals
        We can also put here a sine, cosine, etc.
        """
        f = 60 *( 1 / 60)
         # Spo2 Red signal function
        self.sR = minR + ampR * (0.05 * np.sin(2 * np.pi * t * 3 * f) + 0.4 * np.sin(2 * np.pi * t * f) +
                                 0.22 * np.sin(2 * np.pi * t * 2 * f + 45))
        # self.sR = minR + ampR * (0.5 * np.sin(2 * np.pi * t * f) + 0.22 * np.sin(2 * np.pi * t * 2 * f + 40))
        # Spo2 InfraRed signal function
        self.sIR = minIR + ampIR * (0.05 * np.sin(2 * np.pi * t * 3 * f) + 0.4 * np.sin(2 * np.pi * t * f) +
                                    0.22 * np.sin(2 * np.pi * t * 2 * f + 45))
        return self.sR, self.sIR
    
    def spo2sl_change(self, value):
        """
        Change the value of the SpO2 when moving the slider.
        It also have the list of SpO2 values vs the R value
        """
        spo2value = value
        # sp02 list from 100 to 50
        sp02 = list(range(50, 101))[::-1]

        R = [0.50, 0.55, 0.60, 0.64, 0.66, 0.70, 0.71, 0.72, 0.73, 0.75, 0.76, 0.77, 0.78, 0.80, 0.81, 0.82, 0.83,
             0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.90, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.00,
             1.01, 1.00, 1.05, 1.11, 1.12, 1.16, 1.19, 1.25, 1.27, 1.32, 1.33, 1.35, 1.39, 1.43, 1.47, 1.52, 1.50]

        Ri = [0] * 51

        Ri[sp02.index(spo2value)] = R[sp02.index(spo2value)]

        # R-IR values & SpO2
        rR = [0.3, 0.4, 0.4, 0.4, 0.4, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.4, 0.4,
              0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,
              0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]

        IR = [1.0, 0.9, 0.7, 1.0, 0.9, 0.7, 0.7, 0.6, 0.6, 0.58, 0.57, 0.54, 0.52, 0.5, 0.5, 0.48, 0.47, 0.46, 0.45,
              0.445, 0.44, 0.43, 0.42, 0.39, 0.4, 0.39, 0.38, 0.38, 0.37, 0.35, 0.36, 0.35, 0.35, 0.34, 0.34, 0.34,
              0.33, 0.32, 0.32, 0.31, 0.3, 0.3, 0.3, 0.29, 0.29, 0.28, 0.28, 0.27, 0.27, 0.26, 0.25]

        self.ampR = rR[sp02.index(spo2value)]
        self.ampIR = IR[sp02.index(spo2value)]

        self.init_values(self.ampR, self.ampIR, self.hr, spo2value)


    def init_values(self, amp_r, amp_ir, heart_rate, spo):
        _hr = heart_rate
        t = np.linspace(0.2, 0.8, 100)
        _s_r, _s_ir = self.ppg_parameters(self.minR, amp_r, self.minIR, amp_ir, t, 200)

        data = sio.loadmat('curvesHB')
        x = data['x']

        _xhb_o2, _hb_02, _x_oxy_hb, _oxy_hb = x[0], x[1], x[2], x[3]

        spo2value = spo

        _hb_x = np.linspace((700 - spo2value), 1000, 100)
        _hb_y = x[5]
    
    def update_plot(self):
        """
        Updates the graphics in the plot.
        """
        # Getting heart rate
        hr = float(60)

        self.tPPG = time() - self.timestamp
        self.sR, self.sIR = self.ppg_parameters(self.minR, self.ampR, self.minIR, self.ampIR, self.tPPG, hr)

        # store data into variables 
        self.time.append(self.tPPG)
        self.dataR.append(self.sR)
        self.dataIR.append(self.sIR)
    
    def reset_buffers(self):
        self.dataR.clear()
        self.dataIR.clear()
    