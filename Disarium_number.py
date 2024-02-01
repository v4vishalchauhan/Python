"""<<<Code to print all Disarium numbers in a given range>>>"""
"""A number is called Disarium number if the sum of the powers of its digits equals the number itself
for example 135 as 1^1+3^2+5^3=135 so 135 is a disarium number"""


print("Enter the number: ")
l=int(input())
numbers=[]
total=0
for num in range(l+1):
    for i in str(num):
        numbers.append(i)

    for j in numbers:
        total=total+int(j)**(numbers.index(j)+1)

    if int(num)==total:
       print("<<<<We got it "+str(num)+" is a Disarium number>>>>")
       numbers=[]
       total=0


    else:
         print(str(num)+" is not a Disarium number!!")
         numbers=[]
         total=0
