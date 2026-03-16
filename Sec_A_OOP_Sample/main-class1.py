# # Declaring a class named Student
# class Student:
#     # Constructor method to initialize the attributes of the class
#     def __init__(self, name, id):
#         # Instance variables to store the name and id of the student (Attributes)
#         self.name = name
#         self.id = id

#     # Method to display the information of the student (instance method)
#     def display_info(self):
#         print(f"Name: {self.name}, ID: {self.id}")

# # Creating an instance of the student class (Also known as an object)
# student1 = Student("Alice", 12345)
# student1.display_info()

# class Mobile:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def call(self):
#         print(f"Calling from {self.brand} mobile...")

#     def details(self):
#         print(f"Brand: {self.brand}, Price: {self.price}")

# mobile1 = Mobile("Samsung", 500)
# # print(mobile1.brand)
# mobile1.call()
# mobile1.details()

# class Person:
#     count = 0 # class variables/static variables are shared among all objects

#     def __init__(self, name):
#         self.name = name # instance variable/attributes are unique to each object
#         Person.count += 1 # Incrementing the count of people created

# p1 = Person("Alice")
# p2 = Person("Bob")
# p3 = Person("Charlie")
# p4 = Person("David")

# print(f"Total people created: {Person.count}")
# print(f"Person 1: {p1.name}")
# print(f"Person 2: {p2.name}")

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
    
#     def deposit(self, amount):
#         if amount <= 0:
#             print("Deposit amount must be positive.")
#             return
#         self.__balance += amount
#         print(f"Deposited {amount}. New balance: {self.__balance}")

#     def show_balance(self):
#         print(f"Current balance: {self.__balance}")

# class Person:
#     def __init__(self, account, name):
#         self.account = account
#         self.name = name

#     def show_account_balance(self):
#         print(f"{self.name}'s account balance:")
#         self.account.show_balance()

# account = BankAccount(1000)
# person = Person(account, "Alice")
# person.show_account_balance()
# person.account.deposit(-500)
# person.show_account_balance()

# name -> This is by default public and can be accessed directly
# _name -> This is a convention to indicate that it is intended for internal use (protected)
# Internal use means that it is not meant to be accessed from outside the class, but it can still be accessed if needed from the same package or subclass.
# __name -> This is name mangling and makes it harder to access from outside (private)

# class BankAccount:
#     def __init__(self, account_name, account_number, balance):
#         self.account_name = account_name
#         self._account_number = account_number
#         self.__balance = balance

# account = BankAccount("Alice", "12345", 1000)
# print(account.account_name) # Accessible directly
# print(account._account_number) # Accessible but should be treated as protected
# print(account.__dict__)
# print(account._BankAccount__balance) # This is how you can access the private variable using name mangling (not recommended)
# # So python does not have direct private variables but uses name mangling to make it harder to access them from outside the class (Pseudo-private).

# Inheritance example (Single Inheritance)
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.eat() # Inherited method from Animal class
dog.bark() # Dog's own method


    