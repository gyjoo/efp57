principal = eval(input("Enter the principal: "))
interest_rate = eval(input("Enter the rate of interest: "))
years = eval(input("Enter the number of years: "))

net_worth = principal * ( 1 + interest_rate/100 * 4)

print("After %d years at %0.1f, the investment will\nbe worth $%d." %(years, interest_rate, net_worth)) 
