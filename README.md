Final Project for PHYS 405 -- Classical Mechanics

Poincare Recurrence Theorem: Simulations of the Chaotic Double Pendulum and Arnold's Cat Map. 

Ashwin Narayan 

Fall 2014


README

Run *double_pend.py* to simulate a double pendulum with command line arguments 
giving
initial conditions: initial angle 1, initial velocity 1, initial angle 2, initial velocity 2, timesteps, outfile name 

Default: (30 deg, -10 m/s, 0 deg, 0 m/s, 500, "init_temp.npy")

Then run *animate.py* with commandline argument giving the datafile specified above. You can also use "init_1.npy" and "init_2.npy" which are provided and have nice properties. 

Default: "init_temp.npy"

---

Run *recurrence.py* to see cool recurrence plots. 

And run *cat_map.py* to see Arnold's Cat Map work with the tiger photo. This is a 
chaotic map that has recurrence properties, but be patient!