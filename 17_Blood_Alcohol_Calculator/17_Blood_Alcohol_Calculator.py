# Declaration parts
BAC_RATE_MEN = 0.73
BAC_RATE_WOMEN = 0.66

class inputException(Exception):
	def __init__(self, value):
		self.parameter = value
	def __str__(self):
		return repr(self.parameter)

class Person:
	weight = -1
	hours_passed = -1
	alcohol_consumed = -1
	gender = "unknown"

	class BAC:
		bac_rate = -1
		def __init__(self):
			self.bac_rate = Person.alcohol_consumed * 5.14 / Person.weight \
				   * (BAC_RATE_MEN if (Person.gender == "man") else BAC_RATE_WOMEN) \
				   - 0.015 * Person.hours_passed
		def get_bac_rate(self):
			return self.bac_rate
		def isLegalDrive(self):
			return True if self.bac_rate < 0.08 else False


# Execute a program
you = Person()

try:
	you.alcohol_consumed = eval(input("How much total alcohol get consumed? "))
	if(you.alcohol_consumed < 0):
		raise inputException(The input must be positive number)

	you.weight = eval(input("How much is your body weight in pounds? "))
	if(you.weight < 0):
		raise inputException("The input must be positive number")

	you.gender = input("Are you a man or a woman? (man/woman) ").lower()
	if(you.gender != ("man" or "woman")):
		raise inputException("The input must be \'man\' or \'woman\'")

	you.hours_passed = eval(input("How much hours passed since the last drink? "))
	if(you.hours_passed < 0):
		raise inputException("The input must be positive number")

except inputException as err_msg:
	print("ERROR: %s" %err_msg)
	exit()

print("Your BAC is %.2f" %(you.BAC().get_bac_rate()))

if you.BAC().isLegalDrive():
	print("It is legal for you to drive.")
else:
	print("It is not legal for you to drive.")
