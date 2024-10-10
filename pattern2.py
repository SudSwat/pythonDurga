'''
*****
****
***
**
*
'''
n=int(input("Enter the no. of rows that you want to make the shape:"))
#range(start,stop,step)
for i in range(n,-1,-1):
    # print(i)
    for j in range(i+1):
        print("*",end='')
    print()










