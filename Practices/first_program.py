# JF First Program

ones = ["", "un", "duo", "tre", "quattor", "quin", "sex", "septen", "octo", "novem"]
tens = ["", "vigin", "trigin", "quadragin", "quinquagin", "sexagin", "septagin", "octogin", "nonagin"]
hundreds = ["", "cent", "duocent", "trecent", "quadringent", "quingent", "sescent", "septingent", "octingent", "nongent"]


num = input("Enter a number of any size: ")


for i in range(len(num)//3):
    i *= -3
    print(num[i-2]+num[i-1]+num[i])