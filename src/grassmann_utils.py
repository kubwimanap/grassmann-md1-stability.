import numpy as np
from scipy.linalg import qr, svd

def random_grassmann_point(n, p):
    """
    Generates a random point on the Grassmann manifold Gr(n, p).
    Returns an orthonormal matrix Y of size (n x p).
    """
    # Generate a random matrix and compute its QR decomposition to get orthonormal columns
    A = np.random.randn(n, p)
    Q, R = qr(A, mode='economic')
    return Q

def grassmann_metric(Y1, Y2):
    """
    Computes the Grassmann distance (geodesic distance) between two subspaces.
    """
    # Compute principal angles using SVD
    U, s, Vt = svd(Y1.T @ Y2)
    # The diagonal elements of s are the cosines of the principal angles
    # Distance is the square root of the sum of squared principal angles
    angles = np.arccos(np.clip(s, -1.0, 1.0))
    return np.sqrt(np.sum(angles**2))

def project_to_tangent(Y, G):
    """
    Projects a Euclidean gradient G onto the tangent space of the Grassmann manifold at point Y.
    Formula: P_G = (I - Y*Y^T) * G
    """
    n, p = Y.shape
    I = np.eye(n)
    # (I - YY^T)G
    tangent_vec = (I - Y @ Y.T) @ G
    return tangent_vec

def retraction(Y, eta):
    """
    Retraction step: moves a point Y on the manifold in the direction of tangent vector eta
    and maps it back to the manifold (typically using QR decomposition).
    """
    # QR decomposition of (Y + eta)
    Y_new, R = qr(Y + eta, mode='economic')
    return Y_new
