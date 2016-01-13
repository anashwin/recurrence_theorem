# Ashwin Narayan
# Visualization of Double Pendulum
# Code based on Plot.ly example: 
# https://plot.ly/python/streaming-double-pendulum-tutorial/
# Recurrence plots are my own

#import plotly.plotly as py
#import plotly.tools as tls
#from plotly.graph_objs import *
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import time
import sys
import numpy as np
from numpy import sin, cos, pi
import json
import matplotlib.animation as animation

def p1(th1, w1, th2, w2): 
    return (M1+M2)*(L1**2)*w1+M2*L1*L2*w2*cos(th1-th2)

def p2(th1, w1, th2, w2): 
    return M2*(L2**2)*w2+M2*L1*L2*w1*cos(th1-th2)

def rad(deg): 
    return 1.0*deg*pi/180

# Constants
G = 9.8
L1 = 1.0
L2 = 1.0
M1 = 1.0
M2 = 1.0

if len(sys.argv) > 1: 
    th1 = rad(float(sys.argv[1]))
    w1 = rad(float(sys.argv[2]))
    th2 = rad(float(sys.argv[3]))
    w2 = rad(float(sys.argv[4]))
    tsteps = int(sys.argv[5])
    outfile = sys.argv[6]
else: 
    th1 = rad(30.0)
    th2 = rad(-10.0)
    w1 = rad(0.0)
    w2 = rad(0.0)
    tsteps = 500
    outfile ='init_temp.npy'

state = np.array([th1, w1, th2, w2, p1(th1,w1,th2,w2), p2(th1,w1,th2,w2)])

def derivs(state,t): 
    dxdt = np.zeros_like(state) # derivatives array
    del_ = state[2] - state[0] # angles of pendula
    
    dxdt[0] = state[1]
    den1 = (M1+M2)*L1 - M2*L1*cos(del_)*cos(del_)  # deno. of dxdt[2]
    dxdt[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_)
               + M2*G*sin(state[2])*cos(del_) 
               + M2*L2*state[3]*state[3]*sin(del_)
               - (M1+M2)*G*sin(state[0]))/den1     # derv. of angular velo.1

    dxdt[2] = state[3]  # derv. of angle2

    den2 = (L2/L1)*den1  # deno. of dxdt[3]
    dxdt[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_)  
               + (M1+M2)*G*sin(state[0])*cos(del_)
               - (M1+M2)*L1*state[1]*state[1]*sin(del_)
               - (M1+M2)*G*sin(state[2]))/den2   # derv. of angular velo.2
    
    
    return dxdt  # return time derv. array
    
N=2   # number of time integrate.odeint() integrations 
i=1   # init. counter

# (-) Solve the system of ODEs N times

while i<N:
    
    i+=1                    # add to counter
    dt=0.05                 # create a time array from 0..100  
    t=np.arange(0.0,tsteps,dt)  # sampled at 0.05 second steps

    # Solve the system of  ODEs, for times in t!
    y=integrate.odeint(derivs,state,t)
    #y.extend([p1(state[0],state[1],state[2],state[3]),
    #          p2(state[0],state[1],state[2],state[3])])
    y[:,4] = p1(y[:,0],y[:,1],y[:,2],y[:,3])
    y[:,5] = p2(y[:,0],y[:,1],y[:,2],y[:,3])
    np.save(outfile, y)

    # (!) Write the solutions to Plotly's servers, 
    #     1 per stream, 1 point at a time
#    for (x1i,y1i,x2i,y2i) in zip(x1,y1,x2,y2):
        
        # (@) Write list corresponding to 3 pendulum nodes,
        #     overwriting the data on the plot
#        s1.write(dict(x=[0, x1i, x2i], y=[0, y1i, y2i]))  
        
        # (@) Write 1 point corresponding to 1 pt of path,
        #     appending the data on the plot
#        s2.write(dict(x=x2i, y=y2i))        
        
#        time.sleep(0.08)  # (!) plot pts 80 ms at a time, for smoother plotting

    # Set the new initial state

# (@) Close both streams when done plotting
#s1.close()
#s2.close()
