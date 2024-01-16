#Python program to calculate the sum of all numbers from 1 to a given number
z=int(input("enter a number"))
a=0
for s in range(0,z+1):
    a=a+s
    s+=1
print(a)