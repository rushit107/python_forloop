#Python program to check if a given number is an Armstrong number
a=int(input("enter a number to check if it is a armstrong number or not:"))
p=str(a)
z=0
for i in p:
    z=(int(i)*int(i)*int(i))+z
if z==a:
    print(a," is an armstrong number")
else:
    print(a," a is not an armstrong number")


#this feature is added in feature1 branch and not in master branch
Aa=10
print(Aa)