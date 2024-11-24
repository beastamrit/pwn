a=int(input("Enter a number"))
b=int(input("Enter a number"))
while b:
    x=b
    b=a%b
    a=x
print(a)