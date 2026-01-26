# JF Financial Calculator

p = []
for j in ["What is your monthly income? $", "What is your monthly rent/mortgage? $", "What is your monthly utilities cost? $", "What is your monthly groceries budget? $", "What is your monthly transport budget? $"]:
    p.append(float(input(j)))
i = float(input())
r = float(input())
u = float(input())
g = float(input())
t = float(input())
print(f"\nYour rent is ${p[1]}, which is {round(p[1]/p[0]*100,2)}% of your income.\nYour utilites are ${p[2]}, which is {round(p[2]/p[0]*100, 2)}% of your income.\nYour groceries are ${p[3]}, which is {round(p[3]/p[0]*100, 2)}% of your income.\nYour transportation is ${p[4]}, which is {round(p[4]/p[0]*100, 2)}% of your income.\nYou should be saving ${p[0]/10} per month, which is 10% of your income.\n\nWith this budget plan, you will have {p[0]*9/10-p[1]-p[2]-p[3]-p[4]} of spending money per month.")