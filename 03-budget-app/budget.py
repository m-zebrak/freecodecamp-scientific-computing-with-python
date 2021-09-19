class Category:
    def __init__(self, category: str):
        self.category = category.capitalize()
        self.ledger = []

    def __str__(self) -> str:
        output = [self.category.center(30, '*')]
        output += [f'{line.get("description")[:23]:23}{line.get("amount"):7.2f}' for line in self.ledger]
        output += [f'Total: {self.get_balance():.2f}']
        return '\n'.join(output)

    def deposit(self, amount: float, description: str = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount: float, description: str = '') -> bool:
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def check_funds(self, amount: float) -> bool:
        return self.get_balance() >= amount

    def get_balance(self) -> float:
        return sum([line.get('amount') for line in self.ledger])

    def transfer(self, amount: float, recipient: 'Category') -> bool:
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {recipient.category}')
        recipient.deposit(amount, f'Transfer from {self.category}')
        return True


def create_spend_chart(categories: list[Category]) -> str:
    output = ['Percentage spent by category\n']
    withdrawals = [sum([line.get('amount') for line in cat.ledger if line.get('amount') < 0]) for cat in categories]
    percent_withdrawals = [round(w / sum(withdrawals) * 100) for w in withdrawals]
    names = [cat.category for cat in categories]
    max_len = len(max(names, key=len))
    names = [n.ljust(max_len) for n in names]

    for i in range(100, -1, -10):
        output += [str(i).rjust(3) + '| '] + ['o  ' if percent >= i else ' ' * 3 for percent in percent_withdrawals] \
                  + ['\n']

    output += [' ' * 4 + '-' * (len(categories) * 3 + 1)]
    for i in range(max_len):
        output += ['\n' + ' ' * 5] + [n[i] + '  ' for n in names]

    return ''.join(output)
