def cm_to_feet_inches(cm):
    inches_total = cm / 2.54  # 1 inch = 2.54 cm
    feet = inches_total // 12
    inches = inches_total % 12
    return round(feet, 2), round(inches, 2)

# Input
height_cm = float(input("Enter height in centimeters: "))

# Calculation and output
feet, inches = cm_to_feet_inches(height_cm)
print(f"Height: {feet} feet and {inches} inches")