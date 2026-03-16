# Heirerchical Inheritance
# class A:
#     def method1(self):
#         print("This is method 1 of class A")

# class B(A):
#     def method2(self):
#         print("This is method 2 of class B")

# class C(A):
#     def method3(self):
#         print("This is method 3 of class C")

# c = C()
# c.method1()  # Inherited from class A
# b = B()
# b.method1()  # Inherited from class A

# Multilevel Inheritance
# class A:
#     def method1(self):
#         print("This is method 1 of class A")

# class B(A):
#     def method2(self):
#         print("This is method 2 of class B")

# class C(B):
#     def method3(self):
#         print("This is method 3 of class C")

# c = C()
# c.method1()  # Inherited from class A
# c.method2()  # Inherited from class B

# Multiple Inheritance
# class Father:
#     def skill1(self):
#         print("Driving")

# class Mother:
#     def skill2(self):
#         print("Painting")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.skill1()  # Inherited from Father
# c.skill2()  # Inherited from Mother

# What is Polymorphism
# Polymorphism allows us to use a single Behaviour(Method) in different ways based on different inputs or contexts(Classes).
# We can achieve polymorphism through method overriding and method overloading.
# Method Overriding
# Method overriding happens when a child class provides its own version of a method that already exists in the parent class.
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     # pass
#     def sound(self):
#         print("Cat meows")

# d = Dog()
# d.sound()  # Output: Dog barks
# c = Cat()
# c.sound()  # Output: Cat meows

# While overriding, we can write duplicate parent initialization logics in the child class.
# So we use super() to point to parent class and call the parent initialization logic in the child class.
# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, breed):
#         super().__init__("Buddy")
#         # self.name = name  # Initialize the name attribute inherited from Animal
#         self.breed = breed  # Initialize the breed attribute specific to Dog

#     def show_info(self):
#         print(f"Name: {self.name}, Breed: {self.breed}")

# d = Dog("Golden Retriever")
# d.show_info()  # Output: Name: Buddy, Breed: Golden Retriever

# Method Overloading
# Python does not support method overloading in the traditional sense. So the following code will not work as expected.
# class Demo:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c
    
# d = Demo()
# print(d.add(1, 2))
# print(d.add(1, 2, 3))

# But we can achieve method overloading using default arguments or variable-length arguments or type checking.
# 1. Using Default Arguments
# class Demo:
#     def add(self, a, b, c=0):
#         return a + b + c

# d = Demo()
# print(d.add(1, 2))
# print(d.add(1, 2, 3))

# 2. Using Variable-Length Arguments
# class Demo:
#     def add(self, *args):
#         return sum(args)
    
# d = Demo()
# print(d.add(1, 2))
# print(d.add(1, 2, 3))
# print(d.add())
# print(d.add(1, 2, 3, 4, 5))

# 3. Using Type Checking
# class Demo:
#     def show(self, data):
#         if isinstance(data, int):
#             print(f"Integer: {data}")
#         elif isinstance(data, str):
#             print(f"String: {data}")
#         else:
#             print(f"Other type: {data}")

# d = Demo()
# d.show(10)  # Output: Integer: 10
# d.show("Hello")  # Output: String: Hello
# d.show(3.14)  # Output: Other type: 3.14

# Abstract classes and interfaces
# from abc import ABC, abstractmethod # ABC means Abstract Base Class

# class Shape(ABC):
#     # @ Represents decorator. This is used to modify the behaviour of a method or a class without changing its source code.
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

#     def perimeter(self):
#         return 2 * 3.14 * self.radius
    
# r = Rectangle(4, 5)
# print(f"Area of Rectangle: {r.area()}")
# print(f"Perimeter of Rectangle: {r.perimeter()}")
# c = Circle(3)
# print(f"Area of Circle: {c.area()}")
# print(f"Perimeter of Circle: {c.perimeter()}")

# Combined example
from abc import ABC, abstractmethod

class Employee(ABC):
    company = "ABC Corporation" # Class variable shared by all employees

    def __init__(self, name, salary):
        self.name = name  # Instance variable unique to each employee
        self.__salary = salary # Private variable, not accessible outside the class (Pseudo-private) implementing ENCAPSULATION

    def show_basic_info(self):
        print(f"Name: {self.name}, Company: {Employee.company}")

    # Getter setter methods for salary
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        # ABSTRACTION by hiding the implementation details of salary validation
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive")

    @abstractmethod
    def calculate_bonus(self):
        pass

# INHERITANCE by creating a child class Manager that inherits from the Employee class and can access its properties and methods
class Manager(Employee):
    # Override the calculate_bonus method to provide a specific implementation for managers(POLYMORPHISM)
    def calculate_bonus(self):
        return self.get_salary() * 0.1  # Managers get a 10% bonus

class Developer(Employee):
    # Override the calculate_bonus method to provide a specific implementation for developers(POLYMORPHISM)
    def calculate_bonus(self):
        return self.get_salary() * 0.5  # Developers get a 50% bonus
    
m = Manager("Alice", 80000)
m.show_basic_info()
print(f"Manager Bonus: {m.calculate_bonus()}")
d = Developer("Bob", 60000)
d.show_basic_info()
print(f"Developer Bonus: {d.calculate_bonus()}")
