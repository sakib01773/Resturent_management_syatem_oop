from Menu import Menu
class Resturent:
    def __init__(self,name):
        self.name=name
        self.Users=[]#for storing users
        self.menu=Menu()

    def add_employee(self,employee):
        self.Users.append(employee)
    

    def view_employee(self):
        for emp in self.Users:
            print(emp.name,emp.phone,emp.email,emp.addres,emp.age,emp.designation,emp.salary)
