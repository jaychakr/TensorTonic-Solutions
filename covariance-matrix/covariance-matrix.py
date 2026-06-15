import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    N = X.shape[0]
    if N < 2 or X.ndim != 2:
        return None
    mean = np.mean(X, axis=0)
    X_centered = X - mean
    return X_centered.T @ X_centered / (N - 1)