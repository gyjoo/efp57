length = eval(input("What is the length of the room in feet? "))
width = eval(input("What is the width of the room in feet? "))

print("You entered dimensions of %0.3f feet by %0.3f feet." % (length, width))
print("The area is \n %0.3f square feet\n%0.3f square meters" %(length * width, length * width * 0.09290304))
