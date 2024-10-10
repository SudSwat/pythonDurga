s=input("enter some string:")
l=s.split()
i=len(l)-1
new=[]
while i>=0:
    new.append(l[i])
    i-=1
output=' '.join(new)
print(output)




# output = ""
# # length_words=len(words)
# l=len(words)
#
# for i in range(0,l):
#     # print(words[i],end="")
#     # print(first)
#     if words[i]!=' ':
#         first = words[i]
#         print(first)






