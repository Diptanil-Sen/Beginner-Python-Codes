def manhattan_distance(p, q):
    return sum(abs(p[i] - q[i]) for i in range(3))

# Points
P = (1, 2, 3)
Q = (2, 1, 0)

# Calculation and output
print("Manhattan distance:", manhattan_distance(P, Q))
