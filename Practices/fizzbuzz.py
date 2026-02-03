# JF FizzBuzz

print(*["Fizz"*(n%3==0)+"Buzz"*(n%5==0) or n for n in range(1,51)],sep="\n")