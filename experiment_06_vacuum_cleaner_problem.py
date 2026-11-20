# CSA17 - Artificial Intelligence | Experiment 6 (Manual Ex. 1.6): Vacuum Cleaner Problem
# Name            : V V Naveen Kumar
# Register Number : 192321018

def reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    return "Right" if location == "A" else "Left"

def run(env, location, steps=6):
    print("Initial:", env, "agent at", location)
    for t in range(1, steps + 1):
        action = reflex_agent(location, env[location])
        if action == "Suck":
            env[location] = "Clean"
        elif action == "Right":
            location = "B"
        else:
            location = "A"
        print("Step %d: action=%-5s -> agent at %s, world=%s" % (t, action, location, env))

run({"A": "Dirty", "B": "Dirty"}, "A")


# ============================================================
# OUTPUT
# ============================================================
# Initial: {'A': 'Dirty', 'B': 'Dirty'} agent at A
# Step 1: action=Suck  -> agent at A, world={'A': 'Clean', 'B': 'Dirty'}
# Step 2: action=Right -> agent at B, world={'A': 'Clean', 'B': 'Dirty'}
# Step 3: action=Suck  -> agent at B, world={'A': 'Clean', 'B': 'Clean'}
# Step 4: action=Left  -> agent at A, world={'A': 'Clean', 'B': 'Clean'}
# Step 5: action=Right -> agent at B, world={'A': 'Clean', 'B': 'Clean'}
# Step 6: action=Left  -> agent at A, world={'A': 'Clean', 'B': 'Clean'}
