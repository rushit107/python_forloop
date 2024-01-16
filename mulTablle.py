#Python program to print a multiplication table of a given number
a=int(input("enter which Number table you want"))
for x in range(1,11):
    print(a," x ",x," = ",a*x)
    x+=1
    