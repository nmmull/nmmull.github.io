import numpy as np

a = np.array([
    [1/60, 1/6, 19/60, 1/60, 1/60,  1/60],
    [7/15, 1/6, 19/60, 1/60, 1/60,  1/60],
    [7/15, 1/6,  1/60, 1/60, 1/60,  1/60],
    [1/60, 1/6,  1/60, 1/60, 7/15, 11/12],
    [1/60, 1/6, 19/60, 7/15, 1/60,  1/60],
    [1/60, 1/6,  1/60, 7/15, 7/15,  1/60]])


# step 4: compute eigenvector
eigenvalues, eigenvectors = np.linalg.eig(a)


steady_state = np.real(eigenvectors)[:,0]
steady_state /= np.sum(steady_state)

print()
print(steady_state)

# step 5: display indice (pages) in order of rank
page_rank = np.argsort(steady_state)[::-1] + 1

print()
print(page_rank)
