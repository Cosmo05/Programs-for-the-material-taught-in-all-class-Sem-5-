import numpy as np
import matplotlib.pyplot as plt
from math import *

l = 20
v = 3
xs = 5
tau = 0.2
t = 1.5
dis = np.arange(1,l+1,0.1)

U = []
for n in range(1,51):
    u1 = []
    for x in dis:
        w = n*pi*xs/l
        a = sin(n*pi*xs/l)*exp(-((w*tau)**2/4))
        u = a*sin(n*pi*x/l)*cos(w*t)
        u1.append(u)
    U.append(u1)

array = np.array(U)
u_sum = array.sum(axis = 0)
plt.plot(dis,u_sum)
plt.show()
     


