"""
Created on Wed Dec 28

@author: Santosh Parse
@program name: Write a program to convert JPG/Images file format to HORUS format 
"""
import cv2
import pandas as  pd
import matplotlib.pyplot as plt
import numpy as np

# Input Agreement
sInputFileName = 'C:/VKHCG/05-DS/9999-Data/Lena.jpg'
InputData = cv2.imread(sInputFileName, cv2.IMREAD_COLOR)
print('='*65)
print('Input Data Values:')
print('X:', InputData.shape[0])
print('Y:', InputData.shape[1])
print('RGBA:', InputData.shape[2])
print('='*65)

# Processing Rules
ProcessRawData = InputData.flatten()
y = InputData.shape[2] + 2
x = int(ProcessRawData.shape[0] / y)
ProcessData = pd.DataFrame(np.reshape(ProcessRawData, (x,y)))
sColumns = ['XAxis', 'YAxis', 'Red', 'Green', 'Blue']
ProcessData.columns = sColumns
ProcessData.index.names = ['ID']
print('Rows:', ProcessData.shape[0])
print('Columns:', ProcessData.shape[1])
print('='*65)
print('Process Data Values')
plt.imshow(InputData)
plt.show()
print('='*65)

# Output Agreement
OutputData = ProcessData
sOutputFileName = sInputFileName = 'C:/VKHCG/05-DS/9999-Data/Lena-HORUS-Picture.csv'
print('Storing File :', sOutputFileName)
OutputData.to_csv(sOutputFileName, index=False)
print('='*20 + ' Picture to HORUS - Done ' + '='*20) 