"""
Created on Wed Dec 28

@author: Santosh Parse
@program name: Write a program to convert Audio file format to HORUS format 
"""
from scipy.io import wavfile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def show_info(aname, a, r):
    print('-'*65)
    print("Audio:", aname)
    print('-'*65)
    print("Rate:", r)
    print('-'*65)
    print("shape:", a.shape)
    print("dtype:", a.dtype)
    print("min, max:", a.min(), a.max())
    print('-'*65)
    plot_info(aname, a,r)

def plot_info(aname, a, r):
    sTitle= 'Signal Wave - '+ aname + ' at ' + str(r) + 'hz'
    plt.title(sTitle)
    sLegend=[]
    for c in range(a.shape[1]):
        sLabel = 'Ch' + str(c+1)
        sLegend=sLegend+[str(c+1)]
        plt.plot(a[:,c], label=sLabel)
    plt.legend(sLegend)
    plt.show()

# Input Agreement
sInputFileName = 'C:/VKHCG/05-DS/9999-Data/2ch-sound.wav'
print('-'*65)
print('Processing:', sInputFileName)
print('-'*65)

# Processing Rules
InputRate, InputData = wavfile.read(sInputFileName)
show_info('2 channel', InputData, InputRate)
ProcessData = pd.DataFrame(InputData)
sColumns = ['ch1', 'ch2']
ProcessData.columns = sColumns

# Output Agreement
OutputData = ProcessData
sOutputFileName = 'C:/VKHCG/05-DS/9999-Data/HORUS-Audio-2ch.csv'
OutputData.to_csv(sOutputFileName, index=False)
