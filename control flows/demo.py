# Control flows help us add logic to our application
height = 157  
if height > 160:
    print("You are really short")

# > Greater than
# < Less than
# ==Equal to
# !=not equal to
# >= Greater than or equal to
# <=Less than or Equal to
# and Checks if both conditions evaluate to true
# or Checks if at least one condition is true
# not returns the opposite of the condition given
# The else statement comes right at the end of the if statement. 
# It is run only when the if statement evaluates to False
height = 199 
if height < 160:
    print("You are really short")
else:
    print("You are really tall")
    #  if we have more than one condition to check for? We can use elif, 
    #  which will allow us to check for multiple conditions
    height = 68 # inches
if height > 70 :
    print("You are really tall")
elif height > 60:
    print("You are of average height")

else:
    print("You are really short")