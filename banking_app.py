def accountcreation():
    print("==================Create a New Account=======================")
    fname=input("Enter your First Name: ")
    lname=input("Enter your last Name: ")
    Nicnum=input("Enter your NIC number: ")
    Dob=input("Enter your Date of birth: ") 
    Contact_num=input("Enter your Contact Number :")
    import random
    acc_num=random.randint(100000,999999)
    print("Your Account number is" ,acc_num )
    print("Do not forgot your account number")
    import datetime
    date=datetime.datetime.now
    import random
    import string
    def generateusername(lrname):
        strnum=''.join(random.choices(string.digits,k=4))
        username=lrname.lower().replace(" ","")+strnum
        return username

    username=generateusername(lname)
    print("Your User name is" ,username)
    print(" Do Not forgot your username")
    

    Newuserdetails=[fname,lname,Nicnum,Dob,Contact_num,username,acc_num]
    return Newuserdetails
    

def User_information():
    with open("User.txt","a") as file:
        file.write(Newuserdetails)

def logintest():
    with open("login.txt","a") as login_file:
        login_file.write(Newuserdetails[-2],[-1])
        Uservari=login_file.readlines()  


with open("login.txt","a") as file:
    



print("================Welcome to SlS Bank=================")
print("1.Login")
print("2.Create New Account")
print("Please Select options 1/2")
logins=int(input("Enter your option: "))
if logins ==1:
   yourusername=input("Enter your username: ")
   youraccountnum=input("Enter your account number: ")
   
   if yourusername == Newuserdetails[-2] and youraccountnum == Newuserdetails[-1]:
      print ("Successfully login")
      
   else:
       print("Invalid Username or password")
"""1


else:
    accountcreation()
     Enter=int(input("If you are continue bank work press 1 : "))
     def deposit():
    global balance
    deposit_amount=int(input("Enter your deposit amount"))
    if deposit_amount>0:
       balance+=deposit_amount
       print(f"Success fully deposited your amount {deposit_amount} now your account balance is {balance}")
    else:
        print("Can't deposit amount your amount must be greater than 0")



def withdraw():
    global balance
    withdrawal_amount=int(input("Enter your withdrawal ammount"))

    

    if withdrawal_amount>0 and withdrawal_amount<=balance:
        balance-=withdrawal_amount
        print(f"Success fully withdrawed money now your account balance is{balance}")
    else:
        print("Can't withdraw money insufficient account balance")
balance=100000  

def main():
    while True:
          print("=============MAIN MENU==============")
          print("1.Deposit")
          print("2.Withdraw")
          print("3.Show balance")
          print("4.Exit")
          options=int(input("Please choose the options (1/2/3/4) : "))
          if options==1:
             deposit()
          elif options==2:
              withdraw()
          elif options==3:
              global balance
              print("Your account balance is",balance)
          elif options==4:
               break 
          else:
              print("Invalid option please choose (1/2/3/4)")
              


main()
  """  