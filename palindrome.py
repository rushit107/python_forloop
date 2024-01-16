#Python program to check if the given string is a palindrome
a=input("enter to check if the word is palindrome or not:")
b=""
for i in a:
    b=i+b
if a==b:
    print("the entered string is palindrome")
    
else :
    print("the entered string is not palindrome")