"""Code to find given number is a emirp number or not"""
"""Emirp numbers:prime nubers whose reverse is also a prime number for example:17 is a
prime number as well as its reverse 71 is also a prime number hence its a emirp number.."""



def prime_check(k):
  n=int(k)
  if n<=1:
    return False

  for i in range(2,n):
    if n%int(i)==0:
      return False
  else:
    return True


print("Enter the number: ")
l=int(input())

for num in range(l+1):
    if prime_check(num)==True:
      d=str(num)[::-1]
      if prime_check(d)==True:
        print("$$$We got it....."+str(num)+" is a Emirp number$$$")
    else:
        print(str(num)+ "  is not a emirp number..")