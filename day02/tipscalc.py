print("Welcome to the Tip Calculator")
bill_amount = input("Enter the bill amount : ")
percentage_tip = input("Enter the amount of tip you would like to give. 10, 12, or 15? ")
people = input("Enter the number of people you are sharing the bill with: ")

total_amount = float(bill_amount) + (float(bill_amount)*int(percentage_tip)/100)
individual_amount = total_amount / int(people)
final = round(individual_amount,2)
print("Each person should pay ",final)