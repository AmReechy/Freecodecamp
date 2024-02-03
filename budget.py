


class Category:
    def __init__(self, cat):
        self.ledger = []
        self.cat = cat

    def deposit(self, amount, description= ""):
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self, amount, description= ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -(amount), "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum([amount for amount in [item["amount"] for item in self.ledger]])

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other.cat}')
            other.deposit(amount, f'Transfer from {self.cat}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        header = f'{self.cat.center(30,"*")}'
        details = ""
        for item in self.ledger:
            details += item["description"][:23].ljust(23) + f'{item["amount"]:.2f}'.rjust(7) + '\n'
        total = f'Total: {self.get_balance():.2f}'
        return header + '\n' + details + total

    
def create_spend_chart(cat_list):
    #cat_list = [cat1, cat2, cat3] amount = cat_list[0].ledger[0]['amount']
    #total_spent_each = [sum([-(withdrawn) for withdrawn in [cat_ledger['amount'] for cat_ledger in [cat.ledger for cat in cat_list]] if withdrawn < 0])]
    total_spent_each = []
    for cat in cat_list:
        total = 0
        for ledger in cat.ledger:
            amount = ledger["amount"]
            if amount < 0:
                total += amount
        total_spent_each.append(-(total))
    overall_total = sum(total_spent_each)
    percent_each = [int(round(total/overall_total * 100, -1)) for total in total_spent_each]

    each_line = []
    for num in range(100, -1, -10):
        num_str = f'{num}| '.rjust(5)
        for perc in percent_each:
            if perc >= num:
                num_str += 'o  '
        each_line.append(num_str + '\n')
    #return "".join(each_line) + ('_'*(3*len(cat_list))).rjust(3*len(cat_list) + 4)

    cat_names = [cat.cat for cat in cat_list]
    print(cat_names)
    names_tag = []

    for i in range(0, max([len(name) for name in cat_names])):
        tag = " "*5
        for name in cat_names:
            try:
                tag += f"{name[i]}  "
            except:
                tag += "   "
        tag += '\n'
        names_tag.append(tag)

    return "".join(each_line) + ('_'*(3*len(cat_list))).rjust(3*len(cat_list) + 4) + '\n' + "".join(names_tag)

                
    