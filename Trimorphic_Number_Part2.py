"""Finding a Trimorphic Number ina particular range"""
"""A trimorphic number is a number whose cube ends in the number itself.For example  4 whose cube is 64
so 4 is trimorphic number as 64 contains 4  """

print("Enter number")
num=input()

for i in range(0,int(num)+1):


    cube=pow(int(i),3)

    if str(i) in str(cube):
           print(str(i)+" is a Trimorphic Number")
           print("*"*30)
    else:
           print(str(i)+" is not a Trimorphic Number")
           print("*"*30)
