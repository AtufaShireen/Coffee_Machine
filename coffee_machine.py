class Machine:
    def __init__(self):
        self.water, self.milk, self.beans, self.cups, self.money = 400, 540, 120, 9, 550

    def left(self):
        sym = '$' if self.money > 0 else ''
        print(
            f'The coffee machine has:'
            f'\n{self.water} of water'
            f'\n{self.milk} of milk'
            f'\n{self.beans} of coffee beans'
            f'\n{self.cups} of disposable cups'
            f'\n{sym}{self.money} of money\n')
        self.take_action()

    def check(self, n_water, n_milk, n_beans, n_cups, n_money):
        avail = {'water': self.water - n_water,
                 'milk': self.milk - n_milk,
                 'beans': self.beans - n_beans,
                 'cups': n_cups
                 }
        for key, value in avail.items():
            if value < 0:
                print(f'Sorry, not enough {key}!\n')
                return False
        print('I have enough resources, making you a coffee!\n')

        self.water -= n_water
        self.milk -= n_milk
        self.beans -= n_beans
        self.cups -= n_cups
        self.money += n_money
        return True


    def buy(self):
        coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')

        if coffee == '1':
            self.check(250, 0, 16, 1, 4)
        if coffee == '2':
            self.check(350, 75, 20, 1, 7)
        if coffee == '3':
            self.check(200, 100, 12, 1, 6)
        if coffee == 'back':
            pass
        self.take_action()

    def fill(self):

        self.water += int(input('Write how many ml of water do you want to add:\n'))
        self.milk += int(input('Write how many ml of milk do you want to add:\n'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:\n'))
        print()
        self.take_action()

    def take_action(self):
        try:
            action = input("Write action (buy, fill, take, remaining, exit):\n")
            if action == 'exit':
                exit(0)
        except EOFError:
            exit()
        print()
        if action == 'buy':
            self.buy()
        elif action == 'fill':
            self.fill()

        elif action == 'take':
            print(f'I gave you ${self.money}')
            money = 0
        elif action == 'remaining':
            self.left()

client=Machine()
client.take_action()
