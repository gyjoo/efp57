principal = eval(input("What is the principal amount? "))
rate = eval(input("What is the rate? "))
years = eval(input("What is the number of years? "))
compounded_times = eval(input("What is the number of times the interest\nis compounded per year? "))

amount = principal * pow((1 + (rate / 100) / compounded_times), compounded_times * years)

print("$%d invested at %0.1f for %d years\ncompounded %d times per year is $%0.2f." %(principal, rate, years, compounded_times, amount))
