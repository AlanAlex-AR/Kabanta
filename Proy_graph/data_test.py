import sys 
import numpy as np
import os
import wfdb
import scipy.signal
import neurokit2 as nk
from collections import deque
import pandas as pd
#record = wfdb.rdrecord('Proy_graph/Signals/AFL_08',channels=[0],sampfrom=0)
record = wfdb.rdrecord('Signals/430_C_SBR_880_7s_frag',channels=[0],sampfrom=0)
signal = record.p_signal
ecg_signal = signal.tolist()
#print(ecg_signal)
save = deque([])
print(np.size(ecg_signal))
for i in range(302):
    save.append(ecg_signal[i][0])
save = list(save)
print(save)

# record_name = 'Proy_graph/Signals/cu01'
# record_name = 'Signals/418_C_VTHR_1074_9s_frag'
# annotation = 'atr'  # Tipo de anotación

# # Lee las anotaciones del archivo .atr
# annotation_data = wfdb.rdann(record_name, annotation)

# # Obtiene los códigos de anotación y las marcas de tiempo
# annotation_codes = annotation_data.aux_note
# annotation_timestamps = annotation_data.sample

# print(annotation_codes)
# print(annotation_timestamps)

#Cambios de Codigo Main, Separacion de StyleSheet, y agregado de Generacion de senales con neurokit
class obtainSignals():
    @staticmethod
    def generateSignals(id_1):
        ecg12 = nk.ecg_simulate(duration=10, method="multileads",sampling_rate=50,heart_rate=id_1)
        return ecg12
    
    @staticmethod
    def generate_rsp():
        rsp = nk.rsp_simulate(duration=10, respiratory_rate=100, method="sinusoidal")
        return rsp

        



