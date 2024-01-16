#Python for loop to print the multiples of 3 using range() function
i=int(input("enter any number"))
for x in range(1,i+1):
    if x%3==0:
        print(x)
    