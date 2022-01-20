age = input("Enter your age : ")

years_left = 90 - int(age)
days_remaining = years_left * 365
weeks_remaining = years_left * 52
months_remaining = years_left * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")