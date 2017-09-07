ppl = eval(input("How many people? "))
pizza = eval(input("How many pizzas do you have? "))

pizza_per_person = int(8*pizza/ppl)
leftover = pizza*8 - pizza_per_person * ppl 

print(ppl, "people with", pizza, "pizzas")
print("Each person gets", pizza_per_person, "pieces of pizza.")
print("There are", leftover ,"leftover pieces.")