Atrialfibrillation = [-0.2449957272254892, -0.2449957272254892, -0.2500138857348753, -0.2449957272254892, -0.24000640870753634,
-0.2449957272254892, -0.2550032042528282, -0.2650106812801672, -0.26999999979812006, -0.2650106812801672, 
-0.2500138857348753, -0.26999999979812006, -0.26999999979812006, -0.27498931831607293, -0.25999252277078105, 
-0.24000640870753634, -0.23498825019815023, -0.23498825019815023, -0.24000640870753634, -0.2650106812801672, 
-0.2500138857348753, -0.2449957272254892, -0.23498825019815023, -0.2449957272254892, -0.2550032042528282, 
-0.25999252277078105, -0.25999252277078105, -0.2550032042528282, -0.2449957272254892, -0.2449957272254892, 
-0.25999252277078105, -0.2650106812801672, -0.2449957272254892, -0.22999893168019736, -0.21999145465285835, 
-0.21500213613490549, -0.21001281761695262, -0.21999145465285835, -0.21500213613490549, -0.1949871820802275, 
-0.18999786356227463, -0.18999786356227463, -0.2000053405896136, -0.21001281761695262, -0.20499465910756648, 
-0.17999038653493563, -0.1700117494990299, -0.16499359098964378, -0.16499359098964378, -0.13499999989906003, 
-0.06999465920850645, 0.019986114063244735, 0.13001068138110716, 0.2250096131622445, 0.33500534048867364, 
0.42498611376042483, 0.5500074766235792, 0.6600032039500083, 0.7500128172131928, 0.8249967949396521, 
0.8549903860302358, 0.8200074764216992, 0.7150010676132229, 0.554996795141532, 0.37999572712454927, 
0.17999038653493563, -0.00498931851795287, -0.1399893184170129, -0.2250096131622445, -0.28000747682545907, 
-0.30501174939808995, -0.2999935908887038, -0.27498931831607293, -0.24000640870753634, -0.21999145465285835, 
-0.2250096131622445, -0.23498825019815023, -0.2550032042528282, -0.26999999979812006, -0.28000747682545907, 
-0.28499679534341193, -0.28499679534341193, -0.2899861138613648, -0.2999935908887038, -0.30501174939808995, 
-0.3149903864339957, -0.3149903864339957, -0.30501174939808995, -0.30501174939808995, -0.30501174939808995, 
-0.30501174939808995, -0.3149903864339957, -0.30501174939808995, -0.2999935908887038, -0.2999935908887038, 
-0.2899861138613648, -0.29500427237075094, -0.2999935908887038, -0.29500427237075094, -0.2899861138613648, 
-0.2899861138613648, -0.29500427237075094, -0.29500427237075094, -0.2999935908887038, -0.2899861138613648, 
-0.2899861138613648, -0.28499679534341193, -0.28499679534341193, -0.2899861138613648, -0.2899861138613648, 
-0.28000747682545907, -0.28000747682545907, -0.27498931831607293, -0.26999999979812006, -0.27498931831607293, 
-0.28000747682545907, -0.2650106812801672, -0.2449957272254892, -0.2500138857348753, -0.2449957272254892, 
-0.2449957272254892, -0.2449957272254892, -0.23498825019815023, -0.21500213613490549, -0.2000053405896136, 
-0.20499465910756648, -0.21500213613490549, -0.20499465910756648, -0.1949871820802275, -0.18999786356227463, 
-0.18500854504432176, -0.17999038653493563, -0.1949871820802275, -0.1949871820802275, -0.17999038653493563, 
-0.16499359098964378, -0.15498611396230477, -0.1499967954443519, -0.1499967954443519, -0.14500747692639904, 
-0.12000320435376817, -0.10500640880847631, -0.10500640880847631, -0.07501281771789257, -0.09000961326318445, 
-0.09499893178113732, -0.08000213623584544, -0.06999465920850645, -0.06500534069055358, -0.07501281771789257, 
-0.09000961326318445, -0.09998825029909018, -0.09000961326318445, -0.08499145475379832, -0.08499145475379832, 
-0.09000961326318445, -0.1150138858358153, -0.13499999989906003, -0.13499999989906003, -0.13499999989906003, 
-0.1399893184170129, -0.1499967954443519, -0.16499359098964378, -0.18500854504432176, -0.18500854504432176, 
-0.18500854504432176, -0.18500854504432176, -0.1949871820802275, -0.20499465910756648, -0.2250096131622445, 
-0.2250096131622445, -0.2250096131622445, -0.23498825019815023, -0.2250096131622445, -0.24000640870753634, 
-0.2449957272254892, -0.23498825019815023, -0.22999893168019736, -0.2250096131622445, -0.2250096131622445, 
-0.23498825019815023, -0.2449957272254892, -0.24000640870753634, -0.22999893168019736, -0.22999893168019736, 
-0.24000640870753634, -0.2449957272254892, -0.23498825019815023, -0.2250096131622445, -0.21999145465285835, 
-0.21999145465285835, -0.21999145465285835, -0.2250096131622445, -0.24000640870753634, -0.21999145465285835, 
-0.21001281761695262, -0.1949871820802275, -0.18500854504432176, -0.2000053405896136, -0.18500854504432176, 
-0.18500854504432176, -0.17500106801698276, -0.1700117494990299, -0.17999038653493563, -0.18500854504432176, 
-0.18999786356227463, -0.17999038653493563, -0.17999038653493563, -0.17500106801698276, -0.18500854504432176, 
-0.18999786356227463, -0.20499465910756648, -0.1949871820802275, -0.18999786356227463, -0.18999786356227463, 
-0.18999786356227463, -0.2000053405896136, -0.1949871820802275, -0.2000053405896136, -0.2000053405896136, 
-0.1949871820802275, -0.2000053405896136, -0.21500213613490549, -0.21999145465285835, -0.21500213613490549, 
-0.1949871820802275, -0.1949871820802275, -0.18999786356227463, -0.20499465910756648, -0.21500213613490549, 
-0.21001281761695262, -0.2000053405896136, -0.18999786356227463, -0.20499465910756648, -0.21500213613490549, 
-0.21999145465285835, -0.21999145465285835, -0.20499465910756648, -0.18999786356227463, -0.21500213613490549, 
-0.21500213613490549, -0.21999145465285835, -0.21001281761695262, -0.2000053405896136, -0.1949871820802275, 
-0.21500213613490549, -0.21500213613490549, -0.2250096131622445, -0.2250096131622445, -0.21500213613490549, 
-0.21001281761695262, -0.21001281761695262, -0.21500213613490549, -0.21500213613490549, -0.21500213613490549, 
-0.21001281761695262, -0.21001281761695262, -0.21001281761695262, -0.21999145465285835, -0.21999145465285835, 
-0.21999145465285835, -0.21999145465285835, -0.21500213613490549, -0.21500213613490549, -0.22999893168019736, 
-0.23498825019815023, -0.22999893168019736, -0.21999145465285835, -0.21999145465285835, -0.21500213613490549, 
-0.2250096131622445, -0.22999893168019736, -0.21500213613490549, -0.21999145465285835, -0.21999145465285835, 
-0.2250096131622445, -0.22999893168019736, -0.22999893168019736, -0.22999893168019736, -0.21500213613490549, 
-0.20499465910756648, -0.21999145465285835, -0.21999145465285835, -0.22999893168019736, -0.21999145465285835, 
-0.2000053405896136, -0.18999786356227463, -0.18999786356227463, -0.1949871820802275, -0.2000053405896136, 
-0.18500854504432176, -0.15498611396230477, -0.13499999989906003, -0.13001068138110716, -0.10999572732642918, 
-0.07501281771789257, 0.00498931851795287, 0.09499893178113732, 0.18999786356227463, 0.28499679534341193, 
0.37999572712454927, 0.4899914544509784] 

