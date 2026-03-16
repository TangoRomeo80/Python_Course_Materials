# Multilevel Inheritance
# class A:
#     def method_a(self) -> None:
#         print("Method A from class A")

# class B(A):
#     def method_b(self) -> None:
#         print("Method B from class B")

# class C(B):
#     def method_c(self) -> None:
#         print("Method C from class C")

# c_instance = C()
# c_instance.method_a()  # Inherited from A
# c_instance.method_b()  # Inherited from B

# Multiple inheritance (Child inherits from multiple parents)
# class Father:
#     def skill1(self) -> None:
#         print("Driving")

# class Mother:
#     def skill2(self) -> None:
#         print("Painting")

# class Child(Father, Mother):
#     def skill3(self) -> None:
#         print("Coding")

# c = Child()
# c.skill1()  # Inherited from Father
# c.skill2()  # Inherited from Mother

# Using super()
# super() is used to call methods or constructors of the parent class
# class Animal:
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Animal.count += 1

# class Dog(Animal):
#     def __init__(self, name, breed):
#         self.name = name
#         # super().__init__(name)  # Call the constructor of the parent class
#         self.breed = breed

#     def show(self):
#         print(f"Name: {self.name}, Breed: {self.breed}")  # Accessing parent class attribute using super()

# d = Dog("Buddy", "Golden Retriever")
# # print(d.__dict__)
# d.show()

# Polymorphism
# Method overriding: A child class can provide a specific implementation of a method that is already defined in its parent class
# class Animal:
#     def make_sound(self) -> None:
#         print("Animal makes a sound")

# class Dog(Animal):
#     def make_sound(self) -> None:
#         print("Dog barks")

# class Cat(Animal):
#     def make_sound(self) -> None:
#         print("Cat meows")

# animals = [Dog(), Cat()]
# for animal in animals:
#     animal.make_sound()  # Polymorphic behavior: same method name, different implementations

# Python does not support method overloading in traditional sense like java or c++.
# The followings will not work as expected:
# class Demo:
#     def add(self, a, b):
#         return a + b
    
#     def add(self, a, b, c):
#         return a + b + c
    
# d = Demo()
# print(d.add(1, 2))

# There are ways to achieve this behaviour
# 1. Using default arguments
# class MathOps:
#     def add(self, a, b, c=0):
#         return a + b + c
    
# m = MathOps()
# print(m.add(1, 2))      # Output: 3
# print(m.add(1, 2, 3))   # Output: 6

# 2. Variable length arguments
# class MathOps:
#     def add(self, *args):
#         return sum(args)

# m = MathOps()
# print(m.add(1, 2))          # Output: 3
# print(m.add(1, 2, 3))       # Output: 6
# print(m.add(1, 2, 3, 4))    # Output: 10
# print(m.add())
# print(m.add(1, 5, 7, 215439845327, 12345678901234567890, 9, 12, 3, 342879324))

# 3. Type checking inside the method
# class Display:
#     def show(self, data):
#         if isinstance(data, int):
#             print(f"Integer: {data}")
#         elif isinstance(data, str):
#             print(f"String: {data}")
#         else:
#             print(f"Unsupported type: {type(data)}")

# d = Display()
# d.show(42)          # Output: Integer: 42
# d.show("Hello")     # Output: String: Hello
# d.show(3.14)        # Output: Unsupported type: <class 'float'>

# ABC (Abstract Base Class) and Interfaces
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod # @ represents decorators. Decorators modify the behaviour of a method or a class without explicit modification.
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, width: float, height: float) -> None:
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
# class Circle(Shape):
#     def __init__(self, radius: float) -> None:
#         self.radius = radius

#     def area(self):
#         import math
#         return math.pi * self.radius ** 2
    
# r = Rectangle(5, 10)
# c = Circle(7)
# print(f"Area of Rectangle: {r.area()}")
# print(f"Area of Circle: {c.area()}")

# Full example combining all concepts
from abc import ABC, abstractmethod

class Employee(ABC):
    company: str = "TechCorp" # Class variable shared by all instances

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # Private attribute (Pseudo-private, implementing encapsulation)

    def show_basic_info(self):
        print(f"Name: {self.name}, Company: {Employee.company}")

    # getter and setter for the private attribute
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, amount):
        # Hiding implementaiton details (Abstraction)
        if amount >= 0:
            self.__salary = amount
        else:
            print("Salary cannot be negative.")

    @abstractmethod
    def bonus(self):
        pass

class Manager(Employee):
    def bonus(self):
        return self.get_salary() * 0.1  # Managers get a 10% bonus
    
class Developer(Employee):
    def bonus(self):
        return self.get_salary() * 0.5  # Developers get a 50% bonus
    
m = Manager("Alice", 80000)
d = Developer("Bob", 60000)
m.show_basic_info()
print(f"{m.name}'s Bonus: {m.bonus()}")
d.show_basic_info()
print(f"{d.name}'s Bonus: {d.bonus()}")
    

        