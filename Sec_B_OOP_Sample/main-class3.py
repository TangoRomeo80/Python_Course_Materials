# Overriding happens when a child class provides own implementation of a method that is already defined in its parent class.
# Run time polymorphism and compile time polymorphism
# Method overriding examples:

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     # This is overrriding the sound method of the parent class
#     # So when we call the sound method of the Dog class, it will execute the sound method defined in the Dog class instead of the one in the Animal class.
#     def sound(self):
#         print("Dog barks")

#     def parent_sound(self):
#         self.sound()
#         super().sound()

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

#     def parent_sound(self):
#         self.sound()
#         super().sound()

# dog = Dog()
# cat = Cat()
# dog.parent_sound()
# cat.parent_sound()

# class NafiParent:
#     def cook_biriyani(self):
#         print("Nafi's Parent is cooking biriyani")

# class Nafi(NafiParent):
#     # pass
#     def cook_biriyani(self):
#         print("Nafi is cooking biriyani with extra spices")

# nafi_parent = NafiParent()
# nafi_parent.cook_biriyani()
# nafi = Nafi()
# nafi.cook_biriyani()


# We use super to access parent class method or attributes.
# This prevents duplicate code and parent initialization logic.

# class Animal:
#     def __init__(self, name: str = ""):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name: str = "", breed: str = ""):
#         super().__init__(name)
#         self.breed = breed

#     def show(self):
#         print(f"Dog Name: {self.name}, Breed: {self.breed}")

# dog = Dog("Buddy", "Golden Retriever")
# dog.show()

# Unfortunately, Python does not support method overloading based on the number of parameters or their types.
# class Demo:
#     def add(self, a: int, b: int, c: int) -> int:
#         return a + b + c

#     def add(self, a: int, b: int) -> int:
#         return a + b
    
    
# demo = Demo()
# # This will call the second add method, and the first one will be overridden.
# print(demo.add(1, 2, 3))
# print(demo.add(1, 2))  # This will raise an error because the first add method is overridden.

# So how is overloading handled in Python?
# 1. Default arguments
# class MathOps:
#     def add(self, a: int, b: int, c: int = 0) -> int:
#         return a + b + c
    
# math_ops = MathOps()
# print(math_ops.add(1, 2))  # This will call the add method with default value of c as 0
# print(math_ops.add(1, 2, 3))  # This will call the add method with c as 3

# 2. Variable-length arguments
# class MathOps:
#     def add(self, *args: int) -> int:
#         return sum(args)
    
# math_ops = MathOps()
# print(math_ops.add(1, 2))  # This will call the add method with 2 arguments
# print(math_ops.add(1, 2, 3))  # This will call the
# print(math_ops.add(1, 2, 3, 4))  # This will call the add method with 4 arguments
# print(math_ops.add())  # This will call the add method with no arguments.
# print(math_ops.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,500, 800, 277, 312, 896, 8758959, 2345))

# Type checking method overloading
# class MathOps:
#     def show(self, value):
#         if isinstance(value, int):
#             print(f"Integer value: {value}")
#         elif isinstance(value, str):
#             print(f"String value: {value}")
#         else:
#             print(f"Other type value: {value}")

# math_ops = MathOps()
# math_ops.show(42)  # This will call the show method with an integer
# math_ops.show("Hello")  # This will call the show method with a string
# math_ops.show(3.14)  # This will call the show method with a float

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     # decorator is a function (or class) that takes another function, method, or class 
#     # as an argument and extends or modifies its behavior without explicitly changing its source code.
#     @abstractmethod 
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius: float):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
    
# class Rectangle(Shape):
#     def __init__(self, width: float, height: float):
#         self.width = width
#         self.height = height

#     def show(self):
#         print(f"Width: {self.width}, Height: {self.height}")

#     def area(self):
#         return self.width * self.height

# circle = Circle(5)
# print(f"Area of Circle: {circle.area()}")
# rectangle = Rectangle(4, 6)
# print(f"Area of Rectangle: {rectangle.area()}")
# # shape = Shape()  # This will raise an error because we cannot instantiate an abstract class.

from abc import ABC, abstractmethod

class Employee(ABC):
    company = "ABC Corporation" # This is a class variable, shared by all instances of the Employee class.

    def __init__(self, name: str, salary: int):
        self.name = name
        self.__salary = salary # This is a private variable, it cannot be accessed outside the class. This ensures encapsulation.

    def show_basic_info(self):
        print(f"Employee Name: {self.name}, Company: {self.company}")

    # We use setters and getters to access private variables.
    def set_salary(self, salary: int):
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    @abstractmethod
    def calculate_bonus(self):
        pass

class Manager(Employee):
    # Overriding the calculate_bonus method of the Employee class to provide specific implementation for Manager.
    def calculate_bonus(self):
        return self.get_salary() * 0.2
    
class Developer(Employee):
    # Overriding the calculate_bonus method of the Employee class to provide specific implementation for Developer.
    def calculate_bonus(self):
        return self.get_salary() * 0.8
    
manager = Manager("Alice", 100000)
developer = Developer("Bob", 80000)
manager.show_basic_info()
print(f"Manager Bonus: {manager.calculate_bonus()}")
developer.show_basic_info()
print(f"Developer Bonus: {developer.calculate_bonus()}")