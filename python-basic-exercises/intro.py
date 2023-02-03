# Python Basics Exercises
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

















