height = float(input("Enter your height in M:"))
weight = float(input("Enter your weight in kg:"))

bmi = weight / height ** 2

bmi = round(bmi)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, and you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, and you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, and you are slightly overweight.") 
elif bmi < 35:
    print(f"Your bmi is {bmi}, and you are obese.")
else:
    print(f"Your bmi is {bmi}, and you are clinically obese.")