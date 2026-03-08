# class BankAccount:
#     def __init__(self, balance=0):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         print(f"Current balance: {self.__balance}")

# account = BankAccount()
# account.deposit(100)
# account.__owner = "Rahat"
# print(account.__owner)
# account.show_balance()

# class Animal:
#     def eat(self):
#         print("This animal is eating...")

# class Dog(Animal):
#     def bark(self):
#         print("The dog is barking...")

# class Cat(Animal):
#     def meow(self):
#         print("The cat is meowing...")

# d1 = Dog()
# d1.eat()
# d1.bark()
# c1 = Cat()
# c1.eat()
# c1.meow()

# class A:
#     def method_a(self):
#         print("This is method A")

# class B(A):
#     def method_b(self):
#         print("This is method B")

# class C(B):
#     def method_c(self):
#         print("This is method C")

# c1 = C()
# c1.method_a()

class Father:
    def skills1(self):
        print("Programming")

class Mother:
    def skills2(self):
        print("Driving")

class Child(Father, Mother):
    def skills3(self):
        print("Cooking")

c1 = Child()
c1.skills1()
c1.skills2()
c1.skills3()

    