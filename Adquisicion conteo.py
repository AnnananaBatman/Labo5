# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import pyvisa
from scipy.signal import savgol_filter,argrelextrema
import time

from osciloscope import Osciloscope

rm = pyvisa.ResourceManager('@py')
instrumentos = rm.list_resources()
print(instrumentos)

osc = Osciloscope(0)

#%%
#LLevarnos algunas ventanas crudas con los parametros fijos

t, V = osc.getWindow(1)
data_to_save = np.vstack((t, V))
folderpath = '/home/publico/Desktop/Grupo 6/Conteo/Ventanas/'
np.savetxt(folderpath  + 'Ventana-1k-sin-250ns-5mV-900V.txt', data_to_save)

plt.plot(t,V)
plt.xlabel('Tiempo')
plt.ylabel('Tension')

#%%
#Guardamos los mìnimos y los picos de todas las ventanas juntas
N=500
#ampCmin=[]
ampCpeak=[]
for i in range(N):
    try:
        t, V = osc.getWindow(1)
        #filtered_col=savgol_filter(V, 15, 3)
        #y_min=filtered_col[argrelextrema(filtered_col, np.less)[0]]
        #ampCmin.append(y_min)
        peaks = find_peaks(V,distance=20)
        amp=V[peaks[0]]
        for j in range(len(amp)):
            ampCpeak.append(amp[j])
            #np.savetxt('/home/publico/Desktop/Grupo 6/Conteo/Ventanas/'  + f'50-sin-50ns-5mv-900V-{i}.txt', amp, fmt = '%.3f')
        print(i)
        time.sleep(50e-3)
    except:
        print('cague')
        pass
    
#np.savetxt('/home/publico/Desktop/Grupo 6/Conteo/Ventanas/'  + f'MinCf-50-sin-100ns-2mvBw-900V.txt', ampCmin, fmt = '%.7f')
np.savetxt('/home/publico/Desktop/Grupo 6/Conteo/Ventanas/'  + f'MinSf-100.8-sin-2.5us-2mVBw-900V.txt', ampCpeak, fmt = '%.7f')
#%%
#Probar los histogramas
binsize=np.arange(min(V), max(V), 0.0002)
plt.figure(1)
plt.hist(np.array(ampCpeak), bins=binsize)

#plt.figure(2)
#plt.hist(ampCmin)
#%%

t, V = osc.getWindow(1)
peaks = find_peaks(V,distance=20)
Amp=V[peaks[0]]
TAmp=t[peaks[0]]


plt.plot(t,V)
plt.scatter(TAmp,Amp,color='r')


'''
filtered_col=savgol_filter(V, 15, 3)
y_min=filtered_col[argrelextrema(filtered_col, np.less)[0]]

plt.plot(t,V)
plt.plot(t,filtered_col)
'''
