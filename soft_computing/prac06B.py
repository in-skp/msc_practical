"""
Created on Mon Dec 12

@author: Santosh Parse
@program name: Implement Adaptive resonance theory.
"""
from __future__ import print_function
from __future__ import division
import numpy as np

class ART:
    def __init__(self, n=5, m=10, rho=.5):
        
        self.F1 = np.ones
        self.F2 = np.ones(m)
        self.Wf = np.random.random((m,n))
        self.Wb = np.random.random((n,m))
        self.rho = rho
        self.active = 0

    def learn(self, X):
        self.F2[...] = np.dot(self.Wf, X)
        I = np.argsort(self.F2[:self.active].ravel())[::-1]

        for i in I:
            
            d = (self.Wb[:,i]*X).sum()/X.sum()
            if d >= self.rho:
                
                self.Wb[:,i] *= X
                self.Wf[i,:] = self.Wb[:,i]/(0.5+self.Wb[:,i].sum())
                return self.Wb[:,i], i

        if self.active < self.F2.size:
            i = self.active
            self.Wb[:,i] *= X
            self.Wf[i,:] = self.Wb[:,i]/(0.5+self.Wb[:,i].sum())
            self.active += 1
            return self.Wb[:,i], i

        return None,None


if __name__ == '__main__':

    np.random.seed(1)
    network = ART( 5, 10, rho=0.5)
    data = ["   O ",
            "  O O",
            "    O",
            "  O O",
            "    O",
            "  O O",
            "    O",
            " OO O",
            " OO  ",
            " OO O",
            " OO  ",
            "OOO  ",
            "OO   ",
            "O    ",
            "OO   ",
            "OOO  ",
            "OOOO ",
            "OOOOO",
            "O    ",
            " O   ",
            "  O  ",
            "   O ",
            "    O",
            "  O O",
            " OO O",
            " OO  ",
            "OOO  ",
            "OO   ",
            "OOOO ",
            "OOOOO"]
    X = np.zeros(len(data[0]))
    for i in range(len(data)):
        for j in range(len(data[i])):
            X[j] = (data[i][j] == 'O')
        Z, k = network.learn(X)
        print("|%s|"%data[i],"-> class", k)