#Python program to find the factorial of a given number.
x=int(input("enter a number"))
z=1
for i in range(1,x+1):
    z=z*i
    i+=1
print(z)