Atrialflutter = [-0.2549888601526184, -0.2800256348984665, -0.2800256348984665, -0.2649897756847065, 
-0.23002105723802604, -0.21001922617384988, -0.24002197277011414, -0.2500228883022022, -0.2449879446205303,
-0.23002105723802604, -0.22002014170593798, -0.22002014170593798, -0.2500228883022022, -0.2449879446205303,
-0.2449879446205303, -0.24002197277011414, -0.2349870290884422, -0.23002105723802604, -0.22498611355635412,
-0.2349870290884422, -0.2500228883022022, -0.24002197277011414, -0.22498611355635412, -0.21498519802426602, 
-0.21498519802426602, -0.2349870290884422, -0.2549888601526184, -0.2500228883022022, -0.23002105723802604, 
-0.2349870290884422, -0.2500228883022022, -0.2649897756847065, -0.2600238038342903, -0.2749906912167946, 
-0.2700247193663784, -0.2700247193663784, -0.2800256348984665, -0.2800256348984665, -0.28499160674888263, 
-0.2800256348984665, -0.2649897756847065, -0.2500228883022022, -0.2449879446205303, -0.2349870290884422, 
-0.2449879446205303, -0.2449879446205303, -0.2349870290884422, -0.21001922617384988, -0.23002105723802604, 
-0.2449879446205303, -0.2500228883022022, -0.24002197277011414, -0.2000183106417618, -0.15001373298132134, 
-0.08497329610712087, -0.02000183106417618, 0.060005493192528535, 0.1549797048317375, 0.2700247193663784, 
0.3500320436230831, 0.41996948051644395, 0.43997131158062014, 0.4150035086660278, 0.3899667339201797, 0.4150035086660278, 
0.43997131158062014, 0.4699740581768844, 0.5050117484548207, 0.5450154105831729, 0.5550163261152611, 0.5750181571794373, 
0.6150218193077897, 0.64999053775447, 0.64999053775447, 0.6250227348398777, 0.5799841290298534, 0.4899758892410606, 
0.3950016776018516, 0.3049934378130588, 0.23002105723802604, 0.12497695823547322, 0.01000091553208809, 
-0.11001007085296899, -0.18498245142800177, -0.2600238038342903, -0.3049934378130588, -0.3349961844093231, 
-0.3449970999414112, -0.324995268877235, -0.34003112809099506, -0.3549980154734993, -0.3749998465376755, 
-0.3799658183880916, -0.3850007620697635, -0.3850007620697635, -0.3850007620697635, -0.3899667339201797, 
-0.4150035086660278, -0.4250044241981159, -0.44997222711270823, -0.42997039604853204, -0.4250044241981159, 
-0.4250044241981159, -0.45997314264479633, -0.45997314264479633, -0.435005339730204, -0.41996948051644395, 
-0.4050025931339397, -0.4150035086660278, -0.4150035086660278, -0.4150035086660278, -0.40996856498435585, 
-0.4050025931339397, -0.3850007620697635, -0.3799658183880916, -0.3799658183880916, -0.3999676494522678, 
-0.3799658183880916, -0.3500320436230831, -0.33003021255890697, -0.34003112809099506, -0.34003112809099506, 
-0.3449970999414112, -0.34003112809099506, -0.3149943533451469, -0.2749906912167946, -0.28499160674888263, 
-0.2800256348984665, -0.2649897756847065, -0.24002197277011414, -0.21498519802426602, -0.2000183106417618, 
-0.22002014170593798, -0.20498428249217793, -0.21001922617384988, -0.18498245142800177, -0.16001464851340944, 
-0.15001373298132134, -0.14001281744923325, -0.13497787376756132, -0.13001190191714515, -0.10497512717129705, 
-0.08000732425670472, -0.04496963397876851, -0.030002746596264267, -0.034968718446680425, -0.034968718446680425, 
-0.02000183106417618, 0.014966887382504243, 0.034968718446680425, 0.014966887382504243, 0.024967802914592333, 
0.02000183106417618, 0.030002746596264267, 0.030002746596264267, 0.024967802914592333, 0.014966887382504243, 
-0.004965971850416155, -0.034968718446680425, -0.0549705495108566, -0.04496963397876851, -0.04000366212835236, 
-0.0649714650429447, -0.07497238057503278, -0.0900082397887928, -0.09497421163920895, -0.0900082397887928, 
-0.0900082397887928, -0.12497695823547322, -0.14001281744923325, -0.15001373298132134, -0.16498062036382558, 
-0.1449787892996494, -0.12497695823547322, -0.15001373298132134, -0.18498245142800177, -0.18498245142800177, 
-0.17001556404549753, -0.16498062036382558, -0.17498153589591367, -0.17498153589591367, -0.1800164795775856, 
-0.1800164795775856, -0.18498245142800177, -0.2000183106417618, -0.18498245142800177, -0.1900173951096737, 
-0.20498428249217793, -0.21498519802426602, -0.21498519802426602, -0.19498336696008986, -0.1800164795775856, 
-0.19498336696008986, -0.20498428249217793, -0.20498428249217793, -0.21498519802426602, -0.21498519802426602, 
-0.18498245142800177, -0.18498245142800177, -0.2000183106417618, -0.2000183106417618, -0.18498245142800177, 
-0.1800164795775856, -0.16001464851340944, -0.16498062036382558, -0.16498062036382558, -0.16498062036382558, 
-0.17001556404549753, -0.1549797048317375, -0.13497787376756132, -0.13497787376756132, -0.16498062036382558, 
-0.18498245142800177, -0.17001556404549753, -0.1449787892996494, -0.1549797048317375, -0.17001556404549753, 
-0.19498336696008986, -0.19498336696008986, -0.1900173951096737, -0.1800164795775856, -0.1549797048317375, 
-0.16498062036382558, -0.18498245142800177, -0.1900173951096737, -0.18498245142800177, -0.16498062036382558, 
-0.1549797048317375, -0.1549797048317375, -0.18498245142800177, -0.2000183106417618, -0.18498245142800177, 
-0.16001464851340944, -0.15001373298132134, -0.17001556404549753, -0.1900173951096737, -0.1900173951096737, 
-0.16498062036382558, -0.17498153589591367, -0.17498153589591367, -0.17498153589591367, -0.17498153589591367, 
-0.18498245142800177, -0.1800164795775856, -0.16498062036382558, -0.17001556404549753, -0.1549797048317375, 
-0.17498153589591367, -0.17498153589591367, -0.17498153589591367, -0.1449787892996494, -0.13497787376756132, 
-0.14001281744923325, -0.14001281744923325, -0.11497604270338514, -0.11497604270338514, -0.09497421163920895, 
-0.1000091553208809, -0.09497421163920895, -0.11497604270338514, -0.13497787376756132, -0.14001281744923325, 
-0.12001098638505707, -0.10497512717129705, -0.12497695823547322, -0.1449787892996494, -0.14001281744923325, 
-0.12497695823547322, -0.12497695823547322, -0.13001190191714515, -0.13497787376756132, -0.13001190191714515, 
-0.15001373298132134, -0.15001373298132134, -0.13001190191714515, -0.12001098638505707, -0.13001190191714515, 
-0.1449787892996494, -0.17001556404549753, -0.1549797048317375, -0.13001190191714515, -0.14001281744923325, 
-0.14001281744923325, -0.1449787892996494, -0.16498062036382558, -0.12497695823547322, -0.04496963397876851, 
0.014966887382504243, 0.07497238057503278, 0.11001007085296899, 0.16001464851340944, 0.22498611355635412, 
0.2600238038342903, 0.2449879446205303, 0.17498153589591367, 0.12497695823547322, 0.10497512717129705, 
0.1449787892996494, 0.23002105723802604, 0.3000274659626427, 0.3950016776018516, 0.43997131158062014]


