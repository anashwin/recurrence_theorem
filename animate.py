import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

#if len(sys.argv) > 1: 
#    infile = sys.argv[1]
#else: 
#    infile = 'init_temp.npy'
#if len(sys.argv) > 2: 
#    animxlim = (float(sys.argv[2]),float(sys.argv[3]))
#    animylim = (float(sys.argv[4]),float(sys.argv[5]))
#else:
#    animxlim = (-2,2)
#    animylim = (-2,2)

if len(sys.argv)== 1: 
    infile = 'init_temp.npy'
    animxlim = (-.6,.6)
    animylim = (-2.2, -1.5)
    phasexlim1 = (-2,2)
    phaseylim1 = (-2,2)
    phasexlim2 = (-2,2)
    phaseylim2 = (-2,2)
    timeylim = (-1,1)
elif sys.argv[1] == 'init_1.npy': 
    infile = 'init_1.npy'
    animxlim = (-2,2)
    animylim = (-2,2)
    phasexlim1 = (-10,10)
    phaseylim1 = (-10,10)
    phasexlim2 = (-20,20)
    phaseylim2 = (-10,10)
    timeylim = (-10,10)
elif sys.argv[1] == 'init_2.npy':
    infile = 'init_2.npy'
    animxlim = (-.1,.1)
    animylim = (-2.1, -1.9)
    phasexlim1 = (-.5,.5)
    phaseylim1 = (-.5,.5)
    phasexlim2 = (-.5,.5)
    phaseylim2 = (-.5,.5)
    timeylim = (-.5,.5)
else: 
    infile = sys.argv[1]
    animxlim = (-.6,.6)
    animylim = (-2.2, -1.5)
    phasexlim1 = (-2,2)
    phaseylim1 = (-2,2)
    phasexlim2 = (-2,2)
    phaseylim2 = (-2,2)
    timeylim = (-1,1)


y = np.load(infile)

L1 = 1.0
L2 = 1.0

x1 = L1*sin(y[:,0])        # convert angles to x-y coordinates
y1 = -L1*cos(y[:,0])
x2 = L2*sin(y[:,2]) + x1   #   for both pendulums
y2 = -L2*cos(y[:,2]) + y1

xp1 = y[:,0]
pp1 = y[:,4]

xp2 = y[:,2]
pp2 = y[:,5]

fig = plt.figure()
axanim = fig.add_subplot(221, autoscale_on=False, xlim=animxlim,ylim=animylim)
axanim.set_xlabel('$x$')
axanim.set_ylabel('$y$')
axanim.grid()

#axtime = fig.add_subplot(222,autoscale_on=True, xlim=(0,10),ylim=(-2.5,2.5))
axtime = fig.add_subplot(222)
axtime.set_xlabel('$t$')
axtime.set_ylabel('$\\theta$')
axtime.grid()

axphase1 = fig.add_subplot(223, autoscale_on=False, xlim=phasexlim1, 
                           ylim=phaseylim1)
axphase1.set_xlabel('$\\theta_1$')
axphase1.set_ylabel('$p_1$')
axphase1.grid()

axphase2 = fig.add_subplot(224, autoscale_on=False, xlim=phasexlim2, 
                           ylim=phaseylim2)
axphase2.set_xlabel('$\\theta_2$')
axphase2.set_ylabel('$p_2$')
axphase2.grid()

line, = axanim.plot([],[],lw=2)
timeline1, = axtime.plot([],[],color='b',ms=0,lw=1, label='$\\theta_1$')
timeline2, = axtime.plot([],[],color='g',ms=0,lw=1, label='$\\theta_2$')
#plt.legend((timeline1,timeline2),('$\\theta_1$','$\\theta_2$'))
phaseline1, = axphase1.plot([],[],lw=1)
phaseline2, = axphase2.plot([],[],lw=1)
lines = []
pops = ('o-','.-')
pw = (.5, 2)
mw = (0, 4)
for index in range(2):
    lobj = axanim.plot([],[],pops[index], lw=pw[index],ms=mw[index])[0]
    lines.append(lobj)
lobj = axphase1.plot([],[],lw=2,ms=4, color='b')[0]
lines.append(lobj)
lobj = axphase2.plot([],[],lw=2,ms=4,color='m')[0]
lines.append(lobj)
lobj = axtime.plot([],[],lw=1,ms=0,color='c')[0]
lines.append(lobj)
lobj = axtime.plot([],[],lw=1,ms=0,color='r')[0]
lines.append(lobj)
axtime.legend((lines[4],lines[5]),('$\\theta_1$','$\\theta_2$'),loc=1)

time_template = 'time = %.1fs'
time_text = axanim.text(0.05, .9, '', transform=axanim.transAxes)
pathx = []
pathy = []

phasex1 = []
phasep1 = []
phasex2 = []
phasep2 = []

time_list = []
timex1 = []
timex2 = []

plt.tight_layout()

dt=0.05                 # create a time array from 0..100  

def init():
    for line in lines: 
        line.set_data([],[])
#    line.set_data([],[])
    time_text.set_text('')
    return line, time_text

def animate(i): 
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    
    flag = False
    if len(pathx) ==  200 and flag:
        del pathx[0]
        del pathy[0]
    pathx.append(x2[i])
    pathy.append(y2[i])
    
    time_list.append(1.0*i/20)
    timex1.append(xp1[i])
    timex2.append(xp2[i])
    
    axtime.set_xlim(1.0*i/20-10, 1.0*i/20)
    axtime.set_ylim(timeylim[0],timeylim[1])

    phasex1.append(xp1[i])
    phasep1.append(pp1[i])

    phasex2.append(xp2[i])
    phasep2.append(pp2[i])

    xlist = [pathx, thisx, phasex1, phasex2, time_list, time_list]
    ylist = [pathy, thisy, phasep1, phasep2, timex1, timex2]

    for lnum, line in enumerate(lines): 
        line.set_data(xlist[lnum],ylist[lnum])
    time_text.set_text(time_template%(i*dt))
#    line.set_data(thisx, thisy)
#    path.set_data(pathx, pathy)
#    return line, time_text
    return tuple(lines) + (time_text,)

ani = animation.FuncAnimation(fig, animate, frames=3000, interval=25, 
                              blit = True, init_func=init)

plt.show()
