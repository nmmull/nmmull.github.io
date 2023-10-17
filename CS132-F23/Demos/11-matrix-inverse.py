import numpy as np

# invertible matrix
a = np.array(
    [[1., 2, 5],
     [0, 1, 3],
     [1, 0, 0]])

# inverse of a
ainv = np.linalg.inv(a)

# a with the identity on the right
aid = np.hstack([a, np.eye(3)])

# row reductions
# TODO


print()
print("------------------------------")
print("The matrix [ A I ]:")
print("------------------------------")
print(aid)

print()
print("------------------------------")
print("Augmented matrix for Ax = e1:")
print("------------------------------")
print(aid[:,:4])

print()
print("------------------------------")
print("Augmented matrix for Ax = e2:")
print("------------------------------")
print(aid[:,[0, 1, 2, 4]])

print()
print("------------------------------")
print("Augmented matrix for Ax = e3:")
print("------------------------------")
print(aid[:,[0, 1, 2, 5]])
