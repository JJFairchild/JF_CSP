# JF First Program

first = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion"]
ones = ["", "un", "duo", "tre", "quattor", "quin", "sex", "septen", "octo", "novem"]
tens = ["", "dec", "vigin", "trigin", "quadragin", "quinquagin", "sexagin", "septagin", "octogin", "nonagin"]
hundreds = ["", "cen", "duocen", "trecen", "quadringen", "quingen", "sescen", "septingen", "octingen", "nongen"]

while True: # Ensure the number entered is in a handleable format
    num = input("Enter any whole number less than 10^3003: ")

    if not num.isdigit():
        print("That's not a valid number. Try again.")
        continue
        
    if len(num) < 3003: break
    else: print("Too large. Try again.")

num = num.lstrip("0") # Ensure the number doesn't have any leading zeroes
if num == "": num = "0"

groups = [] # Create groups of 3 numbers (each group has a separate name)
for i in range(1, len(num)//3*3, 3): groups.insert(0, num[-i-2]+num[-i-1]+num[-i])

remainder = len(num)%3 # Get the leftover numbers that didn't fit into a group
if remainder != 0:
    lead = ""
    for i in range(remainder): lead += num[i]
    groups.insert(0, lead)

full_num = "" # Concatenate everything into a single string
for pos, group in enumerate(groups):
    index = str(len(groups) - pos - 1)
    for i in range(3-len(index)): index = "0"+index
    illion = ""
    if group == "000": continue

    if int(index) <= 10: # Handle numbers less than 10^33
        illion += first[int(index)]
        group = group.lstrip("0")

        full_num += group + " " + illion + " "

    else: # Handle larger numbers
        index = str(int(index)-1)
        for i in range(3-len(index)): index = "0"+index

        illion += ones[int(index[2])]
        illion += tens[int(index[1])]
        illion += hundreds[int(index[0])]

        if illion[-1] == "n": illion += "t" # Fix for pronunciation
        group = group.lstrip("0")

        full_num += group + " " + illion + "illion "

if num == "0": full_num = "0" # Special case for zero
print(full_num.strip())