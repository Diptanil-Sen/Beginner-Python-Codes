def day_of_year(day, month):
    return (month - 1) * 30 + day

# Input
day = int(input("Enter day: "))
month = int(input("Enter month: "))

# Output
print("Day of the year:", day_of_year(day, month))
