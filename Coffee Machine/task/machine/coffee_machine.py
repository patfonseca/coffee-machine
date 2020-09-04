class CoffeeMachine:
    def __init__(self):
        self.state = ''
        self.supplies = [[400, 250, 350, 200],  # water 0 - machine, 1 - espresso, 2 - latte, 3 - cappuccino
                         [540, 0, 75, 100],  # milk
                         [120, 16, 20, 12],  # coffee
                         [550, 4, 7, 6]]  # money
        self.cups = 9

    def status(self):
        print('The coffee machine has:')
        print(self.supplies[0][0], 'of water')
        print(self.supplies[1][0], 'of milk')
        print(self.supplies[2][0], 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print(self.supplies[3][0], 'of money')

    def fill(self):
        self.supplies[0][0] += int(input('Write how many ml of water do you want to add:'))
        self.supplies[1][0] += int(input('Write how many ml of milk do you want to add:'))
        self.supplies[2][0] += int(input('Write how many grams of coffee beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))

    def take(self):
        print('I gave you $', self.supplies[3][0])
        self.supplies[3][0] = 0

    def buy(self):
        t = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if t in '123' and self.supplies[0][0] >= self.supplies[0][int(t)] and self.supplies[1][0] >= self.supplies[1][
            int(t)] and self.supplies[2][0] >= self.supplies[2][int(t)] and self.cups > 0:
            for n in range(3):
                self.supplies[n][0] -= self.supplies[n][int(t)]
            self.supplies[3][0] += self.supplies[3][int(t)]
            self.cups -= 1
            print('I have enough resources, making you a coffee!')
        elif t in '123':
            if self.supplies[0][0] < self.supplies[0][int(t)]:
                print('Sorry, not enough water!')
            if self.supplies[1][0] < self.supplies[1][int(t)]:
                print('Sorry, not enough milk!')
            if self.supplies[2][0] < self.supplies[2][int(t)]:
                print('Sorry, not enough coffee beans!')
            if self.cups == 0:
                print('Sorry, not enough disposable cups!')

    def action(self, action):
        self.state = action
        if action == 'remaining':
            self.status()
        elif action == 'fill':
            self.fill()
        elif action == 'take':
            self.take()
        elif action == 'buy':
            self.buy()


marley = CoffeeMachine()

while marley.state != 'exit':
    print()
    to_do = input('Write action (buy, fill, take, remaining, exit):')
    print()
    marley.action(to_do)
