# %%
import numpy as np

# numpy arrays like python lists but optimized for linear algebra and mathematical computation

# %%
# you can create a numpy array from a python list

x = np.array([1., 2, 3])
print("simply numpy array")
print(x)

# %%
# vectors are represented as above
a = np.array([4., 5, 6])
print("example of a vector")
print(a)

# note: we typically put a float in the vector so that all values are floats

# %%
# note: strictly speaking, this is represented like a point, as a row we could write
a_ = np.array([[4.], [5], [6]])
print("example of a vector in column form")
print(a_)

# but this is uncommon, and almost always unnecessary
# %%
# vector addition works as expected

print("vector addition example")
print(x)
print("+")
print(a)
print("=")
print(x + a)

# %%
# same with vector scaling
print("vector scaling example")
print("2\n*")
print(a)
print("=")
print(2 * a)

# %%
# matrices are represented as 2D numpy arrays
b = np.array(
    [[0.0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]
)

print("matrix example")
print(b)

# 2D numpy arrays must have fixed width and height
print()
try:
    b = np.array(
    [[0.0, 1, 2],
     [3, 4, 5],
     [6, 7]]
    )
except:
    print("we can't build 2D numpy arrays that aren't matrices")

# %%
# we can get rows of a matrix by indexing

print("row index example")
print("a matrix:")
print(b)
print()
print("row 1 of this matrix:")
print(b[1])

# note the zero indexing

# %%
# we can get columns of a matrix by indexing on a tuple
print("entry index example")
print("a matrix:")
print(b)
print()
print("entry at row 1 and column 0 in the same matrix:")
print(b[1, 0])

# %%
# we can also index multiple columns at a time with a list, which allows us to do swaps

print("index multiple rows example")
print()
print("matrix before swap:")
print(b)
print()
print("matrix after swap")
b[[0, 1]] = b[[1, 0]]
print(b)

# %%
# adding and scaling rows also works as expected

print("adding and scaling rows example")
print()
print("matrix before scale and add:")
print(b)
print()
print("matrix after scale and add")
b[0] += 2 * b[1]
print(b)

# %%
# we can get information about the size of a numpy array with .shape

print("shape example")
print()
print("(row, column) of")
print(b[1:])
print()
print(b[1:].shape)

# %%
# Hopefully this is enough to get you started

# Please read the tutorial on numpy linked on the course website