Sinusarrhythmia = [-0.33500671409764443, -0.3249758904023084, -0.3249758904023084, -0.3400221259453125, 
-0.3299913022499764, -0.33500671409764443, -0.35501136817186585, -0.3499959563241978, -0.36002678001953387, 
-0.3649851985507511, -0.35501136817186585, -0.3499959563241978, -0.34498054447652976, -0.3400221259453125, 
-0.3400221259453125, -0.33500671409764443, -0.35501136817186585, -0.36002678001953387, -0.35501136817186585, 
-0.37000061039841914, -0.37997444077730447, -0.3649851985507511, -0.3750160222460872, -0.36002678001953387, 
-0.34498054447652976, -0.3400221259453125, -0.3400221259453125, -0.3299913022499764, -0.3249758904023084, 
-0.3299913022499764, -0.32001747187109114, -0.31500206002342307, -0.31500206002342307, -0.3000128177968698, 
-0.28502357557031643, -0.28000816372264836, -0.2650189214960951, -0.23999885557420564, -0.23498344372653762, 
-0.21497878965231626, -0.21999420149998428, -0.22500961334765232, -0.23498344372653762, -0.24997268595309094, 
-0.260003509648427, -0.254988097800759, -0.24501426742187368, -0.23498344372653762, -0.21999420149998428, 
-0.21999420149998428, -0.21497878965231626, -0.21999420149998428, -0.23498344372653762, -0.260003509648427, 
-0.28000816372264836, -0.2949974059492017, -0.3299913022499764, -0.34498054447652976, -0.3499959563241978, 
-0.3750160222460872, -0.37997444077730447, -0.39000526447264056, -0.3950206763203086, -0.39000526447264056, 
-0.37997444077730447, -0.3950206763203086, -0.3950206763203086, -0.40499450669919385, -0.41502533039452993, 
-0.41502533039452993, -0.41502533039452993, -0.4199837489257472, -0.4199837489257472, -0.41502533039452993, 
-0.40499450669919385, -0.4100099185468619, -0.41502533039452993, -0.4300145726210833, -0.4300145726210833, 
-0.4300145726210833, -0.43998840299996855, -0.43497299115230054, -0.43497299115230054, -0.4300145726210833, 
-0.43497299115230054, -0.4199837489257472, -0.40499450669919385, -0.40499450669919385, -0.40499450669919385, 
-0.40499450669919385, -0.4199837489257472, -0.39997909485152583, -0.41502533039452993, -0.39000526447264056, 
-0.3950206763203086, -0.37997444077730447, -0.3649851985507511, -0.3499959563241978, -0.3400221259453125, 
-0.3249758904023084, -0.30998664817575505, -0.254988097800759, -0.1500064088984349, 0.014989242226553333, 
0.28000816372264836, 0.6350195318945142, 1.0600186926679294, 1.4850178534413447, 1.8700077060663172, 
2.0849864957186335, 2.060023423113195, 1.7800152593905465, 1.245018997867139, 0.6049840541249568, 
-0.0349938963007747, -0.6749718467265062, -1.1350218971171468, -1.2600082400936923, -1.1500111393437003, 
-0.8999814600741585, -0.6399779504257315, -0.4100099185468619, -0.26997734002731233, -0.19497413557809487, 
-0.1750264748203243, -0.20500495927343096, -0.24501426742187368, -0.2899819941015337, -0.32001747187109114, 
-0.33500671409764443, -0.3249758904023084, -0.33500671409764443, -0.32001747187109114, -0.3000128177968698, 
-0.3000128177968698, -0.3050282296445378, -0.3050282296445378, -0.3000128177968698, -0.30998664817575505, 
-0.31500206002342307, -0.30998664817575505, -0.31500206002342307, -0.30998664817575505, -0.3000128177968698, 
-0.3000128177968698, -0.3000128177968698, -0.28000816372264836, -0.2949974059492017, -0.3050282296445378, 
-0.3050282296445378, -0.2949974059492017, -0.3050282296445378, -0.2949974059492017, -0.3000128177968698, 
-0.2899819941015337, -0.2899819941015337, -0.28502357557031643, -0.28000816372264836, -0.28000816372264836, 
-0.28000816372264836, -0.2899819941015337, -0.28000816372264836, -0.2949974059492017, -0.3050282296445378, 
-0.3050282296445378, -0.3000128177968698, -0.28502357557031643, -0.28502357557031643, -0.26997734002731233, 
-0.27499275187498035, -0.2650189214960951, -0.26997734002731233, -0.26997734002731233, -0.28000816372264836, 
-0.28502357557031643, -0.2899819941015337, -0.2899819941015337, -0.28502357557031643, -0.28502357557031643, 
-0.26997734002731233, -0.2650189214960951, -0.254988097800759, -0.24997268595309094, -0.24997268595309094, 
-0.24997268595309094, -0.260003509648427, -0.254988097800759, -0.254988097800759, -0.254988097800759, 
-0.24501426742187368, -0.24997268595309094, -0.23999885557420564, -0.23002502519532037, -0.22500961334765232, 
-0.21497878965231626, -0.21002037112109898, -0.21002037112109898, -0.21002037112109898, -0.20500495927343096, 
-0.21002037112109898, -0.1900157170468776, -0.20500495927343096, -0.19497413557809487, -0.1900157170468776, 
-0.1750264748203243, -0.1649956511249882, -0.1550218207461029, -0.1500064088984349, -0.1399755852030988, 
-0.1500064088984349, -0.1399755852030988, -0.1399755852030988, -0.1300017548242135, -0.12002792444532821, 
-0.10999710074999214, -0.08999244667577078, -0.07500320444921744, -0.0699877926015494, -0.060013962222664106, 
-0.05499855037499607, -0.05499855037499607, -0.04998313852732803, -0.045024719996110775, -0.05499855037499607, 
-0.04998313852732803, -0.045024719996110775, -0.0349938963007747, -0.0349938963007747, -0.014989242226553333, 
-0.005015411847668036, 0.0, -0.009973830378885298, -0.005015411847668036, -0.009973830378885298, -0.02000465407422137, 
-0.029978484453106666, -0.0349938963007747, -0.04000930814844274, -0.04998313852732803, -0.0699877926015494, 
-0.08497703482810273, -0.08497703482810273, -0.10999710074999214, -0.1399755852030988, -0.15998023927732016, 
-0.1900157170468776, -0.21497878965231626, -0.24501426742187368, -0.254988097800759, -0.27499275187498035, 
-0.2899819941015337, -0.3000128177968698, -0.30998664817575505, -0.31500206002342307, -0.33500671409764443, 
-0.34498054447652976, -0.34498054447652976, -0.3649851985507511, -0.37000061039841914, -0.37997444077730447, 
-0.3849898526249725, -0.39000526447264056, -0.39000526447264056, -0.3849898526249725, -0.39000526447264056, 
-0.37997444077730447, -0.37997444077730447, -0.3849898526249725, -0.39000526447264056, -0.39997909485152583, 
-0.4100099185468619, -0.40499450669919385, -0.4199837489257472, -0.4249991607734152, -0.4199837489257472, 
-0.4249991607734152, -0.4199837489257472, -0.40499450669919385, -0.3950206763203086, -0.40499450669919385, 
-0.4100099185468619, -0.41502533039452993, -0.41502533039452993, -0.41502533039452993, -0.41502533039452993, 
-0.40499450669919385, -0.4100099185468619, -0.39997909485152583, -0.37997444077730447, -0.3750160222460872, 
-0.3649851985507511, -0.37000061039841914, -0.3750160222460872, -0.3750160222460872, -0.37000061039841914, 
-0.3750160222460872, -0.3750160222460872, -0.37000061039841914, -0.3649851985507511, -0.36002678001953387, 
-0.34498054447652976, -0.3400221259453125]

