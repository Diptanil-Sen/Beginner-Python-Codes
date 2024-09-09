def reverse_3_digit_number(number):
    return int(str(number)[::-1])

# Input
number = int(input("Enter a 3-digit number: "))

# Calculation and output
print("Reversed number:", reverse_3_digit_number(number))
