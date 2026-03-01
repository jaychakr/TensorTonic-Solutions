import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    n, m = len(A), len(A[0])
    transpose = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            transpose[i][j] = A[j][i]
    return transpose