'''
*
**
***
****
***
**
*

'''
n=int(input("Enter the row count number:"))
for i in range(n+1):
    for j in range(i+1):
        print("*",end='')
    print()
for k in range(n,-1,-1):
    for l in range(k):
        print("*",end='')
    print()



