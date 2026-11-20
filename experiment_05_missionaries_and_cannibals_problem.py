# CSA17 - Artificial Intelligence | Experiment 5 (Manual Ex. 1.5): Missionaries and Cannibals Problem
# Name            : V V Naveen Kumar
# Register Number : 192321018

from collections import deque

LOADS = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def valid(m, c):
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False
    if m and m < c:
        return False
    rm, rc = 3 - m, 3 - c
    if rm and rm < rc:
        return False
    return True

def solve():
    start, goal = (3, 3, 1), (0, 0, 0)
    queue = deque([start])
    parent = {start: None}
    while queue:
        cur = queue.popleft()
        if cur == goal:
            path = []
            while cur:
                path.append(cur)
                cur = parent[cur]
            return path[::-1]
        m, c, b = cur
        for dm, dc in LOADS:
            nm, nc = (m - dm, c - dc) if b else (m + dm, c + dc)
            nxt = (nm, nc, 1 - b)
            if valid(nm, nc) and nxt not in parent:
                parent[nxt] = cur
                queue.append(nxt)

path = solve()
print("Steps:", len(path) - 1)
for s in path:
    print("Left bank: M=%d C=%d | Boat: %s | Right bank: M=%d C=%d" %
        (s[0], s[1], "left " if s[2] else "right", 3 - s[0], 3 - s[1]))


# ============================================================
# OUTPUT
# ============================================================
# Steps: 11
# Left bank: M=3 C=3 | Boat: left  | Right bank: M=0 C=0
# Left bank: M=3 C=1 | Boat: right | Right bank: M=0 C=2
# Left bank: M=3 C=2 | Boat: left  | Right bank: M=0 C=1
# Left bank: M=3 C=0 | Boat: right | Right bank: M=0 C=3
# Left bank: M=3 C=1 | Boat: left  | Right bank: M=0 C=2
# Left bank: M=1 C=1 | Boat: right | Right bank: M=2 C=2
# Left bank: M=2 C=2 | Boat: left  | Right bank: M=1 C=1
# Left bank: M=0 C=2 | Boat: right | Right bank: M=3 C=1
# Left bank: M=0 C=3 | Boat: left  | Right bank: M=3 C=0
# Left bank: M=0 C=1 | Boat: right | Right bank: M=3 C=2
# Left bank: M=1 C=1 | Boat: left  | Right bank: M=2 C=2
# Left bank: M=0 C=0 | Boat: right | Right bank: M=3 C=3
