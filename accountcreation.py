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

accountcreation()

