# Multilevel inheritance
# class A:
#     def method_a(self):
#         print("Method A")

# class B(A):
#     def method_b(self):
#         print("Method B")

# class C(B):
#     def method_c(self):
#         print("Method C")

# c = C()
# c.method_a()  # Inherited from class A
# c.method_b()  # Inherited from class B

# Multiple inheritance
# class Father:
#     def skills1(self):
#         print("Programming")

# class Mother:
#     def skills2(self):
#         print("Cooking")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.skills1()  # Inherited from Father
# c.skills2()  # Inherited from Mother

# Method overloading in python
# Method overloading is not supported in python in traditional sense.
# class Demo:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c
    
# d = Demo()
# print(d.add(1, 2))
# print(d.add(1, 2, 3))

# Method overriding in python can be done in 3 ways:
# 1. Using default arguments
# class MathOps:
#     def add(self, a, b, c=0):
#         return a + b + c
    
# m = MathOps()
# print(m.add(1, 2))      # Output: 3
# print(m.add(1, 2, 3))   # Output: 6

# 2. Using variable-length arguments
# class MathOps:
#     def add(self, *args):
#         return sum(args)
    
# m = MathOps()
# print(m.add(1, 2))          # Output: 3
# print(m.add(1, 2, 3))       # Output: 6
# print(m.add(1, 2, 3, 5, 123, 489, 902, 127, 1762347668566, 1293867, 9023584789235746))

# 3. Using type checking
# class MathOps:
#     def show(self, value):
#         if isinstance(value, int):
#             print(f"Integer: {value}")
#         elif isinstance(value, str):
#             print(f"String: {value}")
#         else:
#             print(f"Other type: {value}")

# m = MathOps()
# m.show(42)          # Output: Integer: 42
# m.show("Hello")     # Output: String: Hello
# m.show(3.14)        # Output: Other type: 3.14

# So in overloading we are defining multiple methods with same name but different parameters.
# If someone says python supports method overloading, then it is imprecise. We can only simulate method overloading behavior using above mentioned techniques.

# Method overriding
# Method overriding happens when a child class provides its own implementation of a method that is already defined in its parent class.
# class Parent:
#     def cook_biriyani(self):
#         print("Parent is cooking biriyani")

# class Child(Parent):
#     def cook_biriyani(self):
#         print("Child is cooking biriyani with more spices")

#     def check_parent_and_child_biriyani(self):
#         super().cook_biriyani() 
#         self.cook_biriyani()     

# # p = Parent()
# # p.cook_biriyani()
# c = Child()
# c.check_parent_and_child_biriyani()

# Usage of super()
# super() is used to call methods, attributes, or constructors of the parent class
# We use super() to prevent duplication of parent initialization code

# class Animal:
#     def __init__(self, name: str = ""):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name: str = "", breed: str = ""):
#         super().__init__(name)  # Call the parent class constructor to initialize the name attribute
#         self.breed = breed

#     def display_info(self):
#         print(f"Name: {self.name}, Breed: {self.breed}")

# d = Dog("Buddy", "Golden Retriever")
# d.display_info()  # Output: Name: Buddy, Breed: Golden Retriever

# Abstract Base Class in python
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     # Decorators in python are used to modify the behavior of a function or a class.
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
    
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
# c = Circle(5)
# print(f"Area of Circle: {c.area()}")  # Output: Area of Circle: 78.5
# r = Rectangle(4, 6)
# print(f"Area of Rectangle: {r.area()}")  # Output: Area of Rectangle: 24
# # Abstract base classes cannot have instances, so the following line will raise an error
# # s = Shape()  # This will raise TypeError: Can't instantiate abstract class Shape with abstract methods area

from abc import ABC, abstractmethod

class Employee(ABC):
    company = "ABC Corp" # Class variable

    def __init__(self, name: str, salary: float):
        self.name = name
        self.__salary = salary # Private variable, implementing encapsulation

    # Getter and setter methods are used to access and modify private variables
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary: float):
        if salary < 0:
            print("Salary cannot be negative.")
        else:
            self.__salary = salary

    def display_basic_info(self):
        print(f"Name: {self.name}, Company: {Employee.company}")

    @abstractmethod
    def bonus(self):
        pass

# Both inheriting Employee ABC and implementing bonus method
class Manager(Employee):
    def bonus(self):
        return self.get_salary() * 0.2
    
class Developer(Employee):
    def bonus(self):
        return self.get_salary() * 0.5
        
m = Manager("Alice", 50000)
m.display_basic_info()  # Output: Name: Alice, Company: ABC Corp
print(f"Manager Salary: {m.get_salary()}")  # Output: Manager Salary: 50000
print(f"Manager Bonus: {m.bonus()}")  # Output: Manager Bonus: 10000.0
d = Developer("Bob", 40000)
d.display_basic_info()  # Output: Name: Bob, Company: ABC Corp
print(f"Developer Salary: {d.get_salary()}")  # Output: Developer Salary: 40000
print(f"Developer Bonus: {d.bonus()}")  # Output: Developer Bonus: 8000.0



