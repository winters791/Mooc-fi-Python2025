class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return(f"balance is {round(self.balance,2)} euros")
    def eat_lunch(self):
        if self.balance > 2.60:
            self.balance -= 2.60
    def eat_special(self):
        if self.balance > 4.60:
            self.balance -= 4.60
    def deposit_money(self,amount):
        if amount < 0:
            raise ValueError("Can not deposit less than 0")
        else:
            self.balance += amount


card = LunchCard(10)
print(card)
card.deposit_money(15)
print(card)
card.deposit_money(10)
print(card)
card.deposit_money(-1)
print(card)