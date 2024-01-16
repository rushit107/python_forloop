# Python program to count the total number of digits in a number.

a=int(input("enter a number"))
b=0
c=str(a)
for i in c:
    b+=1
print("no. of digits in the input is",b)
