# CSA17 - Artificial Intelligence | Experiment 37 (Manual Ex. 4.7): Genetic Algorithm for Optimising a Function
# Name            : V V Naveen Kumar
# Register Number : 192321018

import random

random.seed(3)
BITS, POP, GENS = 5, 8, 10
CROSS_RATE, MUT_RATE = 0.9, 0.05

def decode(ch):
    return int(''.join(map(str, ch)), 2)

def fitness(ch):
    return decode(ch) ** 2

def select(pop):
    return max(random.sample(pop, 3), key=fitness)

def crossover(a, b):
    if random.random() < CROSS_RATE:
        p = random.randint(1, BITS - 1)
        return a[:p] + b[p:], b[:p] + a[p:]
    return a[:], b[:]
def mutate(ch):
    return [1 - g if random.random() < MUT_RATE else g for g in ch]

pop = [[random.randint(0, 1) for _ in range(BITS)] for _ in range(POP)]
for gen in range(GENS + 1):
    best = max(pop, key=fitness)
    print("Generation %2d best x = %2d f(x) = %3d avg f = %.1f" %
        (gen, decode(best), fitness(best), sum(map(fitness, pop)) / POP))
    new_pop = [best] # elitism
    while len(new_pop) < POP:
        c1, c2 = crossover(select(pop), select(pop))
        new_pop += [mutate(c1), mutate(c2)]
    pop = new_pop[:POP]


# ============================================================
# OUTPUT
# ============================================================
# Generation  0 best x = 30 f(x) = 900 avg f = 320.4
# Generation  1 best x = 30 f(x) = 900 avg f = 660.2
# Generation  2 best x = 30 f(x) = 900 avg f = 829.5
# Generation  3 best x = 31 f(x) = 961 avg f = 833.2
# Generation  4 best x = 31 f(x) = 961 avg f = 865.9
# Generation  5 best x = 31 f(x) = 961 avg f = 869.0
# Generation  6 best x = 31 f(x) = 961 avg f = 907.0
# Generation  7 best x = 31 f(x) = 961 avg f = 953.4
# Generation  8 best x = 31 f(x) = 961 avg f = 891.8
# Generation  9 best x = 31 f(x) = 961 avg f = 796.0
# Generation 10 best x = 31 f(x) = 961 avg f = 862.0
