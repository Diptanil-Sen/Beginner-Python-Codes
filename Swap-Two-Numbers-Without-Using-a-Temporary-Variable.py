def swap(a, b):
    a, b = b, a
    return a, b

# Input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calculation and output
a, b = swap(a, b)
print(f"Swapped numbers: a = {a}, b = {b}")
