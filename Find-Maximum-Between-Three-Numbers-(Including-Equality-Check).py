def find_maximum(a, b, c):
    if a >= b:
        if a >= c:
            if a == b or a == c:
                return f"{a} is the largest, but there are equal numbers."
            return f"{a} is the largest."
        else:
            return f"{c} is the largest."
    else:
        if b >= c:
            if b == a or b == c:
                return f"{b} is the largest, but there are equal numbers."
            return f"{b} is the largest."
        else:
            return f"{c} is the largest."

# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Output
print(find_maximum(a, b, c))
