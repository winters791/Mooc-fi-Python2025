class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return(f"balance is {self.balance} euros")
card = LunchCard(50)
print(card)