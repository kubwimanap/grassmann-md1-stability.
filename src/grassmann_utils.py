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
    # Principal angles theta_i: cos(theta_i) are the singular values of Y1^T Y2,
    # sin(theta_i) those of (I - Y1 Y1^T) Y2. Combining both with arctan2 is
    # accurate for small angles, where arccos alone loses about half the digits.
    M = Y1.T @ Y2
    U, cos_t, Vt = svd(M)
    sin_t = svd((Y2 - Y1 @ M) @ Vt.T, compute_uv=False)
    sin_t = np.sort(sin_t)[: len(cos_t)]  # pair the smallest sines with the largest cosines
    angles = np.arctan2(sin_t, cos_t)
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
