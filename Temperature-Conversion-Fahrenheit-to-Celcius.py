def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Input
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Calculation and output
print("Temperature in Celsius:", fahrenheit_to_celsius(fahrenheit))
