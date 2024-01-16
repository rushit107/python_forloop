#Calculate the cube of all numbers from 1 to a given number
a=int(input("enter a number:"))
for i in range(1,a+1):
    print("the cube of ",i," is:",i*i*i)
    i+=15
    