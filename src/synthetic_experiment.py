import numpy as np
from grassmann_utils import random_grassmann_point, grassmann_metric

np.random.seed(0)  # reproducible output

# 1. Create two random points on the Grassmann manifold Gr(10, 3)
# (10 dimensions, 3-dimensional subspace)
Y1 = random_grassmann_point(10, 3)
Y2 = random_grassmann_point(10, 3)

print("Point 1 shape:", Y1.shape)
print("Point 2 shape:", Y2.shape)

# 2. Calculate the distance between them
dist = grassmann_metric(Y1, Y2)
print(f"Geodesic distance between the two subspaces: {dist:.4f}")
