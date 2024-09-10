import math

def euclidean_distance(p, q):
    return math.sqrt(sum((p[i] - q[i]) ** 2 for i in range(3)))

# Points
P = (1, 2, 3)
Q = (2, 1, 0)

# Calculation and output
print("Euclidean distance:", euclidean_distance(P, Q))
