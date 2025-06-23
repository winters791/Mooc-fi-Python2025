class Person:
    def __init__(self, name: str):
        parts = name.split(" ")
        self.first = parts[0]
        self.last = parts[1]
    def return_first_name(self):
        return self.first
    def return_last_name(self):
        return self.last


if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())