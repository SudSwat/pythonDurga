'''
*
**
***
****
*****

'''

def fun():
    n = int(input("Enter the no. of rows to form the pattern:"))
    for i in range(n+1):
        for j in range(i+1):
            print("*",end='')
        print()

fun()
