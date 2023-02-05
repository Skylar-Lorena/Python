# Functions are defined as blocks of code that perform tasks
# They begin with the def keyword

def greetings(name):
    print("Hello " + name)
greetings("Skylar")

# Exception Handling is the mechanism for stopping normal program flow and 
# continuing it at some surrounding code block.
# Simply put it is the art of spotting fatal errors that may come up in our applications and handling those errors.
def get_age():
    print("How old are you ")
    age = int(input())
    return age

print(get_age())

def get_age_num():
    print("How old are you ")
    try:
        age = int(input())
        return age
    except ValueError:
        return "That was not a valid input"
    
# Programmer Errors
# There are some error that are caused by programmers themselves. These errors should not be handled but fixed.
# 
# IndentationError - when you fail to separate code blocks properly.
# NameError - when you call an undefined variable function or method.
# TypeError - when you try and perform operations on unrelated types .
# 