import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt, pi

def norm(v1,v2): 
    return sqrt((v1-v2).dot(v1-v2))

infile = 'init_1.npy'
data = np.load(infile)

Dx1 = max(data[:,0])-min(data[:,0])
Dx2 = max(data[:,2])-min(data[:,2])
Dp1 = max(data[:,4])-min(data[:,4])
Dp2 = max(data[:,5])-min(data[:,5])

V = Dx1*Dx2*Dp1*Dp2
print V

tsteps = len(data[:,0])
muA = 1.0*V/tsteps

#epsilon = sqrt(sqrt(muA))
epsilon = (2*muA/(pi**2))**.25
print epsilon

tx = []
ty = []
to_plot = []
diffs = []
#for i in range(len(data)): 

for i in range(len(data)):
#for i in range(1): 
    print 'Processing member: ' + str(i)
    xi = np.array([data[i][0], data[i][2], data[i][4], data[i][5]])
    recurs = 0
    for j in range(i+1,len(data)): 
#   for j in range(10):
        yj = np.array([data[j][0], data[j][2], data[j][4], data[j][5]])
        if norm(xi,yj) < epsilon:
            recurs += 1
            to_plot.append((i,j))
    print 'Recurrences: ' + str(recurs)

if len(to_plot) > 0: 
    (tx,ty) = zip(*to_plot)
np.savetxt('diffs_out', diffs)

#tx = np.random.rand(1,100)
#ty = np.random.rand(1,100)
marker_style = dict(color='black', linestyle=':',linewidth=0, marker='.',
                    markersize=1.5)

fig, ax = plt.subplots()

if len(tx) > 0: 
    ax.plot(tx,ty, **marker_style)
    ax.plot(ty,tx, **marker_style)
    ax.plot([0,len(data[:,0])],[0,len(data[:,0])], 'k-')
else: 
    tx = []
    ty = []
    ax.plot([0,len(data)],[0,len(data)], 'k-')
ax.set_title('Recurrence Plot \n $\\theta_1 = 120^\circ$, $\omega_1 = 0$, $\\theta_2 = -10^\circ$, $\omega_2 = 0$, $\epsilon =' +str(epsilon) + '$')
ax.set_xlabel('Time $i$')
ax.set_ylabel('Time $j$')

fig.savefig('recurrence_chaotic_4sphere.png',bbox_inches='tight')
