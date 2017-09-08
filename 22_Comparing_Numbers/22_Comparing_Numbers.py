num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num3 = eval(input("Enter the third number: "))

largest_num = 0 # Initialize

if num1 > num2 and num1 > num3:
	largest_num = num1
elif num2 > num1 and num2 > num3:
	largest_num = num2
elif num3 > num1 and num3 > num2:
	largest_num = num3

print("The largest number is %d." %largest_num)
