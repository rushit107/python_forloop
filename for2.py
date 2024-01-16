# Python program to calculate the sum of all the odd numbers within the given range.

a=int(input("enter a number:"))
z=0
for x in range(1,a,2):
    z=z+x
    x+=1
print(z)
