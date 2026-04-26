# class Student:
#     # class attribute
#     college="NIT Srinagar"
#     name="Anonymous"

#     # default constructor
#     def __init__(self):
#         print("Default constructor called")
    
#     # parameterized constructor
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("Adding new student to our DB")
#         print(self)
    
#     def say_hello(self):
#         print("Hello, I am a student of",self.college,"and my name is",self.name)
    
#     def get_marks(self):
#         return self.marks

# s1=Student("Abishek",90)
# print("Name :",s1.name)
# print("Marks :",s1.marks)

# s2=Student("Suresh",80)
# print("Name :",s2.name)

# # both class and object can access class attributes
# print("College :",Student.college)
# print("College :",s1.college)

# s1.say_hello()
# print("Marks of",s1.name,"are",s1.get_marks())


# class Student:
#     college="NIT Srinagar"
#     def __init__(self,name,marks_math,marks_phy,marks_chem):
#         self.name=name
#         self.marks_math=marks_math
#         self.marks_phy=marks_phy
#         self.marks_chem=marks_chem

#     def print_avergage(self):
#         sum=self.marks_math+self.marks_phy+self.marks_chem
#         print("Average marks of",self.name,"are",sum/3)
    
#     @staticmethod
#     def print_college():
#         print("College name is",Student.college)

# s1=Student("Abishek",90,80,100)
# s1.print_avergage()
# Student.print_college()

# class Car:
#     def __init__(self):
#         self.clutch=False
#         self.accelerator=False
#         self.brake=False
    
#     def start(self):
#         self.clutch=True
#         self.accelerator=True
#         self.brake=False
#         print("Car started")

# car=Car()
# car.start()


# class Account:
#     def __init__(self,acc_no,balance):
#         self.acc_no=acc_no
#         self.balance=balance

#     def debit(self,amount):
#         if self.balance>=amount:
#             self.balance-=amount
#             print("Amount :",amount,"debited successfully")
#             print("Current Balance:",self.balance)
#         else:
#             print("Insufficient balance")
    
#     def credit(self,amount):
#         self.balance+=amount
#         print("Amount :",amount,"credited successfully")
#         print("Current Balance:",self.balance)
    
#     def printBalance(self):
#         print("Current Balance:",self.balance)

# acc1=Account(123,1000)
# acc1.credit(500)
# acc1.debit(1000)
# acc1.debit(1000)

class Emp:
    def __init__(self,name,salary,password):
        self.name=name
        self.salary=salary
        self.__password=password

    def change_password(self,new_password):
        self.__password=new_password
        print("Password changed successfully")
        print("New Password is",self.__password)

emp1=Emp('John',50000,123)
print(emp1)
print("Employee Name:",emp1.name)
print("Employee Salary:",emp1.salary)
#print("Employee Password:",emp1.__password)

emp1.change_password(456)

# del emp1.salary
# print("Employee Name:",emp1.name)
# print("Employee Salary:",emp1.salary)

# del emp1
# print(emp1)