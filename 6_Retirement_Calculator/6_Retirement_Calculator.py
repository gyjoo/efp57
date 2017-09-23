age = eval(input("What is your current age? "))
retire_age = eval(input("At what age would you like to retire? "))

print("You have %d years left until you can retire." % (retire_age - age))
print("It's 2017, so you can retire in %d" % (retire_age - age + 2017))
