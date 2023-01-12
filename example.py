import this
import random
import math
x = math.sqrt(36)
print (x)

# Circumference Calculation
# Write a program that calculates the circumference of a wheel. The formula is C=2πr, 
# where π is the value 3.14 and r is the radius of the circle.
# To take this a step further, let the radius of the circle be a random integer generated 
# by the random module.
pie = 3.14
r = random.randint(1, 10)
circumference= 2*pie*r
print (circumference)