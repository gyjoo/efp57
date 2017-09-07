months = eval(input("Please enter the number of the month: "))
if months not in range(1,13):
	print("Please type 1 to 12 decimal number.")
else:
	switcher = {
		1: "January",
		2: "Feburary",
		3: "March",
		4: "April",
		5: "May",
		6: "June",
		7: "July",
		8: "August",
		9: "September",
		10: "October",
		11: "November",
		12: "December",
	}
	print("The name of the month is %s." %switcher[months])
