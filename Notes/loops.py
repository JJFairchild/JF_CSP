# JF Loops Notes

import random

start = 0
while start<=10:
    print(start)
    start+=1

goose=random.randint(5,20)
count=1
while count!=goose:
    print("Duck")
    count+=1
print("GOOSE!")

num=random.randint(1,100)
while True:
    guess=int(input("Pick a number between 1 and 100: "))
    if guess<num: print("Too small! Try again.\n")
    elif guess>num: print("Too large! Try again.\n")
    else:
        print(f"You guessed it! The number was {num}.")
        break

names = ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Jake"]
for name in names:
    print(f"Hello {name}!")

nums = [3,653,854,62,68,548,6596535386407,586427,6653,539,757,3647]
for num in nums:
    print(f"{num}-10 = {num-10}")