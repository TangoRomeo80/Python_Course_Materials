class Person:
    count: int = 0

    def __init__(self, name: str = "Person", age: int = 0, secret: str = "Secret") -> None:
        Person.count += 1
        self.name: str = name
        self._age: int = age
        self.__secret: str = secret

    def reveal_secret(self) -> str:
        return self.__secret

if __name__ == "__main__":
    p1 = Person("Alice", 30, "Loves Python")
    p2 = Person()

    print(f"Total people created: {Person.count}")
    print(f"{p1.name} is {p1._age} years old.")
    print(f"{p2.name} is {p2._age} years old.")
    print(p1.reveal_secret())

