pennies = int(input("How many pennies do you have?")) * .01
nickels = float(input("How many nickels do you have?")) * .05
dimes = float(input("How many dimes do you have?")) * .10
quarter = float(input("How many quarters do you have?")) *.25
half_dollar = float(input("How many half dollars do you have?")) * .50
dollars = float(input("How many dollars do you have?")) * 1.0
sum = pennies + nickels + dimes + dollars + quarter + dollars
print("The value of all your coins is $",sum)

