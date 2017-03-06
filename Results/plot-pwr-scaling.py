#!/Users/slayer/Software/Install/anaconda2/bin/python
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.pyplot import show
cores = [12544, 50176, 137984, 275968]
time = [407.8, 123.4, 54.8, 39.6]
tperfect = [407.8, 102.0, 37.1, 18.5]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(cores, time, 'ko-')
ax.plot(cores, tperfect, 'ko:')
leg = ax.legend(("measured", "linear"), loc="lower left")
ax.grid(True)
ax.set_xlabel("Cores")
ax.set_ylabel("Solver Time (m)")
ax.set_title("Time vs. Cores for PWR900 with Preconditioned RQI")
ax.set_xlim([10000, 300000])
#ax.set_xticks([40000, 80000, 120000, 160000, 200000])
show()
