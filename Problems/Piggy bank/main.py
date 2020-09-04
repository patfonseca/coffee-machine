class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def cents_to_dollars(self):
        while self.cents > 99:
            self.dollars += 1
            self.cents -= 100

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        self.cents_to_dollars()


