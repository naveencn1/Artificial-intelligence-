# CSA17 - Artificial Intelligence | Experiment 45 (Manual Ex. 5.5): Markov Chain Model for Predicting Sequences
# Name            : V V Naveen Kumar
# Register Number : 192321018

import numpy as np

states = ['Sunny', 'Cloudy', 'Rainy']
P = np.array([[0.7, 0.2, 0.1],
            [0.3, 0.4, 0.3],
            [0.2, 0.3, 0.5]])

rng = np.random.RandomState(5)
current = 0
sequence = [states[current]]
for _ in range(9):
    current = rng.choice(3, p=P[current])
    sequence.append(states[current])
print("Simulated 10-day weather:", ' -> '.join(sequence))

today = states.index('Rainy')
print("\nToday is Rainy. Most likely tomorrow:", states[int(np.argmax(P[today]))])
print("Probability distribution for tomorrow:", {s: round(float(p), 2) for s, p in zip(states, P[today])})

after3 = np.linalg.matrix_power(P, 3)[today]
print("Distribution after 3 days:", {s: round(float(p), 3) for s, p in zip(states, after3)})

dist = np.array([1.0, 0.0, 0.0])
for _ in range(100):
    dist = dist @ P
print("\nSteady-state distribution:", {s: round(float(p), 3) for s, p in zip(states, dist)})


# ============================================================
# OUTPUT
# ============================================================
# Simulated 10-day weather: Sunny -> Sunny -> Cloudy -> Sunny -> Rainy -> Cloudy -> Cloudy -> Rainy -> Rainy -> Cloudy
#
# Today is Rainy. Most likely tomorrow: Rainy
# Probability distribution for tomorrow: {'Sunny': 0.2, 'Cloudy': 0.3, 'Rainy': 0.5}
# Distribution after 3 days: {'Sunny': 0.396, 'Cloudy': 0.298, 'Rainy': 0.306}
#
# Steady-state distribution: {'Sunny': 0.457, 'Cloudy': 0.283, 'Rainy': 0.261}
