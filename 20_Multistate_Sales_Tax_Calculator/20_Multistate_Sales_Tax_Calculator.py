amount = eval(input("What is the order amount? "))
state = input("What state do you live in? ")
county = input("What county do you live in? ")
tax = 0 # default value is zero

if state in ["Wisconsin", "wisconsin"]:
	if county in ["Eau Claire", "eau claire", "Eau claire"]:
		tax = 0.05
	elif county in ["Dunn", "dunn"]:
		tax = 0.04
elif state in ["Illinois", "illinois"]:
	tax = 0.08
print("The tax is $%.2f." %(amount*tax))
print("The total is $%.2f." %(amount*(1+tax)))
