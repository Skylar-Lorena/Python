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
    try:
        age = int(input())
        return age
    except ValueError:
        return "That was not a valid input"
    

    