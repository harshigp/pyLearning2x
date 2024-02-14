# Factorial
f = int(input("enter the number"))
fact = 1
if f==0 :
    print("factorial is 1")
else:
    for i in range(1,f+1):
        fact = fact * i
    print("the factorial is",fact)

