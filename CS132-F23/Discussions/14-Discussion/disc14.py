import numpy as np
import cs132lib as lib

a = np.array([
    [1, 0, -1,  2, 0],
    [0, 1,  3, -2, 0],
    [0, 0,  0,  0, 1],
    [0, 0,  0,  0, 0]])

print(lib.bmatrix(a))


a[0] += a[1] + 2 * a[2]
a[1] += 3 * a[0] - a[2]
a[2] -= a[1] - a[0]
a[3] += a[0] + a[1]
a[3] += a[2]
print(lib.bmatqrix(a))
print(a[:,:1])
