#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to Tips Calculator!")
bill = float(input('How much is the bill?: \n'))
people = float(input('How many people are going to seperate? \n'))
percentage = float(input('How much percentage for the tips? 12, 15, 20: \n'))
tips = (bill * percentage)/100
total = round((bill + tips), 2)
each_pay = total / people

print(f'Your total bill will be: {total}')
print(f'Each person have to pay: {each_pay}')