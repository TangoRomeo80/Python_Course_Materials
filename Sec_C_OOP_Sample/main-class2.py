# class Student:
#     department = "CSE"

#     # Constructor
#     def __init__(self, name: str = "", grade: str = "", balance: float = 0.0) -> None:
#         self.name = name
#         self._grade = grade # Protected attribute (Also can be considered internal use only)
#         self.__balance = balance # Private attribute (Pseudo-private)

#     # Method to reveal the balance
#     # Getter/Setter methods are commonly used to access private attributes
#     def get_balance(self) -> float:
#         return self.__balance
    
#     def set_balance(self, amount: float) -> None:
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print("Balance cannot be negative.")

# s1 = Student("Bob", "A", 1000.0)
# s2 = Student()
# s2._grade = "B"
# # print(s2._grade)

# s1.__balance = 500
# print(s1.get_balance())
# print(s1.__balance)
# print(s1._Student__balance) # Accessing the private attribute using name mangling

# # print(s1.__dict__)

# # print(f"Student 1: {s1.name}, Grade: {s1._grade}, Balance: {s1.get_balance()}")
# # print(f"Student 2: {s2.name}, Grade: {s2._grade}, Balance: {s2.get_balance()}")

class Info:
    def __init__(self, species: str = "Unknown", age: int = 0) -> None:
        self.sepcies = species
        self.age = age

    def display_info(self) -> None:
        print(f"Species: {self.sepcies}, Age: {self.age}")

class Animal:
    def __init__(self, info: Info, name: str = "Unknown") -> None:
        self.info = info # Composition: Animal has an Info object as an attribute
        self.name = name

    def eat(self) -> None:
        print("Animal is eating.")

class Dog(Animal): # Inheritance: Dog is a subclass of Animal
    def bark(self) -> None:
        print("Dog is barking.")

class Cat(Animal):
    def meow(self) -> None:
        print("Cat is meowing.")

d1 = Dog(Info("Canine", 3), "Buddy")
c1 = Cat(Info("Feline", 2), "Whiskers")
d1.eat()  # Inherited method
d1.bark()  # Dog's own method
c1.eat()  # Inherited method
c1.meow()  # Cat's own method

