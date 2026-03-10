
class Person:
    count = 0

    def __init__(self):
        self.name = "John Doe"
        Person.count += 1
        self._age = 30
        self.__password = "secret"

    # This will not work because the __init__ method is already defined above. Uncommenting this will cause an error.
    # def __init__(self, name: str, age: int):
    #     self.name = name
    #     Person.count += 1
    #     self._age = age
    #     self.__password = "secret"

    def introduce(self):
        return f"My name is {self.name}."
    
    def __set_password(self, password: str):
        self.__password = password


    


