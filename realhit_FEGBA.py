# Visualization of real hit chance as a function of displayed hit chance 
# for FE6/7/8
import matplotlib.pyplot as plt
import numpy.random as nprnd

disp_hit = [i for i in range(101)]
real_hit = []

num_trials = 10000 # reduce noise

j = 0

while ( j < len(disp_hit) ): # O(NT * len(disp_hit))
    i = 0
    hit_ct = 0.0
    while ( i < num_trials ):
        rand_one = nprnd.randint(0,100)
        rand_two = nprnd.randint(0,100)
        avg_val = (rand_one + rand_two) / 2
        if (avg_val < disp_hit[j]): # register a hit
            hit_ct += 1.0
        i += 1
    real_hit.append(hit_ct / 100.0)
    j += 1

plt.plot(disp_hit, real_hit)
plt.xlabel('Display Hit')
plt.ylabel('True Hit')
plt.show()	