# high rate ventricular tachycardia
VTHR = [-1.225, -1.2, -1.18, -1.155, -1.125, -1.08, -1.035, -0.98, -0.92, -0.855, -0.78, -0.695, -0.595, 
-0.475, -0.345, -0.205, -0.07, 0.04, 0.13, 0.2, 0.265, 0.33, 0.39, 0.455, 0.53, 0.595, 0.65, 0.69, 0.715, 
0.74, 0.775, 0.815, 0.85, 0.88, 0.895, 0.9, 0.89, 0.875, 0.86, 0.855, 0.865, 0.875, 0.87, 0.84, 0.78, 0.71, 
0.635, 0.565, 0.515, 0.46, 0.39, 0.28, 0.13, -0.06, -0.255, -0.42, -0.56, -0.66, -0.75, -0.835, -0.915, -0.99, 
-1.05, -1.085, -1.105, -1.1, -1.095, -1.095, -1.105, -1.125, -1.155, -1.17, -1.165, -1.145, -1.115, -1.085, 
-1.06, -1.04, -1.02, -1.0, -0.96, -0.91, -0.85, -0.785, -0.725, -0.675, -0.62, -0.555, -0.48, -0.375, -0.25, 
-0.12, 0.01, 0.125, 0.225, 0.32, 0.425, 0.53, 0.63, 0.72, 0.79, 0.835, 0.865, 0.885, 0.9, 0.92, 0.94, 0.955, 
0.97, 0.97, 0.965, 0.95, 0.94, 0.94, 0.955, 0.97, 0.975, 0.96, 0.915, 0.85, 0.785, 0.725, 0.675, 0.635, 0.585, 
0.505, 0.38, 0.21, 0.01, -0.19, -0.37, -0.515, -0.63, -0.73, -0.82, -0.895, -0.97, -1.03, -1.075, -1.1, -1.11, 
-1.115, -1.125, -1.155, -1.195, -1.23, -1.26, -1.265, -1.26, -1.25, -1.235, -1.225, -1.225, -1.225, -1.225, 
-1.205, -1.17, -1.13, -1.085, -1.045, -1.005, -0.955, -0.89, -0.795, -0.68, -0.555, -0.42, -0.29, -0.175, 
-0.07, 0.025, 0.125, 0.23, 0.335, 0.43, 0.51, 0.565, 0.61, 0.645, 0.68, 0.72, 0.77, 0.825, 0.87, 0.9, 0.92, 
0.925, 0.925, 0.94, 0.96, 0.985, 1.005, 1.01, 1.005, 0.99, 0.965, 0.945, 0.93, 0.925, 0.93, 0.92, 0.895, 
0.85, 0.805, 0.775, 0.755, 0.74, 0.72, 0.69, 0.655, 0.62, 0.58, 0.545, 0.515, 0.495, 0.465, 0.44, 0.405, 
0.37, 0.335, 0.315, 0.295, 0.295, 0.295, 0.285, 0.24, 0.17, 0.08, -0.015, -0.12, -0.23, -0.365, -0.52, 
-0.685, -0.845, -0.985, -1.095, -1.18, -1.25, -1.3, -1.345, -1.365, -1.385, -1.405, -1.44, -1.47, -1.49, 
-1.495, -1.49, -1.47, -1.45, -1.43, -1.415, -1.405, -1.395, -1.37, -1.34, -1.295, -1.245, -1.185, -1.135, 
-1.08, -1.01, -0.925, -0.815, -0.685, -0.565, -0.455, -0.36, -0.27, -0.175, -0.085, 0.015, 0.11, 0.2, 0.28, 
0.35, 0.415, 0.475, 0.54, 0.62, 0.7, 0.78, 0.85, 0.9, 0.935, 0.965, 0.99, 1.02, 1.045, 1.065, 1.085, 1.095, 
1.095, 1.08, 1.045, 1.02, 0.995, 0.985, 0.97, 0.945, 0.905]

