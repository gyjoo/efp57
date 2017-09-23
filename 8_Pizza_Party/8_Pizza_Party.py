ppl = eval(input("How many people? "))
pizza = eval(input("How many pizzas do you have? "))

pizza_per_person = int(8 * pizza / ppl)
leftover = pizza * 8 - pizza_per_person * ppl 

print(ppl, "people with %d pizzas" % pizza)
print("Each person gets %d pieces of pizza." % pizza_per_person)
print("There are %d leftover pieces." % leftover)
