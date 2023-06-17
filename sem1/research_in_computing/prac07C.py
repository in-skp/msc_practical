#7B : Perform polynomial regression for prediction
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100,98,97]

mymodel= np.poly1d(np.polyfit(x, y, 3))
myline = np.linspace(1,22,100)

plt.scatter(x,y)
plt.plot(myline,mymodel(myline))
plt.show()

print(r2_score(y, mymodel(x)))