length = eval(input("What is the length of the room in feet? "))
width = eval(input("What is the width of the room in feet? "))

print("You entered dimensions of", length, "feet by", width, "feet.")
print("The area is \n", length*width, "square feet\n%0.3f square meters" %(length*width*0.09290304))
