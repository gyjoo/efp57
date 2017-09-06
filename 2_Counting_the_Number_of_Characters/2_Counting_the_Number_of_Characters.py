name = input("What is the input string? ")
name_char = list(name)
count = 0
for x in name_char:
  count += 1 # Python3 does not support ++
print(name + " has " + str(count) + " characters.")
