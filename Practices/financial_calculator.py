# JF Financial Calculator
s=0
for j in ["income", "rent/mortgage", "utilities cost", "groceries budget", "transport budget"]:
    p=float(input(f"What is your monthly {j}? $"))
    s+=p
    if j=="income": i=p
    print(f"Your {j} is {round(p/i*100,2)}% of your income.\n")
print(f"You should be saving ${i/10} per month, which is 10% of your income.\n\nWith this budget plan, you will have {i*1.9-s} of spending money per month.")