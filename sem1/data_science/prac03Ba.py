"""
Created on Wed Dec 28

@author: Santosh Parse
@program name: Write a program to convert Video file format to HORUS format 
"""
import os
import shutil
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def mov2frames(sFileName, sOutDir):
    print('='*65)
    print('Start Movie to Frames')
    print('='*65)
    vidcap = cv2.VideoCapture(sFileName)
    success,image = vidcap.read()
    count = 0
    while success:
        success,image = vidcap.read()
        sFrame = sOutDir + str('/venice-frame-' + str(format(count, '04d')) + '.jpg')
        print('Extracted:', sFrame)
        if not success:
            break
        cv2.imwrite(sFrame, image)
        if count == 10:
            break
        if os.path.getsize(sFrame) == 0:
            count += -1
            os.remove(sFrame)
            print('Removed: ', sFrame)
        if cv2.waitKey(10) == 27: # exit if Escape is hit
            break
        count += 1
    print('='*65)
    print('Generate:', count, 'Frames')
    print('='*65)
    print('Movie to Frames HORUS - Done')
    print('='*65)

# Initialize input and output
sInputFileName = 'C:/VKHCG/05-DS/9999-Data/Venice.mp4'
sDataBaseDir = 'C:/VKHCG/05-DS/9999-Data/temp'
if os.path.exists(sDataBaseDir):
    shutil.rmtree(sDataBaseDir)
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)

# Input Agreement
mov2frames(sFileName=sInputFileName, sOutDir=sDataBaseDir)
f = 0
for file in os.listdir(sDataBaseDir):
    if file.endswith(".jpg"):
        f += 1
        sInputFileName = os.path.join(sDataBaseDir, file)
        print('Process:', sInputFileName)
        InputData = cv2.imread(sInputFileName, cv2.IMREAD_COLOR)
        print('='*65)
        print('Input Data Values')
        print('X:', InputData.shape[0])
        print('Y:', InputData.shape[1])
        print('RGBA:', InputData.shape[2])
        print('='*65)

        # Processing Rules
        ProcessRawData = InputData.flatten()
        y = InputData.shape[2] + 2
        x = int(ProcessRawData.shape[0] / y)
        ProcessFrameData = pd.DataFrame(np.reshape(ProcessRawData, (x,y)))
        ProcessFrameData['Frame'] = file
        print('='*65)
        print('Process Data Values')
        print('='*65)
        plt.imshow(InputData)
        # plt.show()
        if f == 1:
            ProcessData = ProcessFrameData
        else:
            ProcessData = pd.concat([ProcessData ,ProcessFrameData])
if f > 0:
    sColumns = ['XAxis', 'YAxis', 'Red', 'Green', 'Blue', 'Alpha']
    ProcessData.columns = sColumns
    ProcessData.index.names = ['ID']
    print('Rows:', ProcessData.shape[0])
    print('Columns:', ProcessData.shape[1])
    print('='*65)

    # Output Agreement
    OutputData = ProcessData
    print('Storing File')
    sOutputFileName = 'C:/VKHCG/05-DS/9999-Data/HORUS-Movie-Frame.csv'
    OutputData.to_csv(sOutputFileName, index = False)
print('='*65)
print('Processed:', f, ' frames')
print('='*65)
print('='*21 + ' Movie to HORUS - Done ' + '='*21)