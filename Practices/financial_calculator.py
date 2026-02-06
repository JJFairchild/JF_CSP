# JF Financial Calculator

def g(p): return round(float(input(f"\nWhat is your monthly {p}? $")),2)
def c(m,v,t): print(f"Your {m} is {v/t*100}% of your income.")
i=g("income")
p=i-sum(c(m,v:=g(m),i) or v for m in ["rent", "utilities", "groceries", "transportation"])
print(f"\nYou should save ${i/10} a month, that is 10% of your income.\n\nYou have ${p-i/10} of spending money each month!")