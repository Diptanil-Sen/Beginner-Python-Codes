def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap and output
a, b = swap_with_temp(a, b)
print(f"After swapping: a = {a}, b = {b}")
