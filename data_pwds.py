"""Code to secure password in form of hash"""
#This code will convert all the passwords into hash so if somehow our database is hacked then also hacker wilnot be able to know the passwords
#During login code will match the hash of entered password and saved password
#To run this code you need to create a pwd_list.txt file and  at line 21 and 32 you have to specify its path


import hashlib
import datetime
import pickle  #importing this to save file in binary format
import re

data_list=[]  #storing all dictionary


def hash_data(nm):  #function to convert data into hash
    return hashlib.sha256(nm.encode()).hexdigest()



def file_loader():  #it will open and load all old data
    try:
        content=open('pwd_list.txt','rb')
        global data_list
        data_list=pickle.loads(content.read())
    except (EOFError):       #If file is empty then this exception will be handled
           data_list=[]


file_loader()


def file_saver():   #it will save new data
    with open('pwd_list.txt','wb') as f:
        pickle.dump(data_list,f)


def input_data(s,i,p,h):
    data={
         'Site':s,
         'Id':i,
         'Password':p,
         'Hint':hint
          }
    data_list.append(data)
    file_saver()


kio=True #just some random variable

try:
    while kio:
        print(""" What would you like to do.
        1.Enter new data
        2.Finding old data
        3.Print blocks
        4.Clear data
        0 Exit""" )


        inp=int(input())

        if inp==1:
                print("Enter name of site: ")
                site=input()
                print("Enter id ")
                ID=input()
                print("Enter password")
                pwd=hash_data(input()+"v4vishal")#v4vishal will act as salt
                print("Enter hint: ")
                hint=input()
                input_data(site,ID,pwd,hint)

        elif inp==2:
            print("Enter site name: ")
            site=input()
            print("Enter id ")
            Id=input()
            print("Enter your password: ")
            pwd=input()

            for i in data_list:

                if i['Id']==Id:
                    if  i['Password']==hash_data(pwd+'v4vishal'): #v4vishal will act as salt
                        print("Login successfull....")
                    else:
                        print("No data found!!!!!")
                        print("Hint:"+i['Hint'])   #hint will be printed when user will enter wrong password
                else:
                     print("Wrong ID")



        elif inp==3:
            print(data_list)

        elif inp==4:
            data_list=[]
            file_saver()


        else:
             kio=False

except:
        print("Enter valid input")