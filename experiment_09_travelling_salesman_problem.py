# CSA17 - Artificial Intelligence | Experiment 9 (Manual Ex. 1.9): Travelling Salesman Problem
# Name            : V V Naveen Kumar
# Register Number : 192321018

from itertools import permutations

cities = ['A', 'B', 'C', 'D']
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]

def tour_cost(order):
    cost = 0
    for i in range(len(order)):
        cost += dist[order[i]][order[(i + 1) % len(order)]]
    return cost

best_cost, best_tour = float('inf'), None
for perm in permutations(range(1, len(cities))):
    tour = (0,) + perm
    c = tour_cost(tour)
    print(' -> '.join(cities[i] for i in tour + (0,)), "cost =", c)
    if c < best_cost:
        best_cost, best_tour = c, tour

print("\nBest tour:", ' -> '.join(cities[i] for i in best_tour + (0,)))
print("Minimum cost:", best_cost)


# ============================================================
# OUTPUT
# ============================================================
# A -> B -> C -> D -> A cost = 95
# A -> B -> D -> C -> A cost = 80
# A -> C -> B -> D -> A cost = 95
# A -> C -> D -> B -> A cost = 80
# A -> D -> B -> C -> A cost = 95
# A -> D -> C -> B -> A cost = 95
#
# Best tour: A -> B -> D -> C -> A
# Minimum cost: 80
