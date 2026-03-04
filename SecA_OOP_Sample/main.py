class Person:
    count: int = 0

    def __init__(self):
        Person.count += 1
        self.name: str = ""
        self._age: int = 0
        self.__secret = "Test"

if __name__ == "__main__":
    p1: Person = Person()
    p1.name = "Alice"
    p1._age = 30 
    p1.__secret = "New Secret"

    print(p1.__secret)