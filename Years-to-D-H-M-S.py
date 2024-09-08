def time_conversion(years):
    days = years * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return days, hours, minutes, seconds

# Input
years = int(input("Enter number of years: "))

# Calculation and output
days, hours, minutes, seconds = time_conversion(years)
print(f"Days: {days}, Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")
