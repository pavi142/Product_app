from Userinfo import user_input,User
from implementation import Dmart
from Productinfo import product_input
dservice = Dmart()
user_list=[]
while True:
    print('''
    ====================================
    ========== 1) Sign In ==============
    ========== 2) Sign Up ==============
    ====================================
    ''')
    choice = int(input("Enter your Choice:"))
    if choice == 1:
        print("Sign In Section")
        username = input('Enter User Name : ')
        password = input('Enter Password : ')
        is_login_success = False
        for user in user_list:
            if user.user_name == username and user.password == password:
                print('Login Successfull...!')
                is_login_success = True
                break
        if is_login_success:
            print('''
                                    1. Add Product
                                    2. Delete Product
                                    3. Update Product
                                    4. Search Product(ID,CATEGORY,VENDOR)
                                    5. Max Price Product
                                    6. Min Price Product
                                    7. Search Product In Price Range(X,Y)
                                    8. List Product
                        ''')
            prch = int(input('Enter Your Choice : '))
            if prch == 1:
                prod = product_input()
                dservice.add_product(prod)
            elif prch == 2:
                pid = int(input('Enter Product Id For Delete : '))
                dservice.delete_product(pid)
            elif prch == 3:
                print('Update Product Code')
            elif prch == 4:
                pid = int(input('Enter Product Id For Search : '))
                prod = dservice.search_product(pid)
                print(prod)
            elif prch == 5:
                print('Max Price Product Code')
            elif prch == 6:
                print('Min Price Product Code')
            elif prch == 7:
                print('Search By PriceRange Product Code')
            elif prch == 8:
                prods = dservice.list_product()
                print(prods)
            else:
                print('Enter Valid Choice : ')

        else:
            print('Invalid Crendentails...!')
    elif choice == 2:
        print("Sign Up Section")
        user = user_input()
        user_list.append(user)
        print(f'{user.user_name} Successfully Registered...!')
    else:
        print("Invalid choice")

    ch = input('Do you want to continue : ')
    if ch.lower() in ['n','no']:
        break

print('Program Completed...!')