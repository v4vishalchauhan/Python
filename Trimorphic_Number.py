"""Finding Trimorphic Number using Regex module"""
"""A trimorphic number is a number whose cube ends in the number itself.For example  4 whose cube is 64
so 4 is trimorphic number as 64 contains 4  """



import re

print("Enter number")
num=input()

for i in range(0,int(num)+1):
    cube=pow(int(i),3)

    m=str(i)
    k=re.compile(m)
    pattern=k.search(str(cube))
    if pattern!=None:
           print(str(i)+" is a Trimorphic number")

    else:
           print(str(i)+" is a not a Trimorphic number")



