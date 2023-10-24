import numpy as np
import cs132lib as lib

a = np.array(
    [[0.95, 0.03],
     [0.05, 0.97]])

b = np.array(
    [[0.7, 0.1, 0.3],
     [0.2, 0.8, 0.3],
     [0.1, 0.1, 0.4]])

# print(lib.reduced_echelon_form(a - np.eye(2)))

# x1 - 0.6x2 = 0
# x2 is free

# x1 + x2 = 1
# (0.6)x2 + x2 = 1
# (1.6)x2 = 1
# x = 1/1.6

# print()
# print(f'x1 = {0.6 * (1 / 1.6)}')
# print(f'x2 = {1/1.6}')

# x1 - 2.25x3 = 0
# x2 - 3.75x3 = 0
# x3 is free

# x1 + x2 + x3 = 1
# (2.25 + 3.75 + 1)x3 = 1
print(f'x3 = {1 / 2.25 + 3.75 + 1}')

print(lib.reduced_echelon_form(b - np.eye(3)))
