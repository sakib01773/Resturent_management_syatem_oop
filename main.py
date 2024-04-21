from food_item import FoodItems
from Menu import Menu
from order import Order
from resturent import Resturent
from user import User,Admin,Employee,Customer


resturent = Resturent("PIZZA MARKET")

def Cumstomer_menu():
    name = input("Enter Your name: ")
    email = input("Enter Your email: ")
    phone = input("Enter Your phone: ")
    addres = input("Enter Your addres: ")

    customer= Customer(name=name,email=email,phone=phone,addres=addres)


    while True:
        print(f"Welcome {customer.name}")
        print("********************")
        print("1. View Menu")
        print("2. Add Item To Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        ch = int(input("Enter choice: "))

        if ch==1:
            customer.view_menu(resturent)
        elif ch==2:
            item=input('Enter Item Name: ')
            quantity= int(input("Enter Quantity: "))
            customer.add_to_cart(resturent,item,quantity)
        elif ch==3:
            customer.view_cart()
        elif ch == 4:
            customer.pay_bill()
        elif ch == 5:
            break
        else:
            print("invalid Choice")


def Admin_menu():
    name = input("Enter Your name: ")
    email = input("Enter Your email: ")
    phone = input("Enter Your phone: ")
    addres = input("Enter Your addres: ")

    admin= Admin(name=name,email=email,phone=phone,addres=addres)


    while True:
        print(f"Welcome {admin.name}")
        print("********************")
        print("1. Add new Item")
        print("2. View Items")
        print("3. Delete Items")
        print("4. Add New employee")
        print("5. View Employee")
        print("6. Exit")

        ch = int(input("Enter choice: "))

        if ch==1:
            item_name=input("Enter Item Name: ")
            price=int(input("Enter Price"))
            item_quantity=int(input("Enter Quantity: "))
            item=FoodItems(item_name,price,item_quantity) 
            admin.add_new_item(resturent,item)
        elif ch==2:
            admin.view_item(resturent)
        elif ch==3:
            item_name= input("Enter Item Name: ")
            admin.remove_item(resturent,item_name)
        elif ch == 4:
            name = input("Enter Employee name: ")
            email = input("Enter Employee email: ")
            phone = input("Enter Employee phone: ")
            addres = input("Enter Employee addres: ")
            age = input("Enter Employee age: ")
            designation = input("Enter Employee designation: ")
            salary = input("Enter Employee salary: ")
            employee = Employee(name,phone,email,addres,age,designation,salary)
            admin.add_employee(resturent,employee)
        elif ch == 5:
            admin.view_employee(resturent)
        elif ch == 6:
            break
        else:
            print("invalid Choice")



while True:
    print("\n******************************")
    print("******************************\n")
    print("Welcome To PIZZA MARKET ")
    print("\n******************************")
    print("******************************")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit\n\n")
    print("Enter Your Choice:")
    ch= int(input())

    if ch == 1:
        Admin_menu()
    elif ch ==2:
        Cumstomer_menu()
    elif ch ==3:
        break
    else:
        print("invalid Choice")
    
        
            
