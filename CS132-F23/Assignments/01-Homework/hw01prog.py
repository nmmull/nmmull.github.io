#%%
import numpy as np
from matplotlib import pyplot

def sub_error(n):
    return abs(n / 7 / 10 * 7 - n / 10)

def next_error(start):
    # TODO
    return 1.0 # CHANGE THIS LINE TOO0

R = np.arange(15)
X = 10.0 ** R
Y = np.array([ next_error(x) for x in X ])

#%%
pyplot.plot(X, Y)
pyplot.yscale('log')
pyplot.xscale('log')
pyplot.show()

#%%
