#employee
#admin
#customer
from abc import ABC

from order import Order

class User(ABC):
    def __init__(self,name,phone,email,addres):
        self.name = name
        self.phone = phone
        self.email = email
        self.addres = addres


class Customer(User):
    def __init__(self,name,phone,email,addres):
        super().__init__(name,phone,email,addres)
        self.cart=Order()


    def view_menu(self,resturent):
        resturent.menu.show_items()


    def add_to_cart(self,resturent,item_name,quantity):
        item = resturent.menu.find_item(item_name)
        if item is not None:
            if quantity>item.quantity:
                print("quantity Exceeded")

            else:
                item.quantity= quantity
                self.cart.add_item(item)
                print("item Added") 
                   
        else:
            print("item Not found")

    def view_cart(self):
        print("*****MENU****")
        print("Name\t Price\t quantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name} \t{item.price} \t{quantity}")

        print(f"Total Price:{self.cart.total_price()}")

    def pay_bill(self):
        print(f"bil paid {self.cart.total_price()} succesfully")
        self.cart.clear()


class Employee(User):
    def __init__(self,name,phone,email,addres,age,designation,salary):
        super().__init__(name,phone,email,addres)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self,name,phone,email,addres):
        super().__init__(name,phone,email,addres)
        


    def add_employee(self,resturent,employee):
        resturent.add_employee(employee)
        print(f"added user {employee.name}")

    def view_employee(self,resturent):
        resturent.view_employee()

    def add_new_item(self,resturent,item):
        resturent.menu.add_menu_item(item)


    def remove_item(self,resturent,item):
        resturent.menu.remove_item(item)

    def view_item(self,resturent):
        resturent.menu.show_items()



