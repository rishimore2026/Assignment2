a=int(input("Enter the first number"))
b=int(input("Enetr the secound number"))
c=int(input("Enter the third nuymber"))

largest=0

if a>b and a>c:
    largest=a

if b>a and b>c:
    largest=b

else:
    largest=c

print(largest, "is the largest of the three numbers.")