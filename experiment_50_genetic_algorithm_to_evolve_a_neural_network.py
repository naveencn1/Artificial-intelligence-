# CSA17 - Artificial Intelligence | Experiment 50 (Manual Ex. 5.10): Genetic Algorithm to Evolve a Neural Network
# Name            : V V Naveen Kumar
# Register Number : 192321018

import numpy as np

rng = np.random.RandomState(11)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([0, 1, 1, 0], dtype=float)
N_GENES, POP, GENS = 13, 80, 300

def forward(w, X):
    W1, b1 = w[:6].reshape(2, 3), w[6:9]
    W2, b2 = w[9:12], w[12]
    hidden = np.tanh(X @ W1 + b1)
    return 1 / (1 + np.exp(-(hidden @ W2 + b2)))

def fitness(w):
    return -np.mean((forward(w, X) - y) ** 2)

def tournament(pop, fit, k=4):
    idx = rng.randint(0, len(pop), k)
    return pop[idx[np.argmax(fit[idx])]]

pop = rng.randn(POP, N_GENES)
for gen in range(GENS + 1):
    fit = np.array([fitness(w) for w in pop])
    if gen % 50 == 0:
        print("Generation %3d best MSE = %.5f" % (gen, -fit.max()))
    order = np.argsort(-fit)
    new_pop = [pop[order[0]], pop[order[1]]] # elitism
    while len(new_pop) < POP:
        p1, p2 = tournament(pop, fit), tournament(pop, fit)
        mask = rng.rand(N_GENES) < 0.5 # uniform crossover
        child = np.where(mask, p1, p2)
        mutate = rng.rand(N_GENES) < 0.15 # Gaussian mutation
        child = child + mutate * rng.randn(N_GENES) * 0.4
        new_pop.append(child)
    pop = np.array(new_pop)

best = pop[0]
print("\nBest evolved network on XOR:")
for xi, out in zip(X, forward(best, X)):
    print(xi.astype(int), "->", round(float(out), 3), "=>", int(out > 0.5))


# ============================================================
# OUTPUT
# ============================================================
# Generation   0 best MSE = 0.22725
# Generation  50 best MSE = 0.00014
# Generation 100 best MSE = 0.00000
# Generation 150 best MSE = 0.00000
# Generation 200 best MSE = 0.00000
# Generation 250 best MSE = 0.00000
# Generation 300 best MSE = 0.00000
#
# Best evolved network on XOR:
# [0 0] -> 0.0 => 0
# [0 1] -> 1.0 => 1
# [1 0] -> 1.0 => 1
# [1 1] -> 0.0 => 0
