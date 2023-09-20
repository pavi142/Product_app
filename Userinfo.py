class User:
    def __init__(self,uid,fname,lname,gender,age,email,contact,addr,usernm,psword):
        self.user_id=uid
        self.first_name=fname
        self.last_name=lname
        self.gender=gender
        self.age=age
        self.email=email
        self.mobile_no=contact
        self.address=addr
        self.user_name=usernm
        self.password=psword

    def __str__(self):
        return f"Name {self.first_name} {self.last_name} "

def user_input():
    uid = input('Enter User ID : ')
    usernm = input('Enter User Name : ')
    psword = input('Enter Password : ')
    fname = input('Enter First Name : ')
    lname = input('Enter Last Name : ')
    age = int(input('Enter Age : '))
    email = input('Enter email address : ')
    addr = input('Enter Address : ')
    contact = input('Enter Contact no : ')
    gendertype = input('Choose Gender : 1. Male 2. Female')
    if gendertype == 1:
        gender = 'Male'
    elif gendertype == 2:
        gender = 'Female'
    else:
        gender = '-'
    return User(uid, fname, lname, gender, age, email, contact, addr, usernm, psword)