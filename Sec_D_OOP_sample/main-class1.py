class Person:
    count = 0

    def __init__(self, name: str, age: int):
        self.name = name
        Person.count += 1
        self._age = age
        self.__password = "secret"

    def intro(self) -> None:
        print(f"Hello I am {self.name}.")

    def _get_age(self) -> int:
        return self._age
    
if __name__ == "__main__":
    p1 = Person("Alice", 30)
    p2 = Person("Bob", 25)
    p3 = Person()

    p1.intro()
    p2.intro()
    p3.intro()

    print(f"Total people created: {Person.count}")

