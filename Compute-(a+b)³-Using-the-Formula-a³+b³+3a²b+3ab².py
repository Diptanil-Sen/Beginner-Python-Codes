def cube_sum(a, b):
    return (a**3) + (b**3) + (3 * a**2 * b) + (3 * a * b**2)

# Input
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Calculation and output
result = cube_sum(a, b)
print(f"(a + b)^3 = {result}")