import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy import misc


photo = 'tiger.jpg'
matt = misc.imread(photo)[:200,:200,:]
plt.imshow(matt)
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0,matt.shape[0]), 
                     ylim=(0,matt.shape[1]))
ax.set_ylim(ax.get_ylim()[::-1])
catmap = ax.imshow(matt)
#ax.imshow(matt)

matt_two = np.array(matt)
N = matt_two.shape[0]

time_template = 'time = %.1fs'
time_text = ax.text(0.05, .9, '', transform=ax.transAxes)

def init(): 
    catmap.set_data(matt)
    time_text.set_text('')
    return catmap, time_text

def animate(i):
    global matt
    global matt_two
    #matt_temp = np.array(matt)

    for x in range(N): 
        for y in range(N): 
            matt_two[x,y] = matt[(2*x+y)%N,(x+y)%N]
    matt = np.array(matt_two)
    catmap.set_data(matt)
    time_text.set_text(time_template%(i))
    return catmap, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(3*N), interval=50, 
                              blit=True, init_func=init)
            
plt.show()

