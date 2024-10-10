
word =input("Enter the string:")
subs =input("Enter the substring:")
flag=False
match=-1
count=0
while True:
    match=word.find(subs,match+1,len(word))
    if match==-1:
        break
    print("found at index:", match)
    flag=True
    count += 1
if flag==False:
    print("Not found")
print("the no. of occurences",count)




# word =input("Enter the string:")
# subs =input("Enter the substring:")
# # word="best in python"
# count=0
# for each in word:
#     match=word.find(subs)
#     # count+=1
#     if match==-1:
#         break
#     count+=1
# print("Word count is:{},using length function:{}, match:".format(count,len(word)),match)
#
