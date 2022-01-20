print("Welcome to BMI Calculator")
height = input("Enter your height in M : ")
weight = input("Enter your weight in kg : ")

bmi = int(weight) / (float(height) ** 2)

print("Your bmi score is", bmi)