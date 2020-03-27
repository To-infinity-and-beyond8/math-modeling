import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as inti
z = np.arange(0,100,100)
def prelomlenie_function (n,z):
    n = n0 + a*z
    return n
a = 3
n0 = 1
n_1 = a, n0
sol=inti.odeint(prelomlenie_function,n_1,z)
fig, ax = plt.subplots()
plt.plot(sol[:,0],sol[:,2],color='y')
plt.xlim(-6*100, 6*100)
plt.ylim(-6*100, 6*100)


plt.show()
