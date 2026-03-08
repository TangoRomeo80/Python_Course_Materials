# class BankAccount:
#     def __init__(self, balance=0):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         print(f"Current balance: {self.__balance}")

# account1 = BankAccount()
# account2 = BankAccount(100)
# account1.deposit(50)
# account1.show_balance()
# account2.show_balance()
# account1.__balance = 1000
# print(account1.__balance)
# print(account1._BankAccount__balance)
# account1.show_balance()
# print(account1.__dict__)
        
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

dog = Dog()
cat = Cat()
dog.eat()
dog.bark()
cat.eat()
cat.meow()