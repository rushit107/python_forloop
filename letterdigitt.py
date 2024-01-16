# Python program that accepts a string and calculates the number of digits and letters.

a=input("enter characters:")
d=0
l=0
for i in a:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1

print("the word contains ",d," digits and ",l," letters")

        