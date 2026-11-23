# CSA17 - Artificial Intelligence | Experiment 43 (Manual Ex. 5.3): Reinforcement Learning Agent (Q-Learning)
# Name            : V V Naveen Kumar
# Register Number : 192321018

import numpy as np

np.random.seed(0)
SIZE, GOAL, PITS = 4, (3, 3), {(1, 1), (2, 3)}
ACTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
ARROWS = ['^', 'v', '<', '>']

def step(state, a):
    r, c = state
    nr = min(max(r + ACTIONS[a][0], 0), SIZE - 1)
    nc = min(max(c + ACTIONS[a][1], 0), SIZE - 1)
    new = (nr, nc)
    if new == GOAL:
        return new, 10, True
    if new in PITS:
        return new, -10, True
    return new, -1, False

Q = np.zeros((SIZE, SIZE, 4))
alpha, gamma, epsilon = 0.1, 0.9, 1.0

for episode in range(3000):
    s, done = (0, 0), False
    while not done:
        if np.random.rand() < epsilon:
            a = np.random.randint(4)
        else:
            a = int(np.argmax(Q[s]))
        s2, reward, done = step(s, a)
        Q[s][a] += alpha * (reward + gamma * np.max(Q[s2]) * (not done) - Q[s][a])
        s = s2
    epsilon = max(0.05, epsilon * 0.998)

print("Learned greedy policy (G = goal, X = pit):")
for r in range(SIZE):
    row = ''
    for c in range(SIZE):
        row += ' G ' if (r, c) == GOAL else ' X ' if (r, c) in PITS else ' %s ' % ARROWS[int(np.argmax(Q[r, c]))]
    print(row)

s, path = (0, 0), [(0, 0)]
while s != GOAL and len(path) < 20:
    s, _, _ = step(s, int(np.argmax(Q[s])))
    path.append(s)
print("\nPath from start:", path)
