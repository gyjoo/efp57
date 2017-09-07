print("Press C to convert from Fahrenheit to Celsius.")
print("Press F to convert from Celsius to Fahrenheit.")
choice = input("Your choice: ")

temp = 0 # Set default value

if choice == ("C" or "c"):
	temp = eval(input("\nPlease enter the temperature in Fahrenheit: "))
	print("The temperature in Celsius is %d." %((temp-32)*5/9))
elif choice == ("F" or "f"):	
	temp = eval(input("\nPlease enter the temperature in Celsius: "))
	print("The temperature in Fahrenheit is %d." %((temp*9/5)+32))
else:
	print("You should type C or F. Please try again.")
