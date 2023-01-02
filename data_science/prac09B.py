"""
Created on Mon Jan 02

@author: Santosh Parse
@program name: Generating Reports - Vermeulen PLC
"""
import sys
import os
import pandas as pd
from folium.plugins import FastMarkerCluster, HeatMap
from folium import Marker, Map
import webbrowser

pd.options.mode.chained_assignment = None

if sys.platform == 'linux':
    Base = os.path.expanduser('~') + 'VKHCG'
else:
    Base = 'C:/VKHCG'
print('#'*65) 
print("Working Base: ", Base, 'using', sys.platform)
print('#'*65) 

sFileName=Base+'/02-Krennwallner/01-Retrieve/01-EDS/02-Python/Retrieve_DE_Billboard_Locations.csv'
df = pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
df.fillna(value=0, inplace=True)
print(df.shape)

t=0
for i in range(df.shape[0]):
    try:
        sLongitude=df["Longitude"][i]
        sLongitude=float(sLongitude)
    except Exception:
        sLongitude=float(0.0)
    try:
        sLatitude=df["Latitude"][i]
        sLatitude=float(sLatitude)
    except Exception:
        sLatitude=float(0.0)
    try:
        sDescription=df["Place_Name"][i] + ' (' + df["Country"][i]+')'
    except Exception:
        sDescription='VKHCG'
    if sLongitude != 0.0 and sLatitude != 0.0:
        DataClusterList=list([sLatitude, sLongitude])
        DataPointList=list([sLatitude, sLongitude, sDescription])
        t+=1
        if t==1:
            DataCluster=[DataClusterList]
            DataPoint=[DataPointList]
        else:
            DataCluster.append(DataClusterList)
            DataPoint.append(DataPointList)
data=DataCluster

pins=pd.DataFrame(DataPoint)
pins.columns = [ 'Latitude','Longitude','Description']
billbords_map1 = Map(location=[48.1459806, 11.4985484], zoom_start=5)
marker_cluster = FastMarkerCluster(data).add_to(billbords_map1)
sFileNameHtml1=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/Billboard1.html'
billbords_map1.save(sFileNameHtml1)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml1))

billbords_map2 = Map(location=[48.1459806, 11.4985484], zoom_start=5)
for name, row in pins.iloc[:100].iterrows():
    Marker([row["Latitude"],row["Longitude"]], popup=row["Description"]).add_to(billbords_map2)
sFileNameHtml2=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/Billboard2.html'
billbords_map2.save(sFileNameHtml2)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml2))

billbords_heatmap = Map(location=[48.1459806, 11.4985484], zoom_start=5)
billbords_heatmap.add_child(HeatMap([[row["Latitude"], row["Longitude"]] for name, row in pins.iloc[:100].iterrows()]))
sFileNameHtml3=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/Billboard_heatmap.html'
billbords_heatmap.save(sFileNameHtml3)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml3))

print('#'*28 + ' Done!!! ' + '#'*28)
