# Python Basics Exercises
import random
import this
# BMI calculator: Create a program in the Python shell that allows you to 
# calculate the body mass index of the person. This is calculated by dividing 
# a person's weight by their height in meters squared.

print("Welcome to the BMI calculator")
weight= 47
height= 1.57
bmi= weight/height
print("Your BMI is", bmi)

# Circumference Calculation
# Write a program that calculates the circumference of a wheel. The formula is C=2πr, 
# where π is the value 3.14 and r is the radius of the circle.
# To take this a step further, let the radius of the circle be a random integer generated 
# by the random module.
pie = 3.14
r = random.randint(1, 10)
circumference= 2*pie*r
print (circumference)

# Birthday dates
# Create a program where you prompt a user for their age and return the year they were born.
# After that, return the year they will turn 80.

print("What's your age?")
age= input()
print("You were born in", 2023-int(age))

# Car Loans
# Create a program in the Python shell that will calculate how long it would take a person to pay off 
# a car loan of $150,000 if the person only spends 25% of his salary of $15,000 to pay the loan assuming
# no interest is charged.
car_loan = 150000
salary = 150000
interest_rate = 0.25
amount_payable= salary*interest_rate
print(amount_payable)

time_frame= car_loan/amount_payable
print(time_frame)
















