# JF First Program

ones = ["", "un", "duo", "tre", "quattor", "quin", "sex", "septen", "octo", "novem"]
tens = ["", "vigin", "trigin", "quadragin", "quinquagin", "sexagin", "septagin", "octogin", "nonagin"]
hundreds = ["", "cent", "duocent", "trecent", "quadringent", "quingent", "sescent", "septingent", "octingent", "nongent"]


num = int(input("Enter a number of any size: "))
string = "e" + str(num)
location = string.find("e")-len(string)

groups = []
i = -1
while abs(i) < len(str(string)):
    
    if location in range(i, i-3, -1):
        pass

    groups.append(int(string[i]+string[i-1]+string[i-2]))
    i -= 3

for group in groups:
    one = num % 10
    ten = num // 10 % 10
    hundred = num // 100 % 10

    print(hundred, ten, one)