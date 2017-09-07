euros = eval(input("How many euros are you exchanging? "))
rate = eval(input("What is the exchange rate? "))
amount = euros * (rate/100)
print("%d euros at an exchange rate of %0.2f is\n%0.2f U.S. dollars." %(euros, rate, amount))
