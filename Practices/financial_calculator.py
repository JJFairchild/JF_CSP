# JF Financial Calculator

income = float(input("What is your monthly income? $"))
rent = float(input("What is your monthly rent/mortgage? $"))
utilities = float(input("What is your monthly utilities cost? $"))
groceries = float(input("What is your monthly groceries budget? $"))
transport = float(input("What is your monthly transport budget? $"))

print(f"\nYour rent is ${rent}, which is {round(rent/income*100, 2)}% of your income.")
print(f"Your utilites are ${utilities}, which is {round(utilities/income*100, 2)}% of your income.")
print(f"Your groceries are ${groceries}, which is {round(groceries/income*100, 2)}% of your income.")
print(f"Your transportation is ${transport}, which is {round(transport/income*100, 2)}% of your income.")
print(f"You should be saving ${income/10} per month, which is 10% of your income.")

print(f"\nWith this budget plan, you will have {income*9/10-rent-utilities-groceries-transport} of spending money per month.")