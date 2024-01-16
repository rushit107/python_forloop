a=[1,2,44,55,2,3,774,36]
e=0
o=0
for i in a:
    if i%2==0:
        e+=1
   
    if i%2!=0:
        o+=1
    
    
print("there are ",e," even numbers in the list")
print("there are ",o," odd numbers in the list")
        