class Item() :
    def __init__(self, input_price, input_quantity) :
        self.price = input_price
        self.quantity = input_quantity

    def get_price(self) :
        return self.price

    def get_quantity(self) :
        return self.quantity

class Order_list(object) :
    def __init__(self) :
        self.tax_rate = 0.055
        self.subtotal = 0
        self.total = 0
        self.list = list()

    def add_item(self, item) :
        self.list.append(item)
        self.subtotal += item.get_quantity() * item.get_price()

    def delete_item(self, item) :
        self.list.remove(item)
        self.subtotal -= item.get_quantity() * item.get_price()

    def get_subtotal(self) :
        return self.subtotal

    def get_tax(self):
        return self.tax_rate * self.subtotal

    def get_total(self) :
        return self.subtotal * ( 1 + self.tax_rate)

my_order = Order_list()
for counter in range(1,4) :
    price = eval(input("Enter the price of item %d: " % counter))
    quantity = eval(input("Enter the quantity of item %d : " % counter))
    my_order.add_item(Item(price, quantity))

print("Subtotal: $%0.2f" % my_order.get_subtotal())
print("Tax: $%0.2f" % my_order.get_tax())
print("Total: $%0.2f" % my_order.get_total())
