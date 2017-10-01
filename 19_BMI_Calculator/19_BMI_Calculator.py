weight = eval(input("What is your weight? (kg) "))
height = eval(input("How tall are you? (m) "))

bmi = weight / (height * height) # Use kilograms and meters

print("Your BMI is %.1f." %bmi)

if 18.5 < bmi < 25:
	print("You are within the ideal weight range.")
else:
	print("You are overweight. You should see your doctor.")
