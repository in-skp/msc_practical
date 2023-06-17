"""
Created on Mon Jan 02

@author: Santosh Parse
@program name: Generating Reports - Vermeulen PLC
"""
import sys
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

if sys.platform == 'linux':
    Base = os.path.expanduser('~') + 'VKHCG'
else:
    Base = 'C:/VKHCG'
print('#'*65) 
print("Working Base: ", Base, 'using', sys.platform)
print('#'*65) 

sInputFileName='02-Assess/01-EDS/02-Python/Assess-Network-Routing-Company.csv'
sOutputFileName1='05-Organise/01-EDS/02-Python/Organise-Network-Routing-Company.gml'
sOutputFileName2='05-Organise/01-EDS/02-Python/Organise-Network-Routing-Company.png'
Company='01-Vermeulen'

# Import Country Data
sFileName=Base + '/' + Company + '/' + sInputFileName
print('#'*65)
print('Loading :',sFileName)
print('#'*65)
CompanyData=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
print('#'*65)
print(CompanyData.head())
print(CompanyData.shape)


G=nx.Graph()
for i in range(CompanyData.shape[0]):
    for j in range(CompanyData.shape[0]):
        Node0=CompanyData['Company_Country_Name'][i]
        Node1=CompanyData['Company_Country_Name'][j]
        if Node0 != Node1:
            G.add_edge(Node0,Node1)
for i in range(CompanyData.shape[0]):
    Node0=CompanyData['Company_Country_Name'][i]
    Node1=CompanyData['Company_Place_Name'][i] + '('+ CompanyData['Company_Country_Name'][i] + ')'
    if Node0 != Node1:
        G.add_edge(Node0,Node1)

print('Nodes:', G.number_of_nodes())
print('Edges:', G.number_of_edges())

sFileName=Base + '/' + Company + '/' + sOutputFileName1
print('#'*65)
print('Storing :',sFileName)
print('#'*65)
nx.write_gml(G, sFileName)

sFileName=Base + '/' + Company + '/' + sOutputFileName2
print('#'*65)
print('Storing Graph Image:',sFileName)
print('#'*65)
plt.figure(figsize=(15, 15))
pos=nx.spectral_layout(G,dim=2)
nx.draw_networkx_nodes(G,pos, node_color="k", node_size=10, alpha=0.8)
nx.draw_networkx_edges(G, pos,edge_color='r', arrows=False, style="dashed")
nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif',font_color='b')
plt.axis('off')
plt.savefig(sFileName,dpi=600)
plt.show()
print('#'*28 + ' Done!!! ' + '#'*28)
