import numpy as np 

def sigX():
    return np.array([[0,1],[1,0]])

def sigY():
    return np.array([[0,-1j],[1j,0]])

def sigZ():
    return np.array([[1,0],[0, -1]])
