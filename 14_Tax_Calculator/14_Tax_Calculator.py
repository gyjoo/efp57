order_amount = eval(input("What is the order amount? "))
state = input("What is the state? ")

if state=="WI":
	print("The subtotal is $%.2f." %order_amount)
	print("The tax is $%.2f." %(order_amount*0.055))
	print("The total is $%.2f." %(order_amount*1.055))
elif state=="MN":
	print("The total is $%.2f" %order_amount)
