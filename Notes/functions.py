# JF, Functions Notes

def hello(name):
    print(f"Hello {name}!")

def full_name(first, last):
    return f"{first} {last}"

hello(full_name("Tia", "LaRose"))

def fact(n):
    product = 1
    for i in range(1,n+1): product *= i
    return product


num = 1

def add():
    return num + 1

print(add())
