import random
import math

def sphere(x):
    return sum(xi ** 2 for xi in x)

def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    solution = [random.uniform(b[0], b[1]) for b in bounds]
    value = func(solution)

    for _ in range(iterations):
        neighbor = [
            max(min(x + random.uniform(-0.1, 0.1), b[1]), b[0])
            for x, b in zip(solution, bounds)
        ]
        n_value = func(neighbor)

        if n_value < value:
            solution = neighbor
            value = n_value

        if abs(n_value - value) < epsilon:
            break

    return solution, value


def random_local_search(func, bounds, iter=1000, epsilon=1e-6):
    solution = [random.uniform(b[0], b[1]) for b in bounds]
    value = func(solution)

    for _ in range(iter):
        rnd_solution = [random.uniform(b[0], b[1]) for b in bounds]
        rnd_value = func(rnd_solution)

        if rnd_value < value:
            solution = rnd_solution
            value = rnd_value

        if abs(rnd_value - value) < epsilon:
            break

    return solution, value

def simulated_annealing(func, bounds, iter=1000, temp=1000, cooling=0.95, epsilon=1e-6):
    solution = [random.uniform(b[0], b[1]) for b in bounds]
    value = func(solution)
    b_solution = solution[:]
    b_value = value

    for _ in range(iter):
        neighbor = [
            max(min(x + random.uniform(-0.1, 0.1), b[1]), b[0])
            for x, b in zip(solution, bounds)
        ]
        n_value = func(neighbor)
        delta = n_value - value
        probability = math.exp(-delta / temp) if delta > 0 else 1

        if random.random() < probability:
            solution = neighbor
            value = n_value

        if value < b_value:
            b_solution = solution[:]
            b_value = value

        temp *= cooling

        if temp < epsilon:
            break

    return b_solution, b_value

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
