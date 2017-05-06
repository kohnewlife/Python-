# Computing the amount of money given a quantity of bills and coins
# Enter the number of twenty dollar bills
twenties = int(input("Twenty dollar bills:"))
cents = twenties * 2000   # $20 = 2000 cents
# Then, the number of ten dollar bills
tens = int(input("Ten dollar bills:"))
cents += tens * 1000     # $10 = 1000 cents
# The number of five dollar bills
fives = int(input("Five dollar bills:"))
cents += fives * 500     # $5 = 500 cents
# Likewise
ones = int(input("One dollar bills:"))
cents += ones * 100
quarters = int(input("Quarters:"))
cents += quarters * 25
dimes = int(input("Dimes:"))
cents += dimes * 10
nickels = int(input("Nickels:"))
cents += nickels * 5
pennies = int(input("Pennies:"))
cents += pennies
# Now I got the total number of cents entered
print("")
# Finally, representing the total number of cents in dollars and cents format
print("Cash entered:", "${:.2f}".format(cents/100))
print("")
print("===============================")
print("")
# Next, do the reverse of the above problem: Monetary amount to currency
# Get the number of cents
cash = input("Please enter total cash (no dollar sign):")
money = float(cash)
cents = float(100*money)
# First, compute the number of twenty dollar bills in the given number of cents
twenties = float(cents) // 2000
print("Twenties:", round(twenties))
# Compute the remaining cents after the twenty dollar bills are accounted for
cents = float(cents) % 2000
# Next, compute the number of ten dollar bills
tens = float(cents) // 1000
print("Tens:", round(tens))
# Compute the remaining cents
cents = float(cents) % 1000
fives = float(cents) // 500
print("Fives:", round(fives))
cents = float(cents) % 500
ones = float(cents) // 100
print("Ones:", round(ones))
cents = float(cents) % 100
quarters = float(cents) // 25
print("Quarters:", round(quarters))
cents = float(cents) % 25
dimes = float(cents) // 10
print("Dimes:", round(dimes))
cents = float(cents) % 10
nickels = float(cents) // 5
print("Nickels:", round(nickels))
cents = float(cents) % 5
pennies = float(cents)
print("Pennies:", round(pennies))

