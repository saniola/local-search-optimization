# Local Search Optimization

Python implementations of three classic local-search optimization algorithms, applied to minimizing the sphere function `f(x) = sum(x_i^2)` over a bounded domain.

## Algorithms

- **Hill Climbing** — iteratively moves to a neighboring point if it improves the objective value.
- **Random Local Search** — samples random points within the bounds and keeps the best one found.
- **Simulated Annealing** — accepts worse neighbors with a probability that decreases over time (cooling schedule), allowing escape from local minima.

## Stack

- Python 3 (standard library only: `random`, `math`)

## Usage

```bash
python main.py
```

Each algorithm prints its resulting solution and objective value for the sphere function over the domain `[-5, 5] x [-5, 5]`.
