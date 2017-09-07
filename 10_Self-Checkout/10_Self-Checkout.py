price1 = eval(input("Enter the price of item 1: "))
quantity1 = eval(input("Enter the quantity of item 1: "))

price2 = eval(input("Enter the price of item 2: "))
quantity2 = eval(input("Enter the quantity of item 2: "))

price3 = eval(input("Enter the price of item 3: "))
quantity3 = eval(input("Enter the quantity of item 3: "))

subtotal = price1*quantity1 + price2*quantity2 + price3*quantity3
tax = subtotal*0.055
total = tax + subtotal

print("Subtotal: $%0.2f" %subtotal)
print("Tax: $%0.2f" %tax)
print("Total: $%0.2f" %total)
