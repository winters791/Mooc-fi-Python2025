class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.value = 0
    def add_number(self, number: int):
        self.numbers += 1
        self.value += number
    def count_numbers(self):
        return self.numbers
    def get_sum(self):
        return self.value
    def average(self):
        return self.value/self.numbers
x = 0
stats = NumberStats()
print("Please type in integer numbers:")
while True:
    x = int(input(" "))
    if x == -1:
        break
    stats.add_number(x)
print(f"Numbers added : {stats.count_numbers()}")
print(f"Sum of Numbers: {stats.get_sum()}")
print(f"Mean of Numbers: {stats.average()}")
