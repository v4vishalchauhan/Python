"""Code to check given number is a strange number or not"""


import math

print("Enter number: ")
num=int(input())

root=math.sqrt(num)
square=float(num**2)
print(root)
print(square)




square_list=[]
square_root_list=[]

for j in str(square):
    if j==".":   #removing "." from adding into the list
        continue
    square_list.append(j)

rounded_squreroot=round(root,3)#roundoff of root of given number to 3 digits


for k in str(rounded_squreroot):
    if k==".":  #removing "." from adding into the list
        continue
    square_root_list.append(k)


for i in square_list:
    if i in square_root_list:
       print("Given number is strange number")
       print(i)
       break
    else:
         print("Given number is not strange number")
         break

