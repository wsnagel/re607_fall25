#!/usr/bin/python
from math import sin, cos, pi

import matplotlib
import matplotlib.pyplot as plt
import scipy
import numpy as np
from lqr import LQR 
        

def main(args=None):
    T = 2500
    dt = 0.01
    mass = 1.0
    friction = 0.1

    # State vector = [...] -- You need to determine this structure
    # TODO: Select initial values for state vector.  You have freedom here, so follow prompt's description
    
    x_init = np.array([1.0, -1.0], dtype='float64').transpose() # Two states
    
    #TODO: Build A, B, Q and R Matrices.  Follow the LQR example from class
    A = 0.4*np.eye(2) #Example structure for two states
    B = np.array([[1], [-0.2]], dtype='float64') #Example structure for one input
    Q = np.eye(2)
    R = np.eye(1)
    
    lqr = LQR(A,B,Q,R)
    K = lqr.compute_policy_gains(T, dt)

    x = x_init
    X = np.zeros((T, 2), dtype='float64') #Make same size as state vector
    U = np.zeros((T, 1), dtype='float64') #Make same size as input vector
    
    for i in range(T):
        u = np.dot(K[i], x)

        # This is essentially the simulator of the vehicle
        x = np.dot(A, x) + np.dot(B, u)
        
        
        X[i, :] = x.transpose()
        U[i, :] = u.transpose()


    plt.switch_backend('QtAgg')
    
    plt.figure()
    plt.plot( X[:, 0], '-b')
    plt.plot( X[:, 1], '-r')
    plt.legend(['state1', 'state2'])
    plt.xlabel('time steps')
    plt.show()
    
    
    plt.figure()
    plt.plot( U[:, 0], 'b')
    plt.legend(['input1'])
    plt.xlabel('time steps')
    plt.ylabel('controls')
    plt.show()

    plt.figure()
    plt.plot( X[:, 0], X[:, 1], 'b')
    plt.xlabel('x(t)')
    plt.ylabel('y(t)')
    plt.legend(['Another state plot: State1 vs. State2'])
    
    plt.show()
    
    
if __name__ == "__main__":
    main()


    
