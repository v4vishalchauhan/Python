"""Code to check given number is a Howling Prime or not"""
"""If a number is a prime number and sum of its digits is also a prime number then its a Howling prime number """


print("Enter number: ")
k=int(input())

num_list=[]


def prime_check(n):

    if n<=1:     #'1' is not a prime number
       return False

    for j in range(2,n):
        if n%j==0:
            return False

    else:
        return True


prime_sum=0


for num in range(1,k+1):

    if prime_check(num)==True:

           for i in str(num):
               num_list.append(int(i))       #filing elements of given number into a list

           for l in num_list:
               prime_sum+=l     #adding elements of entered number

           if prime_check(prime_sum)==True:
              print(str(num)+" is a howling prime!!!!!!")
              num_list=[]
              prime_sum=0
           else:
                print(str(num)+" is not a howling prime")
                num_list=[]
                prime_sum=0



    else:
        print(str(num)+" is not a  prime")
        num_list=[]
        prime_sum=0







