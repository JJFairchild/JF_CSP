# JF Conditionals Notes

"""num = 1000

if num < 10 and num > -10:
    print(f"{num} is a single digit number")
elif num < 100:
    print(f"{num} is a double digit number")
else:
    print(f"{num} is a triple digit number")
    print(". . . .or is it?")
    if num**2 > 1000:
        print(f"Surprise number! {num**2}")"""

name = input("What is your name?: ").strip().title()

if name == "Arthur":
    print("Hello, King Arthur!")
    quest = input("What is your quest?: ").strip().capitalize()
    if "Holy Grail" in quest.title():
        print("Good luck!")
    else:
        print(f"{quest} is a lame quest.")
else:
    print(f"Hello {name}. You are not a king.")