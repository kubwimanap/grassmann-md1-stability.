# grassmann-md1-stability

Python utilities for optimization on the Grassmann manifold, developed for the manuscript

> P. Kubwimana, B. Prabhakar Reddy, J. M. Mkenyeleye.
> *Stochastic Stability Analysis of Grassmann Manifold Optimization Under State-Dependent Gradient Noise.*
> Manuscript under review, 2026.

**Contact:** Pascal Kubwimana, Department of Mathematics and Statistics, University of Dodoma — kubwimanap4@gmail.com

## Status

This repository currently contains the basic Grassmann-manifold building blocks used in the project. The scripts that produce the tables and figures of the manuscript have not been added yet; they will be published here together with the paper.

## Contents

```
src/
  grassmann_utils.py      random points on Gr(n, p), geodesic distance,
                          tangent-space projection, QR retraction
  synthetic_experiment.py small example: distance between two random subspaces
requirements.txt
```

`grassmann_utils.py` provides:

| Function | Description |
|---|---|
| `random_grassmann_point(n, p)` | orthonormal `n × p` basis of a random `p`-dimensional subspace |
| `grassmann_metric(Y1, Y2)` | geodesic distance `sqrt(sum θᵢ²)` from the principal angles `θᵢ` |
| `project_to_tangent(Y, G)` | Riemannian gradient `(I − YYᵀ)G` of a Euclidean gradient `G` |
| `retraction(Y, eta)` | QR retraction of `Y + eta` back to the manifold |

## Usage

Requires Python 3.9 or later.

```bash
pip install -r requirements.txt
python src/synthetic_experiment.py
```

## License

MIT — see [LICENSE](LICENSE).
