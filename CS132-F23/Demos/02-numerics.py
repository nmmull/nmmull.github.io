# %%
# INTRO
print(0.1)
print(0.1 + 0.1)
print(0.1 + 0.1 + 0.1) # !!!


#%%
# CLOSER LOOK AT INTRO
def printDec(n):
    print('{:.25f}'.format(n))


print(0.1)
printDec(0.1)
# value is not exact

#%%
print(0.1 + 0.1)
printDec(0.1 + 0.1)
printDec(0.2)
# any thoughts on why this is exact?

#%%
printDec(0.3)
printDec(0.1 + 0.1 + 0.1)
printDec(0.3 - (0.1 + 0.1 + 0.1))

#%%
printDec(0.1 + 0.1 + 0.1 + 0.1)
printDec(0.4)
# floating-point operations do not get the closest representation

#%%
printDec(0.25)
printDec(0.05)
printDec(0.25 + 0.05)
print(0.25 + 0.05)
# any thoughts on why this works?

# %%
# EXAMPLE FROM NOTES
a = 1/8
b = 8
c = 1
printDec(a)
printDec(b)
printDec(c)
print(a * b - c)
# all numbers can be represented exactly

# %%
a = 1/7
b = 7
c = 1
printDec(a)
printDec(b)
printDec(c)
printDec(a * b - c)
# a is not represented exactly 
# but b is
# and we don't lose precision

# %%
a = 1/70
b = 7
c = 0.1
printDec(a)
printDec(b)
printDec(c)
printDec(a * b - c)
# a and b are not represented exactly, and the error gets worse

# %%
# COMMUTATIVITY
a = 7
b = 1/10
c = 1/a
printDec(a)
printDec(b)
printDec(c)
printDec(a * b)
print(a * b * c)

# %%
a = 7
b = 1/10
c = 1/a
printDec(b * c)
print(b * c * a)

# %%
# CLOSENESS
import numpy as np

print(np.finfo('float'))

a = 7
b = 1/10
c = 1/a
print(a * b * c == b * c * a)
print(np.isclose(a * b * c, b * c * a))

# %%
# ILL-CONDITIONED PROBLEMS
a = 10
b = a + 0.0001
c = a + 0.00000001
print(np.isclose(a, b))
print(np.isclose(a, c))
print(1.0 / (b - a))
print(1.0 / (c - a))

# %%
# BEWARE OF SUBTRACTION
a = 999999999999
b = 999999999999999999999999
c = a / 7 / 10 * 7 - a / 10
d = b / 7 / 10 * 7 - b / 10
print(c)
print(d)

# %%
