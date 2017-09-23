class Country:
    def __init__(self):
        self.federal_tax = 0
        self.state_tax = 0
    def calc_tax(self, order_amount):
        return order_amount * (1 + self.federal_tax + self.state_tax)

class US(Country):
    def __init__(self):
        super(US, self).__init__()
        self.federal_tax = 0.077

class Wisconsin(US):
    def __init__(self):
        super(Wisconsin, self).__init__()
        self.state_tax = 0.152

class Minnesota(US):
    def __init__(self):
        super(Minnesota, self).__init__()
        self.state_tax = 0.285

class Canada(Country):
    def __init__(self):
        super(Canada, self).__init__()
        self.federal_tax = 0.055

class Ontario(Canada):
    def __init__(self):
        super(Ontario, self).__init__()
        self.state_tax = 0.122

order_amount = eval(input("What is the order amount? "))
state = input("What is the state? (WI, MN, ON) ")

hometown = Country()

try:
    if state=="WI":
        hometown = Wisconsin()
    elif state=="MN":
        hometown = Minnesota()
    elif state=="ON":
        hometown = Ontario()
    else:
        raise
except:
    print("You should put one of those : WI, MN, ON")
    exit()
print("The total is $%.2f." %order_amount)
print("The tax is $%.2f." %(hometown.calc_tax(order_amount)))
print("You should pay $%.2f." %(order_amount*1.055))
