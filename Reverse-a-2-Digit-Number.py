def reverse_2_digit_number(number):
    return int(str(number)[::-1])

# Input
number = int(input("Enter a 2-digit number: "))

# Calculation and output
print("Reversed number:", reverse_2_digit_number(number))
