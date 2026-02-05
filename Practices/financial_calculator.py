# JF Financial Calculator

"""
What is your monthly income: $3000
What is your monthly rent/mortgage: $1200
What is your monthly utilities: $200
What is your monthly groceries: $250
What is your monthly transportation: $500

Your rent is $ 1200.00 and that is 40 % of your income.
Your utilities are $ 200.00 and that is 7 % of your income.
Your groceries are $ 250.00 and that is 8 % of your income.
Your transportation is $ 500.00 and that is 17 % of your income.
You should save $ 300.00 a month, that is 10 % of your income.
You have $ 550.00 of spending money each month! 
"""

def g(p): return round(float(input(f"\nWhat is your monthly {p}? $")),2)
def c(m,t): print(f"Your {m} is {g(m)/t*100}% of your income.")
i=g("income")
for m in ["rent/mortgage","utilities","groceries","transportation"]: c(m,i)
print(f"You should save ${i/10} a month, that is 10% of your income.\nYou have ${i}")