#Write a program to display all prime numbers within a range
p=int(input("enter a number"))
q=int(input("enter a number"))
for a in range(p,q):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                break
        else:
            print(a)