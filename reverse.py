n = input("Enter the string:")
# print(n[::-1])
#
# for x in reversed(n):
#     print(x,end='')
#
# print()
# print(''.join(reversed(n)))

i=len(n)-1
output=''
while i>=0:
    output=output+n[i]
    i-=1
print(output)