# Ventricular Fibrulation 
VF = [0.02, -0.04, -0.07, -0.08, -0.065, -0.05, -0.045, -0.06, -0.085, -0.105, -0.12, -0.125, -0.115, -0.095,
 -0.085, -0.08, -0.085, -0.09, -0.1, -0.1, -0.105, -0.1, -0.1, -0.105, -0.115, -0.13, -0.145, -0.155, -0.155, 
 -0.14, -0.13, -0.125, -0.125, -0.13, -0.135, -0.135, -0.12, -0.105, -0.075, -0.045, -0.03, -0.025, -0.02, 
 -0.005, 0.025, 0.06, 0.09, 0.11, 0.125, 0.145, 0.17, 0.205, 0.245, 0.285, 0.33, 0.36, 0.37, 0.36, 0.335, 0.3, 
 0.265, 0.245, 0.225, 0.19, 0.135, 0.055, -0.03, -0.11, -0.175, -0.225, -0.25, -0.255, -0.265, -0.285, -0.32, 
 -0.37, -0.415, -0.445, -0.45, -0.44, -0.43, -0.43, -0.445, -0.46, -0.47, -0.465, -0.445, -0.42, -0.39, -0.365, 
 -0.355, -0.365, -0.375, -0.385, -0.375, -0.355, -0.335, -0.315, -0.315, -0.325, -0.33, -0.34, -0.33, -0.305, 
 -0.275, -0.245, -0.225, -0.215, -0.215, -0.2, -0.175, -0.14, -0.085, -0.025, 0.045, 0.11, 0.16, 0.185, 0.2, 0.21, 
 0.22, 0.225, 0.225, 0.195, 0.15, 0.095, 0.045, 0.005, -0.02, -0.04, -0.06, -0.085, -0.115, -0.155, -0.195, -0.23, 
 -0.25, -0.26, -0.255, -0.25, -0.245, -0.24, -0.24, -0.235, -0.22, -0.195, -0.165, -0.135, -0.115, -0.105, -0.1, 
 -0.095, -0.08, -0.06, -0.045, -0.03, -0.025, -0.025, -0.025, -0.025, -0.02, 0.0, 0.025, 0.05, 0.07, 0.075, 0.075, 
 0.065, 0.045, 0.045, 0.06, 0.085, 0.105, 0.125, 0.135, 0.145, 0.155, 0.165, 0.185, 0.2, 0.21, 0.2, 0.17, 0.115, 
 0.06, 0.005, -0.04, -0.075, -0.11, -0.15, -0.2, -0.245, -0.28, -0.305, -0.315, -0.32, -0.315, -0.325, -0.355, -0.385, 
 -0.415, -0.45, -0.46, -0.46, -0.445, -0.42, -0.4, -0.4, -0.4, -0.41, -0.41, -0.39, -0.36, -0.33, -0.315, -0.315, -0.33, 
 -0.345, -0.35, -0.34, -0.315, -0.29, -0.265, -0.245, -0.23, -0.215, -0.19, -0.15, -0.095, -0.03, 0.035, 0.09, 0.135, 
 0.175, 0.21, 0.25, 0.3, 0.34, 0.36, 0.36, 0.34, 0.295, 0.245, 0.195, 0.155, 0.12, 0.095, 0.065, 0.025, -0.025, -0.075, 
 -0.12, -0.15, -0.17, -0.175, -0.185, -0.195, -0.215, -0.245, -0.28, -0.3, -0.305, -0.3, -0.295, -0.295, -0.3, -0.315, 
 -0.335, -0.34, -0.33, -0.295, -0.255, -0.215, -0.2, -0.2, -0.22, -0.235, -0.235, -0.22, -0.185, -0.145, -0.11, -0.08, 
 -0.055, -0.03, 0.0, 0.05, 0.125, 0.2, 0.265, 0.315, 0.35, 0.37, 0.38, 0.39, 0.39, 0.395, 0.385, 0.36, 0.32, 0.255, 0.19]

 # Bradicardia Sinusal 
