A = eval(input("How much total alcohol get consumed? "))
W = eval(input("How much is your body weight in pounds? "))
gender = input("Are you a man or a woman? (man/woman) ")
H = eval(input("How much hours passed since the last drink? "))
r = 0.73 # Default value is for men

if gender == "woman":
	r = 0.66

BAC = (A * 5.14/W * r) - .015 * H

print("Your BAC is %.2f" %BAC)
if BAC >= 0.08:
	print("It is not legal for you to drive.")
else:
	print("It is legal for you to drive.")
