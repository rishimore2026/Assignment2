a=int(input("Enter the first side"))
b=int(input("Enter the secound side"))
c=int(input("Enter the third side"))

if (a+b<=c) or (a+c<=b) or (b+c<=a):
    print("No")
else:
    print("Yes")