SBR = [0.125, 0.13, 0.14, 0.14, 0.135, 0.12, 0.105, 0.09, 0.085, 0.09, 0.095, 0.09, 0.08, 0.07, 0.06, 0.055, 0.055, 0.06, 
 0.065, 0.065, 0.06, 0.045, 0.025, 0.005, -0.005, -0.005, -0.005, 0.0, -0.01, -0.02, -0.035, -0.045, -0.045, -0.04, -0.03, 
 -0.02, -0.02, -0.025, -0.035, -0.04, -0.04, -0.04, -0.03, -0.025, -0.02, -0.025, -0.03, -0.04, -0.045, -0.045, -0.035, 
 -0.02, -0.015, -0.015, -0.025, -0.035, -0.045, -0.04, -0.03, -0.02, -0.01, -0.01, -0.015, -0.02, -0.03, -0.035, -0.04, 
 -0.035, -0.025, -0.02, -0.02, -0.03, -0.04, -0.045, -0.04, -0.03, -0.02, -0.01, -0.01, -0.01, -0.015, -0.025, -0.025, 
 -0.015, -0.01, -0.005, -0.005, -0.01, -0.015, -0.02, -0.025, -0.035, -0.035, -0.03, -0.025, -0.02, -0.02, -0.03, -0.035, 
 -0.035, -0.03, -0.02, -0.015, -0.015, -0.015, -0.015, -0.02, -0.02, -0.01, 0.0, 0.005, 0.005, 0.0, -0.01, -0.02, -0.02, 
 -0.015, -0.005, 0.005, 0.01, 0.01, 0.005, -0.005, -0.015, -0.015, -0.015, -0.01, 0.0, 0.01, 0.01, 0.01, 0.01, 0.015, 
 0.025, 0.035, 0.045, 0.05, 0.045, 0.045, 0.035, 0.04, 0.045, 0.055, 0.065, 0.075, 0.07, 0.06, 0.05, 0.045, 0.045, 0.045, 
 0.055, 0.065, 0.07, 0.07, 0.06, 0.05, 0.04, 0.045, 0.055, 0.065, 0.07, 0.065, 0.055, 0.045, 0.04, 0.035, 0.035, 0.035, 
 0.035, 0.03, 0.03, 0.02, 0.01, 0.005, 0.005, 0.01, 0.015, 0.01, 0.005, 0.0, -0.005, 0.0, 0.0, 0.005, 0.01, 0.01, 0.0, 
 -0.01, -0.025, -0.035, -0.03, -0.02, -0.01, 0.0, -0.005, -0.01, -0.015, -0.02, -0.015, -0.005, 0.005, 0.015, 0.02, 
 0.015, 0.0, -0.01, -0.01, -0.01, 0.0, 0.0, 0.0, -0.005, -0.015, -0.025, -0.03, -0.03, -0.035, -0.035, -0.035, -0.045, 
 -0.06, -0.07, -0.08, -0.08, -0.075, -0.075, -0.08, -0.085, -0.095, -0.1, -0.1, -0.11, -0.135, -0.16, -0.185, -0.215, 
 -0.23, -0.245, -0.26, -0.275, -0.285, -0.285, -0.275, -0.26, -0.245, -0.225, -0.21, -0.2, -0.19, -0.19, -0.195, -0.195, 
 -0.19, -0.18, -0.165, -0.135, -0.105, -0.065, -0.025, 0.01, 0.035, 0.05, 0.055, 0.055, 0.06, 0.075, 0.095, 0.11, 0.125, 
 0.125, 0.12, 0.105, 0.1, 0.095, 0.1, 0.105, 0.11, 0.11, 0.105, 0.1, 0.09, 0.09, 0.095, 0.1, 0.11, 0.11, 0.11, 0.105, 
 0.105, 0.105, 0.11, 0.12, 0.13, 0.135, 0.135, 0.125, 0.115, 0.105, 0.1, 0.1, 0.105]