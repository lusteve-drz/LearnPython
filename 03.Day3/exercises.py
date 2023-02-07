# Exe 1
# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# e.g. 86 is even because 86 ÷ 2 = 43
# 43 does not have any decimal places. Therefore, the division is clean.
# e.g. 59 is odd because 59 ÷ 2 = 29.5

# number = int(input('Please enter a number!: '))
# if number % 2 == 0 :
#     print(f'{number} is a even number.')
# else:
#     print(f'{number} is an odd number.')
# --------------------------------------------------------------------------------------------
# Exe 2
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
#
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# weight = float(input('What is your weight?: '))
# height = float(input('What is your height?: '))
# bmi = round(weight / (height * height), 2)
#
# if bmi <= 18.5:
#     print(f'Your BMI is {bmi}, you are underweight.')
# elif bmi > 18.5 and bmi <= 25:
#     print(f'Your BMI is {bmi}, you have a normal weight.')
# elif bmi > 25 and bmi <= 30:
#     print(f'Your BMI is {bmi}, you are slightly overweight.')
# elif bmi > 30 and bmi <= 35:
#     print(f'Your BMI is {bmi}, you are obese!')
# else:
#     print(f'Your BMI is {bmi}, you are clinically obese!!!')
# --------------------------------------------------------------------------------------------
# Exe 3
# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.
# This is how you work out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4
# **except** every year that is evenly divisible by 100
# **unless** the year is also evenly divisible by 400

# year = int(input('Which year you would like to check: '))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Leap Year!!!')
#         else:
#             print('Not Leap Year!!!')
#     else:
#         print('Leap Year!!')
# else:
#     print('Not Leap!')
# --------------------------------------------------------------------------------------------
# Exe 4
# Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# print('Welcome to ST Pizza!')
# size = input('Which size do you want for your pizza? Small = s, Medium = m, Large = l: ').lower()
# pepperoni = input('Do you want to add Pepperoni for your pizza?: Yes = y or No = n: ').lower()
# cheese = input('Do you want to add extra cheese for your pizza?: Yes = y or No = n: ').lower()
# total = 0
#
# if size == 's':
#     total += 15
# elif size == 'm':
#     total += 20
# elif size == 'l':
#     total += 25
#
# if pepperoni == 'y' and size == 's':
#     total += 2
# elif pepperoni == 'y' and size == 'm' or size == 'l':
#     total += 3
#
# if cheese == 'y':
#     total += 1
#
# print(f'Your total bill for pizza is: {total}$.')
# --------------------------------------------------------------------------------------------
# Exe 5
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2-digit number.
print('Welcome to Love Calculator!')
first_name = input("What is your name? ").lower()
second_name = input("What is their name?: ").lower()

# first_total = first_name.count("t") + first_name.count("r") + first_name.count('u') + first_name.count('e') + \
#               first_name.count('l') + first_name.count('o') + first_name.count('v')
# second_total = second_name.count("t") + second_name.count("r") + second_name.count('u') + second_name.count('e') + \
#               second_name.count('l') + second_name.count('o') + second_name.count('v')
first_total = (first_name + second_name).count('t') + (first_name + second_name).count('r') + \
              (first_name + second_name).count('u') + (first_name + second_name).count('e')
second_total = (first_name + second_name).count('l') + (first_name + second_name).count('o') + \
              (first_name + second_name).count('v') + (first_name + second_name).count('e')
total = str(first_total) + str(second_total)
# print(f'{str(first_total) + str(second_total)}')
total = int(total)
if total <= 10 or total >= 90:
    print(f'Your score is {total}, you go together like coke and mentos.')
elif total >= 40 or total <= 50:
    print(f'Your score is {total}, you are alright together!')
else:
    print(f'Your score is {total}')

